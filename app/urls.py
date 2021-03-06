"""app URL Configuration

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
from django.conf.urls import url,include
# from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework import routers
# from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
# from users.views import UserProfileListViewset
from users.views  import VerifyCodeViewset,UserViewset
from details.views import DetailListViewset

router = routers.DefaultRouter()
router.register(r'codes', VerifyCodeViewset,base_name='codes')
router.register(r'users', UserViewset,base_name='users')
router.register(r'details', DetailListViewset)


import xadmin


urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^',include(router.urls)),
    url(r'docs/',include_docs_urls(title="在线管理系统")),
    url(r'^api-token-auth/', obtain_jwt_token),
]
