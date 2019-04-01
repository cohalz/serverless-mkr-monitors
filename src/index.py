import urllib.request
import json
import urllib.parse
import boto3
import os


def handler(event, context):

    print(event)

    payload = json.loads(urllib.parse.unquote_plus(event['body']))
    print(payload)

    response = {}

    client = boto3.client('codebuild')

    client.start_build(
        projectName=os.environ["CODEBUILD_PROJECT"],
        environmentVariablesOverride=[{
            'name': 'COMMIT_MESSAGE',
            'value': f"{payload['event']}: {payload['monitor']['name']}"
        }]
    )

    response['statusCode'] = 200
    response['body'] = "ok"

    return response
