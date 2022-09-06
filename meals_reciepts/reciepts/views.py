from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from django.http import Http404
<<<<<<< HEAD
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
=======
import random
# Create your views here.


def main_page(request):
    return HttpResponse('Привет, это сайт рецептов')


def view_menu(request):
    print(request)

    my_object = Menu.objects.all()
    context = {
        "objects": my_object
    }
    return render(request, 'new-page/.html', context=context)




>>>>>>> ba9553800850bfa704acd9aa976b85cb2996cb54
