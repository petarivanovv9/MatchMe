import scrapy
import json
from crawler.items import EventItem

class FacebookSpider(scrapy.Spider):
    name = "facebook"
    allowed_domains = ["graph.facebook.com"]

    #start_urls = ["http://target.com/"]

    def __init__(self, *args, **kwargs):
        super(FacebookSpider, self).__init__(*args, **kwargs)
        commands_filepath = "./" + self.name + "_" + "commands.json"

        json_data = open(commands_filepath).read()

        commands = json.loads(json_data)
        commands['a_token'] = "&access_token=" + commands['token']

        self.start_urls = map(lambda v: commands['base_url'] + v + commands['a_token'], commands['start_urls'])

    def parse(self, response):
        data = json.loads(response.body)

        for post in data['data']:
            item = EventItem()
            item['origine_id'] = post.get('id')
            item['name'] = post.get('name')
            item['description'] = post.get('description')
            item['place'] = post.get('place')
            item['start_time'] = post.get('start_time')
            item['end_time'] = post.get('end_time')

            yield item

        if 'paging' in data:
            yield scrapy.Request(data['paging']['next'], callback=self.parse)
