from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from django.http import Http404
# Create your views here.


# def index(request):
#     return HttpResponse("Привет, это сайт рецептов ")


def test_view(request):
    print(request)
    my_object = Menu.objects.all()
    print(my_object)
    context = {
        'my_object': my_object
    }
    return render(request, 'reciepts/test.html', context=context)


def post_detail(request, id=None):
    reciepts_object = None
    if id is not None:
        try:
            reciepts_object = Menu.objects.get(id=id)
        except:
            raise Http404
    context = {
        "reciepts_object": reciepts_object
    }
    return render(request, 'reciepts/post_detail.html', context=context)
