# Assume Role Python Script
This script allows you to assume an AWS IAM role programmatically using the **boto3** library. It retrieves temporary security credentials for the specified role and can be used to interact with AWS services under that role's permissions.

# Features

	•	Assumes a specified IAM role using AWS STS.
	•	Retrieves temporary security credentials.
	•	Configures a boto3 session using the temporary credentials.


## Prerequisites

```
python3 --version
````
AWS CLI Credentials: The script uses your default AWS CLI credentials to assume the role. Ensure these are configured:
```
aws configure
```


