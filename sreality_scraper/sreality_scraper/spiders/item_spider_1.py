import scrapy
import json
import html

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500"]

    def parse(self, response):
        # Parse JSON response
        data = json.loads(response.text)
        
        # Loop through each estate item
        for estate in data["_embedded"]["estates"]:
            # Extract and decode name and first image URL
            name = html.unescape(estate.get('name', 'N/A'))
            image_url = estate['_links']['images'][0]['href'] if estate['_links'].get('images') else 'N/A'
            
            yield {
                'name': name,
                'image_url': image_url,
            }
