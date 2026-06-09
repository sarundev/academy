FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the bot
CMD ["python", "bot.py"]
