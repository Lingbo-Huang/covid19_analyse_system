import scrapy
import json
import re


class Covid19Spider(scrapy.Spider):
    name = "covid19"
    allowed_domains = []
    start_urls = []

    api = "http://sa.sogou.com/new-weball/page/sgs/epidemic"

    def start_requests(self):
        yield scrapy.Request(self.api)

    def parse(self, response):
        json_data = re.search(
            r"window.__INITIAL_STATE__ = (.*?)</script>", response.text
        )
        json_data = json_data.group(1)
        data = json.loads(json_data)["data"]

        # 总览数据
        d = data["domesticStats"]
        overall = dict(type="Overall")
        overall["confirmedCount"] = d["diagnosed"]
        overall["confirmedIncr"] = d["yesterdayIncreased"]["diagnosed"]
        overall["suspectedCount"] = d["suspect"]
        overall["suspectedIncr"] = d["yesterdayIncreased"]["suspect"]
        overall["deadCount"] = d["death"]
        overall["deadIncr"] = d["yesterdayIncreased"]["death"]
        overall["curedCount"] = d["cured"]
        overall["curedIncr"] = d["yesterdayIncreased"]["cured"]
        overall["updateTime"] = d["timestamp"]
        yield overall

        # 新闻数据
        n = data["timeline"]["list"]
        for i in n:
            news = dict(type="News")
            news["title"] = i["title"]
            news["summary"] = i["content"]
            news["infoSource"] = i["source"]
            news["sourceUrl"] = i["url"]
            news["pubDate"] = i["timestamp"]
            news["province"] = None
            news["provinceId"] = None
            yield news

        # 省份及城市数据
        a = data["area"]
        for i in a:
            i['type'] = "Province"
            yield i