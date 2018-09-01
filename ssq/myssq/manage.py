# -*- coding: utf-8 -*-
from models import DoubleBallAll, DoubleBall
from django.db import connection, transaction
def query_sql(sql, param):
    cursor = connection.cursor()
    cursor.execute(sql, param)
    result = cursor.fetchall()
    cursor.close()
    transaction.commit()
    return result

def trupe_to_list(trupe):
    list = []
    for t in trupe:
        list.append(t[0])
    return list
