from infisical.models.api import GetSecretsDTO, SecretsResponse
from requests import Session


def get_secrets_req(api_request: Session, options: GetSecretsDTO) -> SecretsResponse:
    """Send request again Infisical API to fetch secrets.
    See more information on https://infisical.com/docs/api-reference/endpoints/secrets/read

    :param api_request: The :class:`requests.Session` instance used to perform the request
    :param workspace_id: The ID of the workspace
    :param environment: The environment
    :return: Returns the API response as-is
    """
    response = api_request.get(
        "/api/v3/secrets",
        params={
            "environment": options.environment,
            "workspaceId": options.workspace_id,
        },
    )

    return SecretsResponse.parse_obj(response.json())
