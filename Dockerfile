# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements files into the container at /app
COPY ./sreality_scraper/requirements.txt ./scraper_requirements.txt
COPY ./web_server/requirements.txt ./server_requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r scraper_requirements.txt
RUN pip install --trusted-host pypi.python.org -r server_requirements.txt

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./sreality_scraper /app/scraper
COPY ./web_server /app/server

# Make ports available to the world outside this container
EXPOSE 8070

# Run command
CMD ["bash", "-c", "scrapy runspider /app/scraper/sreality_scraper/spiders/item_spider_1.py && python /app/server/http_server.py"]
