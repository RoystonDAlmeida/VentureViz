#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()   # Load the env variables

# Set PYTHONPATH manually
PYTHONPATH = os.getenv("PYTHONPATH")
if PYTHONPATH and PYTHONPATH not in sys.path:
    sys.path.insert(0, str(Path(PYTHONPATH).resolve()))

def main():
    """Run administrative tasks."""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()