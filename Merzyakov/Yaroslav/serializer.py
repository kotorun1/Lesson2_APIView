from rest_framework import serializers
from .models import Products
class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    cost = serializers.IntegerField(min_value=0)
    cat_id = serializers.IntegerField()
    man_id = serializers.IntegerField()

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.man_id = validated_data.get('man_id', instance.man_id)
        instance.save()
        return instance