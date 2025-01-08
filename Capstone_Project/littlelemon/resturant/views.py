from .models import Menu
from .models import Booking
from .serializer import BookingSerializer
from .serializer import MenuSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import DestroyAPIView 
from rest_framework import viewsets 

# Create your views here.
class MenuView(ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

