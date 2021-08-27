from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate, BlogChallenge, BlogSeikai, Hantei#viewで定義されるclass

urlpatterns = [
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', BlogDelete.as_view(), name='delete'),
    path('update/<int:pk>', BlogUpdate.as_view(), name='update'),
    path('challenge/<int:pk>', BlogChallenge.as_view(), name='challenge'),
    path('hantei/<int:pk>', Hantei, name='hantei'),
    path('seikai/<int:pk>', BlogSeikai.as_view(), name='seikai'),

]