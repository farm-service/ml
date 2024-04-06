# Base image
FROM python:3.10

# Working directory within the container
WORKDIR /app 

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy your essential files
COPY models/forecaster_hawaii_m.pkl ./
COPY main.py ./

# Execute your inference script 
CMD ["flask", "--app", "main.py", "run", "--host=0.0.0.0"]
