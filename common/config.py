import os
import yaml


class AppConfig:
    _instance = None

    def __new__(cls, config_path=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load(config_path)
        return cls._instance

    def _load(self, config_path=None):
        path = config_path or os.getenv("APP_CONFIG_PATH", "/app/config/config.yml")
        with open(path, "r") as f:
            self._config = yaml.safe_load(f) or {}

    def reload(self, config_path=None):
        self._load(config_path)

    def get_section(self, section_name: str, default=None):
        return self._config.get(section_name, default or {})

    def get_value(self, section: str, key: str, default=None):
        return self._config.get(section, {}).get(key, default)

    def get(self, key: str, default=None):
        return self._config.get(key, default)

    def get_full_config(self):
        return self._config.copy()

    def is_feature_enabled(self, flag_name: str) -> bool:
        return self.get_value("feature_flags", flag_name, False)


config = AppConfig()
