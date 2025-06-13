import sys
import types
import importlib.util
from pathlib import Path
from unittest import mock

# Provide minimal stubs so assume_role.py can be imported without boto3/botocore
boto3_stub = types.ModuleType('boto3')

def _default_client(service_name):
    raise RuntimeError('boto3.client not patched for %s' % service_name)

boto3_stub.client = _default_client

class DummySession:
    def __init__(self, **kwargs):
        self._client = None
    def client(self, service_name):
        return _default_client(service_name)

boto3_stub.Session = DummySession

botocore_stub = types.ModuleType('botocore')
exceptions_stub = types.ModuleType('botocore.exceptions')
class BotoCoreError(Exception):
    pass
class ClientError(Exception):
    pass
exceptions_stub.BotoCoreError = BotoCoreError
exceptions_stub.ClientError = ClientError
botocore_stub.exceptions = exceptions_stub

sys.modules.setdefault('boto3', boto3_stub)
sys.modules.setdefault('botocore', botocore_stub)
sys.modules.setdefault('botocore.exceptions', exceptions_stub)

# Load the module under test
MODULE_PATH = Path(__file__).resolve().parents[1] / 'assume_role.py'
spec = importlib.util.spec_from_file_location('assume_role', MODULE_PATH)
assume_role = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assume_role)


def test_assume_role(monkeypatch):
    credentials = {
        'AccessKeyId': 'AKIA123',
        'SecretAccessKey': 'SECRET',
        'SessionToken': 'TOKEN'
    }
    response = {'Credentials': credentials}
    mock_client = mock.Mock()
    mock_client.assume_role.return_value = response
    monkeypatch.setattr(assume_role.boto3, 'client', lambda service: mock_client)

    creds = assume_role.assume_role('arn:aws:iam::123:role/demo', 'ext', 'sess')
    assert creds == credentials
    mock_client.assume_role.assert_called_once_with(
        RoleArn='arn:aws:iam::123:role/demo',
        RoleSessionName='sess',
        ExternalId='ext'
    )


def test_list_s3_buckets(capsys):
    buckets_response = {'Buckets': [{'Name': 'bucket1'}, {'Name': 'bucket2'}]}
    mock_s3 = mock.Mock()
    mock_s3.list_buckets.return_value = buckets_response

    class Session:
        def client(self, service_name):
            assert service_name == 's3'
            return mock_s3

    assume_role.list_s3_buckets(Session())
    output = capsys.readouterr().out
    assert 'S3 Buckets:' in output
    assert 'bucket1' in output
    assert 'bucket2' in output
    mock_s3.list_buckets.assert_called_once()


def test_output_export_commands(capsys):
    credentials = {
        'AccessKeyId': 'AKIAID',
        'SecretAccessKey': 'SECRET',
        'SessionToken': 'TOKEN'
    }
    assume_role.output_export_commands(credentials)
    out = capsys.readouterr().out
    assert f"export AWS_ACCESS_KEY_ID={credentials['AccessKeyId']}" in out
    assert f"export AWS_SECRET_ACCESS_KEY={credentials['SecretAccessKey']}" in out
    assert f"export AWS_SESSION_TOKEN={credentials['SessionToken']}" in out
