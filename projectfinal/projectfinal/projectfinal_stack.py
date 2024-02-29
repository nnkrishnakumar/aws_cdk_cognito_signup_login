from aws_cdk import core
from aws_cdk import aws_cognito as cognito

class MyCognitoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a Cognito User Pool
        user_pool = cognito.UserPool(self, "MyUserPool",
            user_verification=cognito.UserVerificationConfig(
                email_subject="Verify your email for our awesome app!",
                email_body="Thanks for signing up to our awesome app! Your verification code is {####}",
                email_style=cognito.VerificationEmailStyle.CODE
            ),
            self_sign_up_enabled=True,
            sign_in_aliases=cognito.SignInAliases(username=True, email=True),
            password_policy=cognito.PasswordPolicy(
                min_length=8,
                require_lowercase=True,
                require_digits=True,
                require_uppercase=True,
                require_symbols=True,
            )
        )

        # Output the User Pool ID
        core.CfnOutput(self, "UserPoolId", value=user_pool.user_pool_id)