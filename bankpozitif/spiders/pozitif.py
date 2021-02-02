import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from bankpozitif.items import Article


class PozitifSpider(scrapy.Spider):
    name = 'pozitif'
    allowed_domains = ['bankpozitif.com.tr']
    start_urls = ['https://www.bankpozitif.com.tr/Tr/BizKimiz/haberler']

    def parse(self, response):
        with open('response.html', 'wb') as f:
            f.write(response.body)

        contents = []
        titles = response.xpath('//div[@class="mkAccordion"]/a/span/text()').getall()
        all_content = response.xpath('//div[@class="mkAccordion"]/div')
        for content in all_content:
            contents.append(" ".join(content.xpath('.//text()').getall()))

        for i, title in enumerate(titles):
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            title = title.split(" ")
            date = title[0]
            try:
                date = datetime.strptime(date, '%d.%m.%Y')
                date = date.strftime('%Y/%m/%d')
            except:
                date = ''

            item.add_value('title', " ".join(title[1:]))
            item.add_value('content', contents[i])
            item.add_value('date', date)

            yield item.load_item()
