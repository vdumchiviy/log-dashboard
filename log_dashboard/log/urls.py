from django.urls import path
from .views import show_all_logs

urlpatterns = [
    path("", show_all_logs, name="show_all_logs"),
]
