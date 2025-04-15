#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
import logging
import yaml


sys.path.append(str(Path(__file__).resolve().parents[1]))
logger = logging.getLogger(__name__)

try:
    from common.logging_config import setup_logging
    from common.config import config

    setup_logging()

    logger.debug(
        "Loaded config.yml:\n%s",
        yaml.dump(config.get_full_config(), default_flow_style=False),
    )

except Exception as e:
    print(f"Failed to initialize logging: {e}")


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testvista.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
