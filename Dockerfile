FROM python:3.10-slim

# Set up the working directory
WORKDIR /app

# Copy the source code and requirements file
COPY ./src /app/src
COPY ./requirements.txt /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the desired port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
