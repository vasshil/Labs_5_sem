from uuid import uuid4

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Token, Good
from .serializers import TokenSerializer, GoodSerializer


@api_view(['GET'])
def get_token(request):
    token_value = str(uuid4())
    token = Token.objects.create(value=token_value)
    serializer = TokenSerializer(token)
    return Response({'token': token.value})

@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def goods(request):
    goods = Good.objects.all()
    serializer = GoodSerializer(goods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def new_good(request):
    token = Token.objects.get(value=request.GET.get('token'))
    if not token:
        return Response({'detail': 'Token is invalid'}, status=401)

    name = request.GET.get('name', '')
    amount = request.GET.get('amount', '')
    price = request.GET.get('price', '')

    if name and amount and price:
        # Сохранение данных в базу данных
        new_good = Good.objects.create(name=name, amount=amount, price=price)
        serializer = GoodSerializer(new_good)
        return Response(serializer.data, status=201)
    else:
        return Response({"message": "All fields are required"}, status=400)
