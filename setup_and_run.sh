#!/bin/bash

# Update and install dependencies
apt-get update && apt-get upgrade -y
apt-get install -y cron

# Install Python dependencies
pip install --upgrade pip --root-user-action=ignore
pip install --no-cache-dir -r requirements.txt --root-user-action=ignore

# Add crontab file in the cron directory
cp crontab /etc/cron.d/container-cron

# Give execution rights on the cron job
chmod 0644 /etc/cron.d/container-cron

# Apply cron job
crontab /etc/cron.d/container-cron

# Create the log file to be able to run tail
touch /var/log/cron.log

# Start cron
cron
# Optional: Add any other cron jobs you need, such as database backups or log rotation
# Example: Clean up unused packages every week
echo "0 1 * * 0 apt-get update && apt-get upgrade -y" | crontab -
echo "0 3 * * 0 apt-get autoremove -y && apt-get clean" | crontab -

# Start the bot script
python ./bot.py
