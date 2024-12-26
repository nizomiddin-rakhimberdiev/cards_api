from .serializers import CardSerializers
from .models import Card
from rest_framework import generics

# Create your views here.

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # Faqat kelgan ma'lumotlarni yangilash
        return super().update(request, *args, **kwargs)