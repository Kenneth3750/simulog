from rest_framework import serializers
from .models import Containers


class ContainerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    width = serializers.FloatField()
    height = serializers.FloatField()
    length = serializers.FloatField()
    weight = serializers.FloatField()
    volume = serializers.FloatField()


    class Meta:
        model = Containers
        fields = '__all__'

class TotalContainerSerializer(serializers.Serializer):
    number_of_pallets = serializers.IntegerField()
    pallets_per_container = serializers.IntegerField()


class positionContainerSerializer(serializers.Serializer):
    pallet_id = serializers.IntegerField()
    container_id = serializers.IntegerField()
    number_of_pallets = serializers.IntegerField()