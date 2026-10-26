#Pull the python image from docker hub
#Use a lightweight version of python image to reduce the size of the image
FROM python: 3.14-slim

#Set the working directory in the container
WORKDIR /app

#Copy the dependency list before coping application code
COPY requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy the application code and saved model inside /app
COPY . .

#Document the  port used by the FastAPI application
EXPOSE 8000

#Start the API server when container is ready
#0.0.0.0 - allows the connections through the container's network interface
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]