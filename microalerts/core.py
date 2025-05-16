import requests
import json
from .formatter import build_slack_blocks

def send_alert(
    message: str,
    webhook_url: str,
    client: str,
    service: str,
    env: str = "dev",
    level: str = "error",
) -> None:
    """
    Send a Slack alert using Slack Blocks formatting.

    Args:
        message (str): The main error or alert message.
        webhook_url (str): Slack Incoming Webhook URL.
        client (str): Client name (e.g., SilverPearl).
        service (str): Microservice name (e.g., auth-service).
        env (str): Environment (e.g., dev, prod).
        level (str): Log level (info, warning, error).
    """
    blocks = build_slack_blocks(message, client, service, env, level)
    payload = {"blocks": blocks}

    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=5,
        )
        if response.status_code != 200:
            print(f"Slack alert failed: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Exception sending alert: {e}")