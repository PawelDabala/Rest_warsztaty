from .models import Person, Movie
from rest_framework import serializers

#
# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'
#
# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    role = 
    class Meta:
        model = Person
        fields = ("name", "rola")


class MovieSerializer(serializers.ModelSerializer):
    actors = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director", "actors", "year")