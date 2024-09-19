from django.http import HttpResponse
from productsServices.models import Produto, Servico
from django.shortcuts import get_object_or_404
#importando a decorator e a request e response do Rest Framework
#request
from rest_framework.decorators import api_view
#response
from rest_framework.response import Response

from .serializers import ProductSerializer

#utilizamos o decorator importado
@api_view()
def product_list(request):
    #ao fazer esse tipo de consulta a baixo recebemos como retorno uma queryset com varios elementos
    produtos = Produto.objects.all()
    #o serializer espera reber por paramentro na instance um objeto e para transformar essa queryset em objeto passamos o parametro many=True informando que ele tem varios elementos
    #assim transporfamando a queryset em objeto
    serializer = ProductSerializer(instance=produtos, many=True, context={'request': request})
    return Response(serializer.data)


@api_view()
def product_detail(request, pk):
    #ao fazer esse tipo de consulta a baixo recebemos como retorno uma queryset com um unico elemento por conta que estamos filtrando um unico produto e pegando o primeiro encontrado
    produto = get_object_or_404(Produto.objects.all(), pk=pk)
    #colocamos o many=False por conta que agora estamos passando apenas um elemento como instancia
    serializer = ProductSerializer(instance=produto, many=False, context={'request': request})
    return Response(serializer.data)