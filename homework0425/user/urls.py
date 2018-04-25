from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'adduser', views.adduser),
    url(r'search', views.search)
]