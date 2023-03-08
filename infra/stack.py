from aws_cdk import (
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as lambda_python,
    Stack
)
from constructs import Construct

class EchoService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        handler = lambda_python.PythonFunction( 
            self,
            "echo_lambda",
            entry="src",  # this should point to the root level of your applicative code
            runtime=lambda_.Runtime.PYTHON_3_9,
            index="echo/main.py",  # relative path to your main Python file, from `entry`
            handler="handler"  # which function to call in the main Python file
        )

        api = apigateway.RestApi(
            self,
            "echo_lambda_apigw"
        )

        api_lambda_integration = apigateway.LambdaIntegration(
            handler,
            request_templates={"application/json": '{ "statusCode": "200" }'}
        )

        api.root.add_method("GET", api_lambda_integration)
        api.root.add_method("POST", api_lambda_integration)

class EchoServiceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        EchoService(self, "echoService")