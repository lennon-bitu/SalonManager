'''
criando serializer informandos os campos de forma manual criando cada um e seus tipos
'''
from rest_framework import serializers
from productsServices.models import Categoria

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
    preco = serializers.DecimalField(max_digits=10, decimal_places=2)

    #campo categoria possui chave estrangeira em produto e utilizando serializers.StringRelatedField()
    # pegamos o moetodo str da class categoria que exibe o nome da categoria relacionada ao produto
    categoria = serializers.StringRelatedField()
    imagem = serializers.CharField()
    
    ''' 
    Exemplo de como buscar um campo de chave estrangeira e exibir seu id e seu nome em um outro campo renomedo e referenciando o campo original do model

    #quando precisamos utilizar um campo que sera chave estrangeira fazemos a declaração da variavel e atribuimos a ela o tipo de PrimaryKeyRelatedField
    # e precisamos passar como parametro para ela uma queryset com as informações dos dados dessa categoria utilizando o parametro queryset = Categoria.objects.all()
    # 

    categoria = serializers.PrimaryKeyRelatedField(
        queryset = Categoria.objects.all()
    )
    '''
    
    '''
    #criamos um nome campo  categoria_nome = serializers.StringRelatedField(source='categoria')
    onde o paramentro source indica para qual campo estamos referenciado a renomeação do campo
    assim podemos obter o id no campo categoria e o nome da categoria no categoria_nome
    
    categoria_nome = serializers.StringRelatedField(source='categoria')
    '''
    