from django.http import HttpResponse
from productsServices.models import Produto, Servico
from django.shortcuts import get_object_or_404

#importando a decorator e a request e response do Rest Framework
#request
from rest_framework.decorators import api_view
#response
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

#utilizamos o decorator importado
@api_view(http_method_names=['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        #ao fazer esse tipo de consulta a baixo recebemos como retorno uma queryset com varios elementos
        produtos = Produto.objects.all()
        #o serializer espera reber por paramentro na instance um objeto e para transformar essa queryset em objeto passamos o parametro many=True informando que ele tem varios elementos
        #assim transporfamando a queryset em objeto
        serializer = ProductSerializer(instance=produtos, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        #ao passar o parametro raise_exception=True evitamos utilizar um If para validar se foi bem sucessedido ou não
        #e faz o lançamento da excessão
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    


@api_view()
def product_detail(request, pk):
    #ao fazer esse tipo de consulta a baixo recebemos como retorno uma queryset com um unico elemento por conta que estamos filtrando um unico produto e pegando o primeiro encontrado
    produto = get_object_or_404(Produto.objects.all(), pk=pk)
    #colocamos o many=False por conta que agora estamos passando apenas um elemento como instancia
    serializer = ProductSerializer(instance=produto, many=False, context={'request': request})
    return Response(serializer.data)