from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, CvicenieSerializer, PokusSerializer
from slovicka.models import Cvicenie, Pokus
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from apiapp.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]

# class CvicenieViewSet(viewsets.ModelViewSet):
#     queryset = Cvicenie.objects.all()
#     serializer_class = CvicenieSerializer

class CvicenieView(APIView):
   # authentication_classes = [JWTAuthentication]
   # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        trieda = request.user.groups.all()
        if trieda:
            trieda = trieda[0]
        #print(trieda)
        cvicenia = Cvicenie.objects.filter(trieda=trieda)
        pokusy = [i.cvicenie for i in Pokus.objects.filter(ziak=request.user)]
        hotove = []
        for i in pokusy:
            print('asd')
            print(i)
            print(cvicenia)
            if i in cvicenia:
                hotove.append(i)
        #print(pokusy)
        serializer = CvicenieSerializer(cvicenia,context={'pokusy': pokusy}, many=True)
        return Response(serializer.data)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class PokusView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        # cvicenie = get_object_or_404(Cvicenie, pk=request.data[0]['cvicenie_id'])
        # trieda = cvicenie.trieda
        # if trieda != str(request.user.groups.all()[0]):
        #     return Response('chyba')
        # ziak = request.user
        #print(data)
        print(request.data)
        data = {"ziak":request.user.id,"cvicenie":request.data['cvicenie_id']}
        pokus_serializer = PokusSerializer(data=data)
        if pokus_serializer.is_valid():

            print(pokus_serializer)
            print('dobre')
            pokus_serializer.save()
            return Response(pokus_serializer.data)
        else:
            print(pokus_serializer.errors)
            print('zle')
            print(pokus_serializer)

        return Response(request.data)
