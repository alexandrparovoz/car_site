import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import WorldCars

class WorldCarsModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class WorldCarsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)
    is_public = serializers.BooleanField(default=True)
    country_id = serializers.IntegerField()


# def encore():
#     model = WorldCarsModel('hfbebyebcu', "Content: ffufnkun")
#     model_str = WorldCarsSerializer(model)
#     print(model_str.data, type(model_str.data))
#     json = JSONRenderer().render(model_str.data)
#     print(json, type(json))
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WorldCarsSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
