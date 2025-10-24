FROM mcr.microsoft.com/devcontainers/python:3.12

# Install system packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Optional: install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Optional: install Python packages globally
RUN pip install --upgrade pip
