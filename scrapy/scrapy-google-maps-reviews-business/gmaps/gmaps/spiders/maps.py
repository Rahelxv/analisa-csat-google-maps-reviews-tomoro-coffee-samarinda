import scrapy
from scrapy_playwright.page import PageMethod


class MapsSpider(scrapy.Spider):
    name = "maps"

    async def start(self):
        url = "https://www.google.com/maps/search/tomoro+coffee+samarinda"  
        yield scrapy.Request(
            url,
            callback=self.parse_list,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "a.hfpxzc"),
                    PageMethod("wait_for_timeout", 3000),
                ],
            },
        )

    def parse_list(self, response):
        cards = response.css("a.hfpxzc")
        self.logger.info(f"Ketemu {len(cards)} hasil di list")

        for card in cards:
            href = card.attrib.get("href")
            if href:
                yield scrapy.Request(
                    href,
                    callback=self.parse_detail,
                    meta={
                        "playwright": True,
                        "playwright_page_methods": [
                            PageMethod("wait_for_timeout", 3000),
                        ],
                    },
                )

    def parse_detail(self, response):
        nama = response.css("h1.DUwDvf::text").get()
        bintang_dan_total_review = response.css("span.ZkP5Je").attrib.get("aria-label")
        alamat = response.css("div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)::text").get()
        nomor_hp = response.xpath(
                '//span[contains(@class,"google-symbols") and contains(@class,"NhBTye") and contains(@class,"PHazN")]'
                '/ancestor::div[contains(@class,"cXHGnc")]'
                '/following-sibling::div[contains(@class,"rogA2c")][1]'
                '//div[contains(@class,"Io6YTe")]/text()'
            ).get()        
        instagram = response.css("a.CsEnBe").attrib.get("href")

        yield {
            "nama": nama,
            "rating_review": bintang_dan_total_review,
            "alamat": alamat,
            "nomor_hp": nomor_hp,
            "instagram": instagram,
        }