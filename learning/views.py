from rest_framework import viewsets
from .models import learn
from .serializers import learnSerializer


class learnViewSet(viewsets.ModelViewSet):
    queryset = learn.objects.all()
    serializer_class = learnSerializer
