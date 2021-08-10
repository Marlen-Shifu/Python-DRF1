from django.urls import path
from .views import *

urlpatterns = [
    path('somemodel/', SomeModelListView.as_view()),
    path('somemodel/<int:pk>/', SomeModelRetrieveView.as_view()),
    path('somemodel/create/', SomeModelCreateView.as_view()),
    path('somemodel/update/<int:pk>/', SomeModelUpdateView.as_view()),
    path('somemodel/delete/<int:pk>/', SomeModelDeleteView.as_view()),
]
