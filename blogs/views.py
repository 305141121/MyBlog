from django.http import HttpResponse, HttpRequest, HttpResponseNotAllowed
from django.template import loader
from django.conf import settings
import json
import os
import math
import markdown

def index(request):
    # print(os.path.join(settings.BASE_DIR, "static"))
    # 扫描静态目录中的博文
    path = os.path.join(settings.BASE_DIR, "static/posts")
    posts = []
    for fileName in os.listdir(path):
        if fileName.endswith(".md"):
            posts.append(str.split(fileName,".")[0])
    # 将博文分割成页数
    print(int(len(posts)/10))
    count = range(1, int(len(posts)/10)+2)
    ctx = {
        'posts': posts[:10],
        'count': count
    }

    # 将博文渲染至目录模板
    template = loader.get_template("blogs/index.html")
    return HttpResponse(template.render(ctx, request))

# 修改文章请求
def submit(request):
    js = json.loads(request.body.decode('utf-8'))
    name = js["name"]
    content = js["content"]
    passwd = js["passwd"]
    if passwd != "******":
        return HttpResponseNotAllowed()
    path = os.path.join(settings.BASE_DIR, "static/posts")
    with open(path+"/"+name+".md","w",encoding="utf-8") as f:
        f.write(content)
        # 重新生成markdown对应页面
        html = markdown.markdown(content)
        with open(path + "/" + name + ".html", "w", encoding="utf-8") as h:
            h.write(html)
    return HttpResponse("ok")

def pageItem(request):
    js = json.loads(request.body.decode('utf-8'))
    print(request.body)
    page = int(js["page"])
    print("cur page:",page)
    curPage = []
    path = os.path.join(settings.BASE_DIR, "static/posts")
    posts = []
    for fileName in os.listdir(path):
        if fileName.endswith(".md"):
            posts.append(str.split(fileName,".")[0])

    if page > int(len(posts)/10)+2:
        return HttpResponse()
    else:
        for p in posts[(page-1)*10:page*10]:
            curPage.append(
                {
                    "name": p
                }
            )
        return HttpResponse(json.dumps(curPage))

