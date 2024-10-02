from rest_framework import serializers
from .models import Posts
from .models import Technologies

class TechnologieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = ['id', 'name', 'description','start_date','level','url_logo']

class PostSerializer(serializers.ModelSerializer):
    technologies = TechnologieSerializer(many=True, read_only=True)
    class Meta:
        model = Posts
        fields = '__all__' 