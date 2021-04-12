"""Projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

# importando views da aplicação core
from core.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')) # -> Se a url for na raiz (http://localhost:8000/) vai utilizar as urlpatterns no arquivo urls.py do core
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
