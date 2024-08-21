import scrapy
import json

from scrapy.downloadermiddlewares.retry import RetryMiddleware


class Covid19Spider(scrapy.Spider):
    name = "_covid19"
    allowed_domains = []
    start_urls = []
    cities = [
        "上海市",
        "云南省",
        "内蒙古自治区",
        "北京市",
        "台湾",
        "吉林省",
        "四川省",
        "天津市",
        "宁夏回族自治区",
        "安徽省",
        "山东省",
        "山西省",
        "广东省",
        "广西壮族自治区",
        "新疆维吾尔自治区",
        "江苏省",
        "江西省",
        "河北省",
        "河南省",
        "浙江省",
        "海南省",
        "湖北省",
        "湖南省",
        "澳门",
        "甘肃省",
        "福建省",
        "西藏自治区",
        "贵州省",
        "辽宁省",
        "重庆市",
        "陕西省",
        "青海省",
        "香港",
        "黑龙江省",
    ]
    province_api = "https://lab.isaaclin.cn/nCoV/api/area?province={}"
    overall_api = "https://lab.isaaclin.cn/nCoV/api/overall"
    news_api = "https://lab.isaaclin.cn/nCoV/api/news?num=100&page={}"

    def start_requests(self):
        yield scrapy.Request(
            self.overall_api, meta=dict(type="Overall", max_retry_times=1000)
        )
        for city in self.cities:
            yield scrapy.Request(
                self.province_api.format(city),
                meta=dict(type="Province", max_retry_times=1000),
            )
        for i in range(1, 6):
            yield scrapy.Request(
                self.news_api.format(i), meta=dict(type="News", max_retry_times=1000)
            )

    def parse(self, response):
        type_ = response.meta["type"]
        if type_ == "Province" or type_ == "Overall":
            j = json.loads(response.text)["results"][0]
            j["type"] = type_
            yield j
        elif type_ == "News":
            for i in json.loads(response.text)["results"]:
                i["type"] = type_
                yield i
