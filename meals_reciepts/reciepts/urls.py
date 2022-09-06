from django.urls import path
from .views import test_view, post_detail


urlpatterns = [
    path('', test_view),
    path('reciepts/<int:id>/', post_detail),
]
