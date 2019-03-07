from django.urls import path
from .views import list_f, add_f,up_f,del_f
urlpatterns = [
    path('', list_f, name='list_f'),
    path('new', add_f, name='add_f'),
    path('update/<int:id>/', up_f, name='up_f'),
    path('delete/<int:id>/', del_f, name='del_f'),
   ]

