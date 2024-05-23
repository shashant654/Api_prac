# from django.urls import path,include
# from . import views
# from .views import ItemListCreate


# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'api/items/',views.ItemListCreate,basename='item-list-create')

# urlpatterns = [
# # path('home/',views.homee,name='home'),
# # path('content/',views.contentt,name='content'),
# # path('api/items/', ItemListCreate.as_view(), name='item-list-create'),
# path('z/',include(router.urls))
# ]

from django.urls import path
from .views import ItemListCreate,item_list

urlpatterns = [
    path('api/items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/', item_list, name='item-list'),
]




