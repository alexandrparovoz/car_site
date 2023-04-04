from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WorldCars
from .serializers import WorldCarsSerializer

class WorldCarsAPIView(APIView):
    def get(self, request):
        cars = WorldCars.objects.all() # получаем объект Queryset  и далее передаем его в сериализатор
        return Response({'post': WorldCarsSerializer(cars, many=True).data})

    def post(self, request):
        serializer = WorldCarsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # проверка на исключения перед передачей JSON клиенту

        post_new = WorldCars.objects.create(   # здесь также объект Queryset должен быть заполнен
            title=request.data['title'],   # данными в представленных полях
            content=request.data['content'],
            country_id=request.data['country_id'],
        )
        return Response({'post': WorldCarsSerializer(post_new).data}) # и передан в сериалазер для обработки





