from django.http import Http404
from django.shortcuts import render

from main.models import Car
from main import models


def cars_list_view(request):
    template_name = 'main/list.html'
    car = models.Car.objects.all()
    print(car)

    context = {
        "cars": car
    }

    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    try: # получите авто, если же его нет, выбросьте ошибку 404
        template_name = 'main/details.html'
        car = models.Car.objects.filter(id=car_id)
        info = car.get(id=car_id)
        print(info.id)

        context = {
            "car": info
        }

        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        template_name = 'main/sales.html'
        car = models.Car.objects.filter(id=car_id)
        info_car = car.get(id=car_id)
        print(info_car)
        sale = models.Sale.objects.filter(car_id=car_id)
        info_sale = sale.all()
        print(info_sale)

        context = {
            "car": info_car,
            "sales": info_sale
        }
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
