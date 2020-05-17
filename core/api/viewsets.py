from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Cursos
from core.api.serialize import ModelSerializer
from sklearn.externals import joblib as jb
import numpy as np

class CursoViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = ModelSerializer
    filter_filed = ('idCurso')

    def list(self, request, *args, **kwargs):
        idCurso = self.request.query_params.get('idCurso')
        modelo = jb.load('modelo_ufrn.pkl')

        dados_mulheres = np.array([[idCurso, 0]])
        dados_homem = np.array([[idCurso,1]])

        predicaoHomem = modelo.predict(dados_homem)
        predicaoMulheres = modelo.predict(dados_mulheres)

        return Response({'Homens': predicaoHomem, 'Mulheres':predicaoMulheres})

    def get_queryset(self):
        return Response({'sei nao': 1})


