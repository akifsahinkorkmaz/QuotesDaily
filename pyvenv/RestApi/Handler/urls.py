from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import DailyView, ShareView, SSIMView
urlpatterns = [
  path("", DailyView),
  path("<slug:shareurl>/", ShareView),
  path("ssim/<slug:shareurl>", SSIMView),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)