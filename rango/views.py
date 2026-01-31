from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)


def index_backup(request):
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
    return HttpResponse(404)


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
        # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)
