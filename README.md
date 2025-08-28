# Fake Services
Some fake servers for developing and testing

## Installation
```
uv pip install -r requirements.txt
```

## Fake SMTP server
Run a basic debugging server on localhost, port 8025 (default)
```
uv run python -m aiosmtpd -n -l localhost:8025
```

Run fake SMTP server programmatically
```
uv run python smtp_server.py
```

Test fake SMTP server
```
uv run python main.py
```