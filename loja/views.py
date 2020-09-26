from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response({ "message": "Usuário ou senha incorretos." }, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data['user']

        if user.perfil.tipo_usuario == 1:
            return Response({ "message": "Login do usuário não permitido." }, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        print(user.perfil.tipo_usuario)
        return Response({
            'user': {
                'id': user.id,
                'nome': user.username,
                'tipo_usuario': user.perfil.tipo_usuario
            },
            'token': token.key,
        })