import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load the environment variables from .env
load_dotenv()

# Absolute path to project root
ROOT_DIR = Path(__file__).resolve().parent.parent.parent  # ventureviz/

# Add PYTHONPATH from .env relative to root
PYTHONPATH = os.getenv("PYTHONPATH")
if PYTHONPATH:
    crewai_path = (ROOT_DIR / PYTHONPATH).resolve()
    if str(crewai_path) not in sys.path:
        sys.path.insert(0, str(crewai_path))

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.production')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
