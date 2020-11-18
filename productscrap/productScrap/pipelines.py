# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ProductScrapPipeline(object):
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = sqlite3.connect("products.db")
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        price = float(item['price'][0].replace('R$','').replace('.','').replace(',','.'))
        self.curr.execute("""insert into products_price_hist_tb values (?,?,CURRENT_DATE)""",(
            item['title'][0],
            price
        ))
        self.conn.commit()