"""Ankara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from AnkaraClothing import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', views.products, name="home"),
    path('search/', views.search, name="search"),
    path('smartphones/', views.search_smartphone, name="search_smartphones"),
    path('earphone/<slug>/', views.EarphonesDetailView.as_view(), name="earphone"),
    path('smartphone/<slug>/', views.SmartphoneDetailView.as_view(), name='smartphone'),
    path('offer/<slug>/', views.OfferDetailView.as_view(), name='offer'),
    path('phone cover/<slug>/', views.CoverDetailView.as_view(), name='cover'),
    path('charger/<slug>/', views.ChargerDetailView.as_view(), name='charger'),
    path('bestseller/<slug>/', views.BestsellerDetailView.as_view(), name='bestseller'),
    path('bt speaker/<slug>/', views.Bt_speakerDetailView.as_view(), name='bt_speaker'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

handler404 = 'AnkaraClothing.views.page_not_found'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)