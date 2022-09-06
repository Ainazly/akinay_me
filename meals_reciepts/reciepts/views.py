from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from django.http import Http404
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




