from django.urls import path
from .views import ListCreateAlunoView, RetrieveUpdateDestroyAlunoView, ListCreateProfessorAPIView, RetrieveUpdateDestroyProfessorAPIView

urlpatterns = [
    path('alunos', ListCreateAlunoView.as_view()),
    path('alunos/<int:pk>', RetrieveUpdateDestroyAlunoView.as_view()),
    path('professores', ListCreateProfessorAPIView.as_view()),
    path('professores/<int:pk>', RetrieveUpdateDestroyProfessorAPIView.as_view())
]
