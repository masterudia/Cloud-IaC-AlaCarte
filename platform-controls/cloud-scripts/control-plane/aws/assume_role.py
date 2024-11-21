#!/usr/bin/env python3
import boto3
import argparse
import sys
import os
import configparser
from botocore.exceptions import BotoCoreError, ClientError

def assume_role(role_arn, external_id, session_name='AssumeRoleSession'):
    """
    Assumes an AWS IAM role and returns temporary credentials.
    """
    try:
        # Create an STS client
        sts_client = boto3.client('sts')
        
        # Assume the role
        response = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name,
            ExternalId=external_id
        )
        
        # Extract temporary credentials
        credentials = response['Credentials']
        return credentials
    except ClientError as e:
        print(f'ClientError while assuming role: {e}')
        sys.exit(1)
    except BotoCoreError as e:
        print(f'BotoCoreError while assuming role: {e}')
        sys.exit(1)
    except Exception as e:
        print(f'Unexpected error while assuming role: {e}')
        sys.exit(1)

def list_s3_buckets(session):
    """
    Lists S3 buckets using the provided boto3 session.
    """
    try:
        s3_client = session.client('s3')
        response = s3_client.list_buckets()
        print('S3 Buckets:')
        for bucket in response.get('Buckets', []):
            print(f'  {bucket["Name"]}')
    except ClientError as e:
        print(f'ClientError while listing S3 buckets: {e}')
    except BotoCoreError as e:
        print(f'BotoCoreError while listing S3 buckets: {e}')
    except Exception as e:
        print(f'Unexpected error while listing S3 buckets: {e}')

def output_export_commands(credentials):
    """
    Outputs export commands for temporary credentials.
    """
    print('\nTo use the temporary credentials in your terminal, run the following commands:')
    print(f'export AWS_ACCESS_KEY_ID={credentials["AccessKeyId"]}')
    print(f'export AWS_SECRET_ACCESS_KEY={credentials["SecretAccessKey"]}')
    print(f'export AWS_SESSION_TOKEN={credentials["SessionToken"]}')

def write_credentials_to_profile(credentials, profile_name='assumed_role'):
    """
    Writes temporary credentials to AWS credentials file under a new profile.
    """
    aws_credentials_file = os.path.expanduser('~/.aws/credentials')
    config = configparser.ConfigParser()
    config.read(aws_credentials_file)
    
    config[profile_name] = {
        'aws_access_key_id': credentials['AccessKeyId'],
        'aws_secret_access_key': credentials['SecretAccessKey'],
        'aws_session_token': credentials['SessionToken']
    }
    
    with open(aws_credentials_file, 'w') as configfile:
        config.write(configfile)
    
    print(f'\nTemporary credentials have been written to profile [{profile_name}] in {aws_credentials_file}')
    print(f'Use --profile {profile_name} with AWS CLI commands to use these credentials.')

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Assume an AWS IAM role using an external ID.')
    parser.add_argument('--role-arn', required=True, help='The ARN of the role to assume.')
    parser.add_argument('--external-id', required=True, help='The external ID for role assumption.')
    parser.add_argument('--session-name', default='AssumeRoleSession', help='An identifier for the assumed role session.')
    parser.add_argument('--output-credentials', choices=['export', 'profile'], help='Output temporary credentials as export commands or write to AWS profile.')
    parser.add_argument('--profile-name', default='assumed_role', help='Profile name to use when writing credentials to AWS credentials file.')
    args = parser.parse_args()
    
    # Assume the role
    credentials = assume_role(args.role_arn, args.external_id, args.session_name)
    
    if not credentials:
        print('Failed to assume role. Exiting.')
        sys.exit(1)
    
    # Use the temporary credentials to create a new session
    try:
        temp_session = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken']
        )
    except Exception as e:
        print(f'Error creating boto3 session with temporary credentials: {e}')
        sys.exit(1)
    
    # Example operation: List S3 buckets
    list_s3_buckets(temp_session)
    
    # Output credentials based on user choice
    if args.output_credentials == 'export':
        output_export_commands(credentials)
    elif args.output_credentials == 'profile':
        write_credentials_to_profile(credentials, args.profile_name)

if __name__ == '__main__':
    main()