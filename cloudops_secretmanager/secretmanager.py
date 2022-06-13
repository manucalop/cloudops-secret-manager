import json
import yaml
from typing import Protocol


class SecretManagerProtocol(Protocol):
    def pull(self) -> dict:
        ...

    def push(self, payload: dict) -> None:
        ...


class JSONSecretManager:
    def __init__(self, path: str):
        self.path = path

    def pull(self) -> dict:
        with open(self.path, "r") as f:
            return json.load(f)

    def push(self, payload: dict) -> None:
        with open(self.path, "w") as f:
            json.dump(payload, f)


class YAMLSecretManager:
    def __init__(self, path: str):
        self.path = path

    def pull(self) -> dict:
        with open(self.path, "r") as f:
            return yaml.safe_load(f)

    def push(self, payload: dict) -> None:
        with open(self.path, "w") as f:
            yaml.dump(payload, f)
