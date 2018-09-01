# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models import DoubleBallAll, DoubleBall
import datetime
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage
import requests
from django.db import connection, transaction
from manage import *
import os
# Create your views here.

def index(request):
    context = {}
    print "-----------"
    try:
        response = requests.get('http://datachart.500.com/ssq/history/history.shtml')
        if len(response.text.split('<tbody id="tdata">')) > 1:
            text = response.text.split('<tbody id="tdata">')[1]
            if len(text.split("</tbody>")) > 1:
                text = text.split("</tbody>")[0]
                if len(text.split('<tr class="t_tr1"><!--<td>2</td>--><td>')) > 1:
                    x = 0
                    for text in text.split('<tr class="t_tr1"><!--<td>2</td>--><td>'):
                        # print "text_%s = %s" % (x, text)
                        x += 1
                        if len(text.split('</td><td class="t_cfont2">')) == 7:
                            qici = text.split('</td><td class="t_cfont2">')[0]
                            red1 = text.split('</td><td class="t_cfont2">')[1]
                            red2 = text.split('</td><td class="t_cfont2">')[2]
                            red3 = text.split('</td><td class="t_cfont2">')[3]
                            red4 = text.split('</td><td class="t_cfont2">')[4]
                            red5 = text.split('</td><td class="t_cfont2">')[5]
                            red6 = text.split('</td><td class="t_cfont2">')[6].split('</td><td class="t_cfont4">')[0]
                            blue = text.split('</td><td class="t_cfont2">')[6].split('</td><td class="t_cfont4">')[1]
                            date = text.split('</td><td class="t_cfont2">')[6].split('</td><td class="t_cfont4">')[2].split('</td><td>')[-1].split('</td></tr>')[0]
                            # print "qici=%s, red1=%s, red2=%s, red3=%s, red4=%s, red5=%s, red6=%s, blue=%s, date=%s" % (qici, red1, red2, red3, red4, red5, red6, blue, date)
                            if DoubleBall.objects.filter(qici=qici).count() < 1:
                                doubleball = DoubleBall()
                                doubleball.qici = qici
                                doubleball.red1 = red1
                                doubleball.red2 = red2
                                doubleball.red3 = red3
                                doubleball.red4 = red4
                                doubleball.red5 = red5
                                doubleball.red6 = red6
                                doubleball.blue=blue
                                doubleball.date=date
                                doubleball.save()
    except BaseException:
        print "Error: 没有网络"
    info = "Hello World"
    context["info"] = info
    return render(request,"base/dashboard.html", context)

def history_datas(request):
    context = {}
    doubleballs = DoubleBall.objects.order_by("-date")
    total = doubleballs.count()
    page = request.GET.get("page")
    if not page or page < 1:
        page = 1
    paginator = Paginator(doubleballs,10)
    try:
        # 尝试获取请求的页数的 产品信息
        doubleballs = paginator.page(int(page))
    #请求页数错误
    except PageNotAnInteger:
        doubleballs = paginator.page(1)
    except EmptyPage:
        doubleballs = paginator.page(paginator.num_pages)
    context["page"] = int(page)
    context["num_pages"] = int(paginator.num_pages)
    context["doubleballs"] = doubleballs
    context["total"] = total
    return render(request,"html/history_datas.html", context)

# 已开奖过的历史数据
def old_datas(request):
    context = {}
    page = request.GET.get("page")
    red = (request.GET.get("red"))
    blue = request.GET.get("blue")
    if not red:
        red = 6
    else:
        red = int(red)
    if not blue:
        blue = 1
    else:
        blue = int(blue)
    if not page or page < 1:
        page = 1
    ids = []
    param = []
    sql = ""
    if red == 6 and blue == 1:
        sql = "select db.id from doubleball db, (select * from doubleball) d where db.blue = d.blue and db.id != d.id and db.red1 = d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 = d.red6;"
    elif red == 6 and blue == 0:
        sql = "select db.id from doubleball db, (select * from doubleball) d where db.blue != d.blue and db.id != d.id and db.red1 = d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 = d.red6;"
    elif red == 5 and blue == 1:
        sql = "select db.id from doubleball db, (select * from doubleball) d where db.blue = d.blue and db.id != d.id and ((db.red1 != d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 != d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 = d.red2 and db.red3 != d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 != d.red4 and db.red5 = d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 != d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 != d.red6));"
    elif red == 5 and blue == 0:
        sql = "select db.id from doubleball db, (select * from doubleball) d where db.blue != d.blue and db.id != d.id and ((db.red1 != d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 != d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 = d.red2 and db.red3 != d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 != d.red4 and db.red5 = d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 != d.red5 and db.red6 = d.red6) or (db.red1 = d.red1 and db.red2 = d.red2 and db.red3 = d.red3 and db.red4 = d.red4 and db.red5 = d.red5 and db.red6 != d.red6));"
    if sql != "":
        result = query_sql(sql, param)
        ids = trupe_to_list(result)
        doubleballs = DoubleBall.objects.filter(id__in=ids).order_by("-date")
        total = doubleballs.count()
        paginator = Paginator(doubleballs,10)
        try:
            # 尝试获取请求的页数的 产品信息
            doubleballs = paginator.page(int(page))
            context["num_pages"] = int(paginator.num_pages)
            context["doubleballs"] = doubleballs
            context["total"] = total
        #请求页数错误
        except PageNotAnInteger:
            doubleballs = paginator.page(1)
        except EmptyPage:
            doubleballs = paginator.page(paginator.num_pages)
    context["page"] = page
    context["red"] = red
    context["blue"] = blue
    return render(request,"html/old_datas.html", context)

