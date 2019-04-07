import json
import boto3
import os


def handler(event, context):

    payload = json.loads(event['body'])
    print(payload)

    client = boto3.client('codebuild')

    client.start_build(
        projectName=os.environ["CODEBUILD_PROJECT"],
        environmentVariablesOverride=[{
            'name': 'COMMIT_MESSAGE',
            'value': f"{payload['event']}: {payload['monitor']['name']} by {payload['user']['screenName']}"
        }]
    )

    return {
        'statusCode': 200,
        'body': 'ok'
    }
