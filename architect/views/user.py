from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from ..serializers.user import UserSerializer

User = get_user_model()

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    # GET - Listar todos los usuarios
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST - Crear nuevo usuario
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT - Actualizar usuario específico (actualización completa)
    def put(self, request, pk=None):
        if pk is None:
            return Response(
                {"error": "Se requiere el ID del usuario"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH - Actualización parcial de usuario
    def patch(self, request, pk=None):
        if pk is None:
            return Response(
                {"error": "Se requiere el ID del usuario"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE - Eliminar usuario
    def delete(self, request, pk=None):
        if pk is None:
            return Response(
                {"error": "Se requiere el ID del usuario"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Eliminación suave si tu modelo tiene deleted_at, sino eliminación física
        if hasattr(user, 'deleted_at'):
            user.soft_delete()  # Si tienes eliminación suave
            message = "Usuario marcado como eliminado"
        else:
            user.delete()  # Eliminación física
            message = "Usuario eliminado permanentemente"
        
        return Response(
            {"message": message}, 
            status=status.HTTP_200_OK
        )