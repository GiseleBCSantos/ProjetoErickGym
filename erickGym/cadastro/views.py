from django.shortcuts import render
from .models import Aluno, Professor
from .serializer import AlunoSerializer, ProfessorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ListCreateAlunoView(ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [permissions.AllowAny]
    
    



    def post(self, request):
        request.data['usuario'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    

class RetrieveUpdateDestroyAlunoView(RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [permissions.IsAuthenticated]


    def put(self, request, pk, *args, **kwargs):
        user = request.user
        aluno = Aluno.objects.get(pk=pk)

        if aluno.usuario != user:
            return Response(
                {'detail': 'Você só pode editar seu próprio perfil'},
                status=400
            )

        return self.update(request, *args, **kwargs)
    
    
    def delete(self, request, pk, *args, **kwargs):
        user = request.user
        aluno = Aluno.objects.get(pk=pk)

        if aluno.usuario != user:
            return Response(
                {'detail': 'Você só pode deletar seu próprio perfil'},
            )
        return self.delete(request, *args, **kwargs)



class ListCreateProfessorAPIView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.AllowAny]
    

    
    
    def post(self, request):
        request.data['usuario'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RetrieveUpdateDestroyProfessorAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        return Professor.objects.filter(usuario=usuario)
    
    
    def put(self, request, pk, *args, **kwargs):
        user = request.user
        professor = Professor.objects.filter(pk=pk)

        if user != professor.usuario:
            return Response(
                {'detail': 'Você só pode modificar seu proprio usuario.'}
            )
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, pk, *args, **kwargs):
        professor = Professor.objects.filter(pk=pk)
        user = request.user

        if professor.usuario != user:
            return Response(
                {'detail': 'Você so pode apagar seu proprio usuario.'}
            )
        return self.delete(request, *args, **kwargs)