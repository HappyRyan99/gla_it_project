from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # 你的数据源
    url_list = [['/rango/about/', 'About'], ['/rango/', 'Index'], ['/rango/images', 'Image']]

    # 1. 初始化空字符串
    url_html = ''

    # 2. 循环拼接 HTML (使用 +=)
    for page_url in url_list:
        # 注意：这里用 += 把新生成的链接追加到 url_html 后面
        # page_url[0] 是链接，page_url[1] 是文字
        url_html += '<a href="%s">%s</a><br/>' % (page_url[0], page_url[1])

    # 3. 拼接静态链接和动态链接
    # 前面是 Bilibili，后面加上刚才循环生成的 url_html
    response_string = '<a href="https://www.bilibili.com">Bilibili</a><br/>' + url_html
    return HttpResponse(response_string)

def page_not_found(request):
    try:
        return HttpResponse("xzxxx")
    except:
        return HttpResponse(404)
