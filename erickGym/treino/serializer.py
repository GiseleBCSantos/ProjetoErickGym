from .models import Exercicio, Treino, ItemTreino
from rest_framework.serializers import ModelSerializer

class ExercicioSerializer(ModelSerializer):
    class Meta:
        model = Exercicio
        fields = '__all__'
        

class ItemTreinoSerializer(ModelSerializer):
    class Meta: 
        model = ItemTreino
        fields = '__all__'

        
class TreinoSerializer(ModelSerializer):
    class Meta: 
        model = Treino
        fields = '__all__'
        