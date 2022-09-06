from django.urls import path
<<<<<<< HEAD
from .views import test_view, post_detail


urlpatterns = [
    path('', test_view),
    path('reciepts/<int:id>/', post_detail),
=======
from .views import main_page, view_menu

urlpatterns = [
    path('', main_page),
    path('reciepts/', view_menu)

>>>>>>> ba9553800850bfa704acd9aa976b85cb2996cb54
]
