"""dareapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from homeapp import views
from django.views.generic.base import TemplateView

# handler404 = 'homeapp.views.handler404'
# handler500 = 'homeapp.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dare/', views.index, name="dare"),
    path('createpost/', views.new_joke_form),
    path('', views.index, name="dare"),
    path('dare/<slug:slug>/', views.dare_slug),
    path('jokes/', views.jokes),
    path('quotes/', views.quotes),
    path('jokes/<slug:slug>/', views.jokes_slug),
    path('quotes/<slug:slug>/', views.quotes_slug),
    path('<str:page_type>/<slug:slug>/details', views.get_url_change)
]


# urlpatterns += patterns('',
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.STATIC_ROOT,
#     }),
#  )

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
