from django.shortcuts import render
from django.http import HttpResponse


# Create your views here
def page_view(request, page):
    html = '这是编号为%s的网页' % (page)
    return HttpResponse(html)


# 这是显示相加的网页函数
def cal_view(request, x, op, y):
    if op not in ['add', 'sub', 'mul']:  # 元组类型
        return HttpResponse('your op is wrong')
    result = 0
    if op == 'add':
        result = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y

    return HttpResponse('结果为:%s' % (result))

def cal_view2(request, x, op, y):
    print(x+op+y)

    return cal_view(request, int(x), op, int(y))