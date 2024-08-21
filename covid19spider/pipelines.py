# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import django
import os
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid19_analysis_system.settings")

django.setup()


def load_data(result, fields):
    return {k: v for k, v in result.items() if k in fields}


def get_fields(model_cls):
    return [i.name for i in model_cls._meta.fields if i.name != "id"]


class covid19spiderPipeline:
    def process_item(self, item, spider):
        if spider.__class__.__name__ == "Covid19Spider":
            from covid19.models import Province, City, Overall, News

            type_ = item["type"]
            del item["type"]
            if type_ == "Province":
                fields = get_fields(Province)
                item["provinceEnglishName"] = " "
                item["updateTime"] = int(time.time() * 1000)
                values = load_data(item, fields)
                ut = values["updateTime"]
                obj, created = Province.objects.update_or_create(
                    updateTime=ut, provinceName=item["provinceName"], defaults=values
                )
                if created:
                    spider.log(f"更新-{obj.provinceName}")
                    for c in item["cities"]:
                        f = get_fields(City)
                        c["highDangerCount"] = -1
                        c["midDangerCount"] = -1
                        v = load_data(c, f)
                        v["location"] = obj
                        v["updateTime"] = obj.updateTime
                        v["deadCount"] = (
                            0 if isinstance(v["deadCount"], str) else v["deadCount"]
                        )
                        spider.log(f"\t{v['cityName']}")
                        City.objects.update_or_create(
                            updateTime=v["updateTime"],
                            cityName=v["cityName"],
                            defaults=v,
                        )
                else:
                    spider.log(f"{obj.provinceName} 已是最新数据")
            elif type_ == "Overall":
                fields = get_fields(Overall)
                values = load_data(item, fields)
                ut = values["updateTime"]
                obj, created = Overall.objects.update_or_create(
                    updateTime=ut, defaults=values
                )
                if created:
                    spider.log("更新总览统计数据成功")
            elif type_ == "News":
                _, created = News.objects.update_or_create(
                    title=item["title"], pubDate=item["pubDate"], defaults=item
                )
                if created:
                    spider.log(f'新闻更新: {item["title"]}')
            return None
