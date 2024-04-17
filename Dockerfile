FROM python:3.10-slim

# Install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends git-lfs && rm -rf /var/lib/apt/lists/*

# Setup Git LFS
RUN git lfs install

WORKDIR /app
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
