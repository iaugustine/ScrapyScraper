# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
import requests

global datacontainer
datacontainer = []

class EventscraperPipeline:

    def open_spider(self, spider):
        # self.file = open('items1.json', 'w')
        pass

    def close_spider(self,spider):
        global datacontainer
        r =requests.put("http://127.0.0.1:5000/bulk_index?type=events", json=datacontainer)
        print(r)       


    def process_item(self, item, spider):
        # line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        # self.file.write(line)
        global datacontainer
        datacontainer.append(dict(item))
        return item

        
    # def process_item(self, item, spider):
    #     print('In the pipeline')
    #     for data in item:
    #         print(data)
    #     return item
