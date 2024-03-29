from django.shortcuts import render

from auto_app.forms import AutoForm
from auto_app.models import Auto


def get_main_page(request):
    autos = Auto.objects.filter(status__in=['2', '3'])
    return render(request, 'main.html', context={'all_autos': autos})


def create_user(request):
    if request.method == 'GET':
        return render(request, 'create_user.html')


def create_car(request):
    if request.method == 'GET':
        auto_form = AutoForm()
        return render(request, 'create_car.html', context={'form': auto_form})

    elif request.method == 'POST':
        auto_form = AutoForm(request.POST)
        error = None

        if auto_form.is_valid():
            auto_form.save()
        else:
            error = auto_form.errors

        return render(request, 'create_car.html', context={'success_message': 'Success!', 'error': error})


def book_or_take(request):
    if request.method == 'GET':
        return render(request, 'book_or_take.html')