import django
import os
from datetime import datetime
import re
import requests
from requests_html import HTMLSession

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid19_analysis_system.settings")

django.setup()

dformat = "%a %b %d %H:%M:%S +%f %Y"
del_quote = re.compile(r"\[.*?\]")


def crawl(uid="2127460165", id_="4773288049639718", max_id=None):
    from covid19.models import Comment

    session = HTMLSession()
    # 'flow=1&is_reload=1&id=4491226084185271&is_show_bulletin=2&is_mix=0&count=20&uid=2656274875'
    url = "https://weibo.com/ajax/statuses/buildComments"
    params = {
        "flow": "1",
        "is_reload": "1",
        "id": id_,
        "is_show_bulletin": "2",
        "is_mix": "0",
        "max_id": max_id,
        "count": "20",
        "uid": uid,
    }
    while True:
        res = session.get(url, params=params)
        result = res.json()
        if not result["data"]:
            break
        # 列表
        for i in result["data"]:
            publish_time = datetime.strptime(i["created_at"], dformat)
            text = del_quote.sub("", i["text_raw"]).replace("！", "").replace("!", "")
            if text:
                try:
                    c = Comment.objects.create(
                        username=i["user"]["name"], text=text, publish_time=publish_time
                    )
                    print(c.username, c.text, c.prob, c.positive)
                except:
                    pass
        params["max_id"] = result["max_id"]


def judge():
    from covid19.models import Comment

    c = Comment.objects.all()
    for i in c:
        i.prob = None
        i.save()
        print(i.prob, i.positive)


if __name__ == "__main__":
    crawl()
