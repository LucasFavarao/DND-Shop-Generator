from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/",views.todos,name="Todos"),
    path("itemList/",views.itemList,name="ItemList"),
    path("run-script/",views.run_script,name='run_script')
]