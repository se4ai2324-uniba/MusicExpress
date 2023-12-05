# Base Image
FROM python:3.11.6

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy the whole current directory into the container
COPY . .

# Install requirements.txt (project dependencies)
RUN pip install -r requirements.txt

# Set the working directory to "/src" within the container
WORKDIR /src

# Expose port 8000
EXPOSE 8000

# Command to run the UVicorn server for the API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
