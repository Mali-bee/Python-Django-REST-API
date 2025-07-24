#Python Django API project by Malibongwe Makhubo
#where we are gonna be setting the display
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


@api_view(['GET'])                                                      #to pull the information, receive the information
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)                                    #display all the users
    
@api_view(['POST'])                                                     #to post the information, send the information
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])                                     
def user_detail(request, pk):                                           #compiling the different oprations inside one function
    try:                                        
        user = User.objects.get(pk=pk)                                  #pk - primary key... in this case being the id
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':                                         #to pull the information, receive the information
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':                                       #update already existng user information
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':                                     #remove user information
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)