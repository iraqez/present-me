"""oscartest URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from oscar.app import application
from oscarapi.app import application as api

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^api_test/', include(api.urls)),
    url(r'', include(application.urls)),

    # Social auth
    url('', include('social.apps.django_app.urls', namespace='social')),

    # #social-auth
    # url(r'^app/', include('social.apps.django_app.urls', namespace='social')),
    # url(r'^app/oauth2login$', 'my.social.oauth2login_view'),  # наша вьюха после авторизации
]
