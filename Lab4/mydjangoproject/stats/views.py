from os import path

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.shortcuts import render
import numpy as np

from order.models import Client, Order

import matplotlib.pyplot as plt

from mydjangoproject import settings


# Create your views here.


def stats(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Permission denied")

    pt = dict()

    x = []
    y = []

    for order in Order.objects.all():
        pt[str(order.date.year) + '.' +
           str(order.date.month) + '.' + str(order.date.day)] = 0

    for order in Order.objects.all():
        pt[str(order.date.year) + '.' + str(order.date.month) +
           '.' + str(order.date.day)] += 1

    for tmp in pt:
        x.append(tmp)
        y.append(pt[tmp])

    plt.xlabel('date', fontsize=10)
    plt.ylabel('order amount', fontsize=10)
    plt.plot(x, y)

    if request.method == "GET":
        plt.savefig(path.join(settings.MEDIA_ROOT,
                              'orders_per_day.png'), format='png')
        plt.close()

    context = {}

    amount_orders_per_day = list(pt.values())
    mean_orders_per_day = np.mean(amount_orders_per_day)
    median_orders_per_day = np.median(amount_orders_per_day)
    min_orders_per_day = np.min(amount_orders_per_day)
    max_orders_per_day = np.max(amount_orders_per_day)

    orders_lst = []
    for order in Order.objects.all():
        orders_lst.append({'driver': order.driver, 'transport': order.transport, 'cargo': order.cargo,
                           'client': order.client, 'service': order.service, 'cost': order.cost, 'date': order.date})

    context.update({'mean_orders_per_day': mean_orders_per_day,
                    'median_orders_per_day': median_orders_per_day,
                    'min_orders_per_day': min_orders_per_day,
                    'max_orders_per_day': max_orders_per_day,
                    'orders_list': orders_lst,
                    })
    return render(request, 'stats.html', context)
