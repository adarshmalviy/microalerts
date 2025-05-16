import requests
import json

def send_alert(
    message: str,
    webhook_url: str,
    client: str,
    service: str,
    env: str = "dev",
    level: str = "error"
) -> None:
    """
    Send a formatted alert message to a Slack webhook.

    Args:
        message (str): The main error or alert message.
        webhook_url (str): Slack Incoming Webhook URL.
        client (str): Client name (e.g., SilverPearl).
        service (str): Microservice name (e.g., auth-service).
        env (str): Environment (e.g., dev, prod).
        level (str): Log level (info, warning, error).
    """
    emoji = {
        "error": ":x:",
        "warning": ":warning:",
        "info": ":information_source:"
    }.get(level, ":grey_question:")

    payload = {
        "text": f"{emoji} *[{client.upper()} | {service.upper()} | {env.upper()}]*\n{message}"
    }

    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        if response.status_code != 200:
            print(f"Slack alert failed: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Exception sending alert: {e}")