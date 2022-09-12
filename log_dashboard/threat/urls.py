from django.urls import path
from .views import show_threat_categories, show_threats

urlpatterns = [
    path('threat_category/', show_threat_categories,
         name='show_threat_categories'),
    path('', show_threats, name='threats'),
]
