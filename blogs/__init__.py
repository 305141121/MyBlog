import markdown
from django.conf import settings
import os


# 在导入包时将所有markdown预先转为html

postPath = os.path.join(settings.BASE_DIR, "static/posts/")
htmlPath = os.path.join(settings.BASE_DIR, "static/posts-HTML/")
aboutPath = os.path.join(settings.BASE_DIR, "static/")

def md2Html(path, fileName):
    with open(path+fileName, 'r', encoding="utf-8") as f:
        with open(path+fileName.split(".")[0]+".html", "w", encoding="utf-8") as h:
            h.write(markdown.markdown(f.read()))


for fileName in os.listdir(postPath):
    if fileName.endswith(".md"):
        md2Html(postPath, fileName)
md2Html(aboutPath, "about.md")







