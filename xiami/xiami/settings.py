# Scrapy settings for xiami project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
BOT_NAME = 'xiami'
LOG_LEVEL = 'DEBUG'
COOKIES_ENABLED = True
RETRY_ENABLED = True
SPIDER_MODULES = ['xiami.spiders']
NEWSPIDER_MODULE = 'xiami.spiders'
ITEM_PIPELINES = ['xiami.pipelines.XiamiPipeline']
DOWNLOAD_DELAY = 0.5
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'


USER_AGENT_LIST = [
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10']
HTTP_PROXY = 'http://127.0.0.1:8123'


DOWNLOADER_MIDDLEWARES = {
	'xiami.middlewares.RandomUserAgentMiddleware': 400,
    # 'xiami.middlewares.ProxyMiddleware': 410,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None}