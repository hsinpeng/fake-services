# Fake Services
Some fake servers for developing and testing

## Installation
```
uv pip install -r requirements.txt
```

## Fake SMTP server
### Run server
(1) Run a basic debugging server on localhost, port 8025 (default)
```
uv run python -m aiosmtpd -n -l localhost:8025
```

(2) Run fake SMTP server programmatically
```
uv run python smtp_server.py -n [host_name] -p [port_number]
```
### Sender testing
Test fake SMTP server by sending email
```
uv run python main.py -o 1
```