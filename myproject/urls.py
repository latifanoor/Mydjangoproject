"""myproject URL Configuration

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
from django.contrib import admin
from django.urls import path
from pygirls import views as pygirls_views
from swahilipot import views as swahilipot_views
from members import views as members_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pygirls/',pygirls_views.pygirls, name='pygirls'),
    path('swahilipot/',swahilipot_views.swahilipot, name='swahilipot'),
    path('boards/',swahilipot_views.home, name='home'),
    path('members/',members_views.members,name='members'),
]

