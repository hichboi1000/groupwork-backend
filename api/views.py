from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import User
from .serializers import UserSerializer


# PUBLIC - Anyone can create an account
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


# PROTECTED - Requires JWT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


# PROTECTED - Requires JWT
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)

    except User.DoesNotExist:
        return Response(
            {'error': 'User not found'},
            status=404
        )

    if request.method == 'GET':

        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = UserSerializer(
            user,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':

        serializer = UserSerializer(
            user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':

        user.delete()

        return Response(
            {'message': 'User deleted successfully'},
            status=204
        )