def init_datas(request):
    context = {}
    count = DoubleBallAll.objects.count()
    info = "数据库已有数据%s条" % count
    if count < 17721088:
        begin_time = datetime.datetime.now()
        info = "新插入数据"
        sql = "insert into doubleball_all (red1, red2, red3, red4, red5, red6, blue, status) values "
        i = 0
        for a in range(1, 29):
            for b in range(a+1, 30):
                for c in range(b+1, 31):
                    for d in range(c+1, 32):
                        for e in range(d+1, 33):
                            for f in range(e+1, 34):
                                for g in range(1, 17):
                                    sql += "(%s, %s, %s, %s, %s, %s, %s, 1)" % (a, b, c, d, e, f, g)
                                    i += 1
                                    if i % 10000 == 0 or i == 17721088:
                                        sql +=  ";"
                                        cursor = connection.cursor()
                                        cursor.execute(sql)
                                        cursor.close()
                                        transaction.commit()
                                        print "插入%s条数据， %s, 用时: %s" % (i, datetime.datetime.now(), datetime.datetime.now() - begin_time)
                                        sql = "insert into doubleball_all (red1, red2, red3, red4, red5, red6, blue, status) values "
                                    else:
                                        sql += ", "
        print "i = %s, 用时: %s" % (i, datetime.datetime.now() - begin_time)
    context["info"] = info
    return render(request,"html/init_datas.html", context)

def import_history_datas(request):
    context = {}
    count = DoubleBall.objects.count()
    info = "数据库已有数据%s条" % count
    if count < 1:
        import xlrd
        sql = "insert into doubleball (qici, red1, red2, red3, red4, red5, red6, blue, date) values "
        info = "ssd"
        workbook = xlrd.open_workbook(u'static/ssq.xlsx')
        worksheet1 = workbook.sheet_by_index(0)
        num_rows = worksheet1.nrows
        for curr_row in range(num_rows):
            row = worksheet1.row_values(curr_row)
            qici = int(row[0])
            red1 = int(row[1])
            red2 = int(row[2])
            red3 = int(row[3])
            red4 = int(row[4])
            red5 = int(row[5])
            red6 = int(row[6])
            blue = int(row[7])
            date = row[15]
            sql += "(%s, %s, %s, %s, %s, %s, %s, %s, '%s'), " % (qici, red1, red2, red3, red4, red5, red6, blue, date)
        sql = sql[0: len(sql) - 2] + ";"
        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.close()
        transaction.commit()
    context["info"] = info
    return render(request,"html/import_history_datas.html", context)

def xiangqi(request):
    context = {}
    # 第一步：（以只读模式）打开文件
    f = open('/home/zhangjianwei/workplace/ssq/static/media/upload/test.svg', 'r')
    # f = open('/home/zhangjianwei/workplace/ssq/static/media/upload/xiangqiqipan.svg', 'r')

    # 第二步：读取文件内容
    xiangqiqipan = f.read().decode('utf-8')

    # 第三步：关闭文件
    f.close()
    context["xiangqiqipan"] = xiangqiqipan
    return render(request,"html/xiangqi/xiangqi.html", context)

def upload(request):
    context = {}
    if request.method == 'POST':
        content =request.FILES.get("upload", None)
        if not content:
            return HttpResponse("没有上传内容")
        position = os.path.join('/home/zhangjianwei/workplace/ssq/static/media/upload',content.name)
        #获取上传文件的文件名，并将其存储到指定位置

        storage = open(position,'wb+')       #打开存储文件
        for chunk in content.chunks():       #分块写入文件
            storage.write(chunk)
        storage.close()                      #写入完成后关闭文件
        return HttpResponseRedirect("/xiangqi/")      #返回客户端信息
    else:
        return HttpResponseRedirect("不支持的请求方法")
