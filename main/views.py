from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework.response import Response


from .serializers import SomeModelSerializer
from .models import SomeModel

class SomeModelListView(ListAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer

class SomeModelCreateView(CreateAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer

class SomeModelRetrieveView(RetrieveAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer

class SomeModelUpdateView(UpdateAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer

class SomeModelDeleteView(DestroyAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer

