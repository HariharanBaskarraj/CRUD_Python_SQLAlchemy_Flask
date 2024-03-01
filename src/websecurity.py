from keycloak import KeycloakOpenID

KEYCLOAK_SETTINGS = {
    "server_url": "YOUR_KEYCLOAK_SERVER_URL",
    "client_id": "YOUR_CLIENT_ID",
    "realm_name": "YOUR_REALM_NAME",
    "client_secret_key": "YOUR_CLIENT_SECRET_KEY",
}

keycloak_openid = KeycloakOpenID(**KEYCLOAK_SETTINGS)