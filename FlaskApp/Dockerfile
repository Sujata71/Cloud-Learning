# Step 1: Use a lightweight, secure official Python image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file over first for better layer caching
COPY requirements.txt .

# Step 4: Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of our application code into the image
COPY . .

# Step 6: Document that the container listens on port 5000
EXPOSE 5000

# Step 7: Launch the Flask web server automatically upon boot
CMD ["python", "app.py"]