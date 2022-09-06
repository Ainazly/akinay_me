from django.urls import path
from .views import main_page, view_menu

urlpatterns = [
    path('', main_page),
    path('reciepts/', view_menu)

]
