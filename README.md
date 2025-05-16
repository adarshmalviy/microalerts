# microalerts

Lightweight alerting library to send notifications from your microservices to Slack (and soon other platforms).

## Installation

```bash
pip install .
```

## Usage

```python
from microalerts import send_alert

send_alert(
    message="Kafka consumer crashed.",
    webhook_url="https://hooks.slack.com/services/...",
    client="SilverPearl",
    service="stream-pipeline",
    env="prod",
    level="error"
)
```