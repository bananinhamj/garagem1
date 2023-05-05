from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Cor, Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields= "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        Fields="__all__"
