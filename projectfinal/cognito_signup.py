import boto3

# Set up Amazon Cognito parameters
user_pool_id = 'ap-south-1_71XRELjrG'
client_id = '4h1514k633kri2oioc1lnvl9rt'  # Assuming this is your client ID
region_name = 'ap-south-1'  # The region where your Cognito User Pool resides

# Initialize the Amazon Cognito client
client = boto3.client('cognito-idp', region_name=region_name)

# Function to sign up a new user
def sign_up(username, password, email):
    try:
        response = client.sign_up(
            ClientId=client_id,
            Username=username,
            Password=password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                }
            ]
        )
        print('User signed up successfully:', response)
    except client.exceptions.UsernameExistsException:
        print('Username already exists')
    except Exception as e:
        print('Error signing up user:', e)

# Function to log in a user and obtain JWT token
def log_in(username, password):
    try:
        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            },
            ClientId=client_id
        )
        print('User logged in successfully')
        return response['AuthenticationResult']['IdToken']
    except client.exceptions.NotAuthorizedException:
        print('Incorrect username or password')
    except Exception as e:
        print('Error logging in user:', e)
        return None

# Function to verify user's email address
def verify_email(username, verification_code):
    try:
        response = client.confirm_sign_up(
            ClientId=client_id,
            Username=username,
            ConfirmationCode=verification_code
        )
        print('User email verified successfully:', response)
    except client.exceptions.UserNotFoundException:
        print('User not found')
    except client.exceptions.CodeMismatchException:
        print('Incorrect verification code')
    except Exception as e:
        print('Error verifying email:', e)


# import argparse

# def main():
#     parser = argparse.ArgumentParser(description='Process username and password.')

#     # Add arguments for username and password
#     parser.add_argument('-u', '--username', type=str, help='Username for authentication')
#     parser.add_argument('-p', '--password', type=str, help='Password for authentication')

#     args = parser.parse_args()

#     # Check if both username and password are provided
#     if args.username and args.password:
#         print("Username:", args.username)
#         print("Password:", args.password)
#         username=args.username
#         password=args.password
#         log_in(username,password)
#     else:
#         print("Please provide both username and password.")

# if __name__ == "__main__":
#     main()
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process username and password.')

    # Add arguments for username and password
    parser.add_argument('-u', '--username', type=str, help='Username for authentication')
    parser.add_argument('-p', '--password', type=str, help='Password for authentication')

    args = parser.parse_args()

    # Check if both username and password are provided
    if args.username and args.password:
        print("Username:", args.username)
        print("Password:", args.password)
        username = args.username
        password = args.password
        jwt_token = log_in(username, password)  # Get the JWT token
        if jwt_token:
            print("JWT Token:", jwt_token)
        else:
            print("Login failed. Please check your credentials.")
    else:
        print("Please provide both username and password.")

if __name__ == "__main__":
    main()
