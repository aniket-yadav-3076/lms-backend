from rest_framework import serializers
from .models import learn

class learnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =learn
        fields = '__all__'