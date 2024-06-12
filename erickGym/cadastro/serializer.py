from rest_framework.serializers import ModelSerializer
from .models import Aluno, Professor

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        
        
class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'nome', 'cpf', 'usuario']