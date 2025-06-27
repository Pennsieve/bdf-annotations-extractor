import os
import boto3
import requests

def authenticate():

    PENNSIEVE_URL = "https://api.pennsieve.io"
    email = os.getenv("API_TOKEN")
    password = os.getenv("API_SECRET")

    r = requests.get(f"{PENNSIEVE_URL}/authentication/cognito-config")
    r.raise_for_status()

    print(r.json())
    cognito_app_client_id = r.json()["userPool"]["appClientId"]
    cognito_region = r.json()["userPool"]["region"]

    cognito_client = boto3.client(
        "cognito-idp",
        region_name=cognito_region,
        aws_access_key_id=email,
        aws_secret_access_key=password,
    )

    login_response = cognito_client.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={"USERNAME": email, "PASSWORD": password},
        ClientId=cognito_app_client_id
    )

    api_key = login_response["AuthenticationResult"]["AccessToken"]

    # r = requests.get(f"{PENNSIEVE_URL}/user", headers={"Authorization": f"Bearer {api_key}"})
    # r.raise_for_status()
    return api_key
