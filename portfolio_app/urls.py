from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import TechnologieViewSet, PostViewSet, PostDetailView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'technologies', TechnologieViewSet)
router.register(r'posts', PostViewSet)  # Lista di post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Include rotte automatiche per post e tecnologie
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),  # Rotta per i dettagli del post
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
