# Base Image
FROM python:3.9

# Working Directory
WORKDIR /app

# Copy requirements.txt and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy sreality_scraper and web_server
COPY sreality_scraper/ sreality_scraper/
COPY web_server/ web_server/

# Copy entry_script.sh
COPY entry_script.sh .

# Make script executable
RUN chmod +x entry_script.sh

# Command to run
CMD [ "./entry_script.sh" ]

