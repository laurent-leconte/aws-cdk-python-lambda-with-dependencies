from aws_lambda_typing import context as context_, events

def handler(event: events.APIGatewayProxyEventV1, context: context_.Context):
    method = event['requestContext']['httpMethod']
    path = event['requestContext']['path']
    print(f"{method} {path}")
    echo = ""
    if method == 'GET':
        query_params = event['queryStringParameters']
        echo = "&".join(f"{k}={v}" for k,v in query_params.items())
    elif method == 'POST':
        echo = str(event['body'])

    return {
        'statusCode': 200,
        'headers': { "Content-Type": "text/plain" },
        'body': echo + " right back at you"
    }