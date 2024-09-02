from rest_framework import serializers
from .models import Premises, Tag, TagGroup


class TagGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagGroup
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    group = TagGroupSerializer()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'description', 'icon', 'group']


class PremisesSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Premises
        fields = ['id', 'name', 'address', 'area', 'description', 'price',
                  'availability_start_date', 'availability_end_date', 'tags']
