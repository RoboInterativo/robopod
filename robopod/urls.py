from django.conf.urls import url, include
from django.urls import path, re_path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('pods.urls')),

]

