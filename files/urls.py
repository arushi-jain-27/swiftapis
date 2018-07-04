"""swift URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include
app_name='files'

urlpatterns = [


    path('info/<account>', views.container_list, name="acc_info"),
    path('info/<account>/<container>', views.object_list, name="cont_info"),
    path('info/<account>/<container>/metadata', views.metadata, name="metadata"),
    path('info/<account>/<container>/upload', views.upload, name="upload"),
    path('info/<account>/<container>/<object>', views.object_details, name="obj_info"),
    path('info/<account>/<container>/<object>/download', views.download_object, name="obj_download")

]
