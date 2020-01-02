# Monitoring Service

This service currently acts as a consumer for the redis stream which can publish events to it.

# Installation
(To install a pyenv virtualenv)
```bash
pyenv virtualenv -p python3.6 3.6.8 monitoring-service
```

Install the requirements into your virtualenv
```bash
pip install -e ".[dev]"
```

Run Unit Test
```bash
Make test
```

To run the service
```bash
Make run
```
