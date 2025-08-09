#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Absolute path to project root
ROOT_DIR = Path(__file__).resolve().parent.parent  # ventureviz/

# Add PYTHONPATH from .env relative to root
PYTHONPATH = os.getenv("PYTHONPATH")
if PYTHONPATH:
    module_path = (ROOT_DIR / PYTHONPATH).resolve()
    if str(module_path) not in sys.path:
        sys.path.insert(0, str(module_path))

def main():
    """Run administrative tasks."""

    # ✅ Default to production settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.production')

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