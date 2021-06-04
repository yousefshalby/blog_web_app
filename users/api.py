from rest_framework.response import Response
from rest_framework import viewsets, status, request, filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


class viewsets_profile(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backend = [filters.SearchFilter]
    search_fields = ['user']
    authentication_classes = [TokenAuthentication]




@api_view(["GET", "PosT"])
def fbv_user_list(request):
    if request.method=="GET":
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(["GET", "PuT", "DELETE"])
def fbv_user_pk(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response (status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif  request.method == "DELETE":
        user.delete()
        return Response (status.HTTP_204_NO_CONTENT)
        
                 