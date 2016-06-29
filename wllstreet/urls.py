"""wllstreet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
#from portfolio import views_portfolio
from login import views
from sellbuy import views_sellbuy
from portfolio import views_portfolio
urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.logout_page, name = 'logout_page'),
    url(r'^transact/$',views_sellbuy.sellbuyhome, name = 'transact'),
    url(r'^home', views.home, name = 'home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^register/', views.register, name = 'register'),
    url(r'^success/$', views.registersuccess, name = 'registersuccess'),
    url(r'^current_price/$',views_sellbuy.current_priceAjax, name = 'current_price'),
    url(r'^timer_update/$',views_sellbuy.timer_update, name = 'timer_update'),
    url(r'^current_news/$',views_sellbuy.current_news, name = 'current_news'),
    url(r'^current_queries/$',views_sellbuy.current_queries, name = 'current_queries'), 
    url(r'^share_graph/(?P<name>\w+)/$',views_portfolio.graph, name = 'graph'), 
    url(r'^dynamic/$',views_portfolio.dynamic, name = 'dynamic'), 
    ]