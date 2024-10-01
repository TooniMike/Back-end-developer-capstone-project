#define URL route for index() view
from django.urls import path
from . import views
from .views import sayHello 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ 
    # . . . ,
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    # path('booking/', views.BookingViewSet.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]
