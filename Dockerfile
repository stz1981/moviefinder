FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

# Make the start_and_run.sh script executable
RUN chmod +x ./setup_and_run.sh

# Use JSON array syntax for CMD
CMD ["sh", "./setup_and_run.sh"]
