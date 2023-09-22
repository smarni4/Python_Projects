from django.urls import path
from . import views

urlpatterns = [
    # path("items", views.items_list),
    # path("user_name", views.user_name)
    path("<task>", views.task_desc)

    # path("side dish", views.items_list.side_dish),
    # path("entree", views.items_list.entree)
]


