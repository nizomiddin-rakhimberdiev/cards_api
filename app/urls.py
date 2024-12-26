from django.urls import path
from .views import CardList, CardDetail


urlpatterns = [
    path('', CardList.as_view(), name="cards"),
    path('<int:pk>/', CardDetail.as_view(), name="card_detail")
]