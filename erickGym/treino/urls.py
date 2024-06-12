from django.urls import path, include
from .views import ListCreateExercicioView, RetrieveUpdateDestroyExercicioView, ItemTreinoViewSet, TreinoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'treinos', TreinoViewSet, basename='treinos')
router.register(r'itens_treinos', ItemTreinoViewSet, basename='itens_treino')



urlpatterns = [
     path('exercicios', ListCreateExercicioView.as_view()),
     path('exercicios/<int:pk>', RetrieveUpdateDestroyExercicioView.as_view()),
     path('', include(router.urls))
]
