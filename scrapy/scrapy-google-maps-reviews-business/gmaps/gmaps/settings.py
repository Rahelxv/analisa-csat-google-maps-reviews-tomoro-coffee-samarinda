BOT_NAME = "gmaps"

SPIDER_MODULES = ["gmaps.spiders"]
NEWSPIDER_MODULE = "gmaps.spiders"

DOWNLOAD_HANDLERS = {
"https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
 "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}



ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 1
COOKIES_ENABLED = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": False,
}

PLAYWRIGHT_PROCESS_REQUEST_HEADERS = None