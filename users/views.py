from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User


@api_view(['POST'])
def user_login(request):
    data = request.data
    email = data.get('email').strip()
    password = data.get('password')

    user = User.objects.filter(email=email, password=password)

    if user.exists():
        user = user.first()
        login(request, user)
        return Response({
            'is_authenticated': user.is_authenticated
        })
    else:
        return Response({'description': 'email or password is invalid'})



# @api_view(['GET'])
# def get_all_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)
