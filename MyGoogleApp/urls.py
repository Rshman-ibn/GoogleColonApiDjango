from django.urls import path
from .views import Index, Search
urlpatterns = [
    path('', Index, name='home'),
    path('search', Search, name='search'),
]
