from rest_framework.serializers import ModelSerializer
from core.models import Cursos



class CursoSerializer(ModelSerializer):
    class Meta:
        model = Cursos
        fields = ('quantidadeHomens', 'quantidadeMulheres')