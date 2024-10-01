from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

def sayHello(request):
    return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer
    
    
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
