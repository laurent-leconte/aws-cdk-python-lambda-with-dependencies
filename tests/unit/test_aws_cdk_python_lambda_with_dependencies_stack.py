import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_python_lambda_with_dependencies.aws_cdk_python_lambda_with_dependencies_stack import AwsCdkPythonLambdaWithDependenciesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_python_lambda_with_dependencies/aws_cdk_python_lambda_with_dependencies_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkPythonLambdaWithDependenciesStack(app, "aws-cdk-python-lambda-with-dependencies")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
