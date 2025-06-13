from rest_framework.permissions import BasePermission  # Importe BasePermission

class IsAluno(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            hasattr(request.user, 'custom_id') and #verifica se esta autenticado e se possui o simbolo
            request.user.identificador.startswith('_')
        )

class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            hasattr(request.user, 'custom_id') and 
            request.user.identificador.startswith('#')
        )

class IsEscola(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            hasattr(request.user, 'custom_id') and 
            request.user.identificador.startswith('@')
        )

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and 
            hasattr(request.user, 'custom_id') and 
            request.user.identificador.startswith('<admin>')
        )


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "tipo": user.tipo,
                "id": user.identificador
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)