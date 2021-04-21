from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# importando views da aplicação core
from core.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('itens/', include('itens.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Critic Hub'
admin.site.site_header = 'Admin Critic Hub'
admin.site.index_title = 'Administração Critic Hub'
