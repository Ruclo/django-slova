from django.contrib.auth.models import User, Group
from rest_framework import serializers
from slovicka.models import Cvicenie, Slovicko, Pokus, Odpoved
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SlovickoSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slovicko
        fields = ['jazyk1', 'jazyk2']


class CvicenieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazov = serializers.CharField(max_length=50)
    datum = serializers.DateTimeField()
    trieda = serializers.CharField(max_length=100)
    typ = serializers.CharField(max_length=100)
    hotove = serializers.SerializerMethodField()
    slovicko_set = SlovickoSetSerializer(many=True)

    def get_hotove(self, cvicenie):
        pokusy = self.context.get('pokusy')
        if cvicenie in pokusy:
            return True
        return False

    class Meta:
        fields = ['id', 'nazov', 'datum', 'trieda','typ','hotove',]#'slovicka']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

#
# class OdpovedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Odpoved
#         fields = ['ziak', 'pokus', 'spravne', 'odpoved', 'jespravne']
#
#     def create(self, validated_data):
#         return Odpoved.object.get_or_create(**validated_data)


class PokusSerializer(serializers.ModelSerializer):
    #odpoved_set = OdpovedSerializer(many=True)

    class Meta:
        model = Pokus
        fields = ['ziak', 'cvicenie'] #'odpoved_set']

    def create(self, validated_data):
        instance, created = Pokus.objects.get_or_create(**validated_data)
        print(instance, created)
        return instance
