from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

items = {'Side Dish': {'Onion Pakodi': 9.99, 'Mirchi Bajji': 9.99},
         'Entree': {'Chicken Biriyani': 12.99, 'Lamb Biriyani': 14.99}
         }

"""
def items_list(requests):
    return HttpResponse("This works!")

def user_name(requests):
    return HttpResponse("User Found")
"""

def task_desc(requests, task):
    if task == "items":
        text = f"Side Dishes:{' '*20}Price\n\n" \
               "\tOnion Pakodi ---------> $9.99\n" \
               "\tMirchi Bajji ---------> $9.99\n" \
               "Entree:\n" \
               "\tChicken Biriyani -----> $12.99\n" \
               "\tLamb Biriyani    -----> $14.99\n"
    elif task == 'user_name':
        text = "Hello Veera"
    else:
        return HttpResponseNotFound
    return HttpResponse(text, content_type="text/plain")
