import aws_cdk as core
import aws_cdk.assertions as assertions

from projectfinal.projectfinal_stack import ProjectfinalStack

# example tests. To run these tests, uncomment this file along with the example
# resource in projectfinal/projectfinal_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProjectfinalStack(app, "projectfinal")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
