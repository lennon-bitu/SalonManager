'''
criando serializer informandos os campos de forma manual criando cada um e seus tipos
'''
from collections import defaultdict
from rest_framework import serializers
from productsServices.models import Categoria, Produto
from usersPerson.api.serializers import ClientTenantSerializer
import re


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','codigo', 'nome', "preco_custo", 'preco', 'ean', 'imagem', 'estoque', 'is_active', 'margem_lucro', 'porcentagem_lucro', 'marca', 'categoria', 'client_tenant' ]

    # Campo categoria configurado para mostrar o String com o nome da categoria ao invés di id
    categoria = serializers.StringRelatedField()
    # Campo marca configurado para mostrar o String com o nome da marca ao invés di id
    marca = serializers.StringRelatedField()

    client_tenant = ClientTenantSerializer(many=False, read_only=True)


    def validate(self, attrs):
        
        super_validate = super().validate(attrs)

        cd = attrs
        _my_errors = defaultdict(list)

        codigo = cd.get('codigo')
        nome = cd.get('nome')

        # Regex para encontrar caracteres especiais
        padrao = r'[^a-zA-Z0-9\s]'

        # Encontrar todos os caracteres especiais
        caracteres_especiais_nome = re.findall(padrao, nome)
        caracteres_especiais_codigo = re.findall(padrao, codigo)

        if caracteres_especiais_nome:
            _my_errors['nome'].append('Não e permitido caracteres especiais no nome do produto')

        if caracteres_especiais_codigo:
            _my_errors['codigo'].append('Não e permitido caracteres especiais no codigo do produto')

        if _my_errors:
            raise serializers.ValidationError(_my_errors)
        
        return super_validate

    
    def validate_codigo(self, value):
        if not value.isalnum():  # Exemplo de validação adicional
            raise serializers.ValidationError('O código deve conter apenas caracteres alfanuméricos.')
        return value