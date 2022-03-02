from django.urls import path, re_path
from .views import DailyView, ShareView, SSIMView
urlpatterns = [
  path("", DailyView),
  path("<slug:shareurl>/", ShareView),
  path("ssim/<slug:shareurl>", SSIMView),
]