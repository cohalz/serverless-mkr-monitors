import json
import boto3
import os


def handler(event, context):

    client = boto3.client('codebuild')

    payload = json.loads(event['body'])

    operator = get_operator(payload['user'])

    client.start_build(
        projectName=os.environ['CODEBUILD_PROJECT'],
        environmentVariablesOverride=[{
            'name': 'COMMIT_MESSAGE',
            'value': f"{payload['event']}: "
                     f"{payload['monitor']['name']} by {operator}"
        }]
    )

    return {
        'statusCode': 200,
        'body': 'ok'
    }


def get_operator(user):
    if user is not None:
        return user['screenName']
    else:
        return 'mkr monitors push'
