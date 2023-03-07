# Use an official Python Image
FROM python:3

# Set the working directory to /app
WORKDIR /app

#Copying the meter code
COPY Meter.py /app

#Installing pika client
RUN python3 -m pip install pika --upgrade

#Entry point to execute program
CMD ["python3", "Meter.py"]