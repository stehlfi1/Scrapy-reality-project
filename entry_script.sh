#!/bin/bash

# sleep 10
echo "Starting scraper..."
# Run scraper
cd sreality_scraper
scrapy runspider ./sreality_scraper/spiders/item_spider_1.py
SCRAPY_STATUS=$?
cd ..

# Check if scraper was successful
if [ $SCRAPY_STATUS -eq 0 ]; then
  echo "Scraper finished, starting web server..."
  # Run web server
  exec python web_server/http_server.py
else
  echo "Scrapy failed with status code $SCRAPY_STATUS"
  exit $SCRAPY_STATUS
fi
