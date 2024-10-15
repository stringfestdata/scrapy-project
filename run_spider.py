# run_spider.py

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mycrawler.spiders.quotes_spider import QuotesSpider

# Set up a process to run the spider
process = CrawlerProcess(get_project_settings())

# Run the spider
process.crawl(QuotesSpider)
process.start()  # This will block until the crawling is finished
