
def build_slack_blocks(message: str, client: str, service: str, env: str, level: str):
    emoji = {
        "error": ":x:",
        "warning": ":warning:",
        "info": ":information_source:",
    }.get(level, ":grey_question:")

    header_text = f"{emoji} Microservice Alert"

    blocks = [
        {"type": "header", "text": {"type": "plain_text", "text": header_text}},
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Client:*\n{client}"},
                {"type": "mrkdwn", "text": f"*Service:*\n{service}"},
                {"type": "mrkdwn", "text": f"*Environment:*\n`{env}`"},
                {"type": "mrkdwn", "text": f"*Level:*\n{emoji} {level.upper()}"},
            ],
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Message:*\n{message}"},
        },
    ]

    return blocks
