# ------------ Builder Stage ------------
FROM python:3.12-slim as builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up venv manually
RUN python -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy requirements and install
COPY backend/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install local Ventureviz package using PEP 621 (pyproject.toml)
COPY crewai/ ./crewai/
RUN pip install ./crewai

# ------------ Production Stage ------------
FROM python:3.12-slim as production

WORKDIR /app

# Copy the virtual environment from builder
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy project files
COPY backend/ ./backend/
COPY crewai/ ./crewai/

# Set environment variable for Python path (so Django finds ventureviz module)
ENV PYTHONPATH="/app/crewai/src"

# Expose port
EXPOSE 8000

# Default CMD
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]