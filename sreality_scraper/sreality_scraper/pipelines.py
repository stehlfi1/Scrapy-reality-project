# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class SrealityScraperPipeline:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="db",
            database="sreality_dat",
            user="admin",
            password="admin1"
        )
        self.cursor = self.connection.cursor()

    def open_spider(self, spider):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS scraped_data (
                            id SERIAL PRIMARY KEY,
                            title TEXT,
                            image_url TEXT);""")
        self.connection.commit()

    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO scraped_data (title, image_url) VALUES (%s, %s)",
                            (item['name'], item['image_url']))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()
