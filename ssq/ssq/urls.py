"""ssq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myssq import views as myssq_views

urlpatterns = [
    url(r'', myssq_views.history_datas, name="history_datas"),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', myssq_views.index, name="index"),
    url(r'^init_datas/', myssq_views.init_datas, name="init_datas"),
    url(r'^xiangqi/', myssq_views.xiangqi, name="xiangqi"),
    url(r'^upload/', myssq_views.upload, name="upload"),
    url(r'^import_history_datas/', myssq_views.import_history_datas, name="import_history_datas"),
    # url(r'^history_datas/', myssq_views.history_datas, name="history_datas"),
    url(r'^old_datas/', myssq_views.old_datas, name="old_datas"),
]
