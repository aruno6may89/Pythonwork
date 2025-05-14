FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/
COPY tests/ ./tests/
COPY scripts/ ./scripts/

# Command to run the SMS_template.py script
CMD ["python", "src/SMS_template.py"]