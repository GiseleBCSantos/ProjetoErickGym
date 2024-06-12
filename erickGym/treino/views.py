from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Exercicio, Treino, ItemTreino
from .serializer import ExercicioSerializer, ItemTreinoSerializer, TreinoSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ListCreateExercicioView(ListCreateAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    

class RetrieveUpdateDestroyExercicioView(RetrieveUpdateDestroyAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    
    
class ItemTreinoViewSet(ModelViewSet):
    queryset = ItemTreino.objects.all()
    serializer_class = ItemTreinoSerializer
    
class TreinoViewSet(ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer