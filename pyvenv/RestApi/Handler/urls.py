from django.urls import path, re_path
from .views import DailyView
urlpatterns = [
  path("", DailyView)
]