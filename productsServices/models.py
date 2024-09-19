from django.db import models
from usersPerson.models import ClientTenant  # Importar o modelo ClientTenant

class Marca(models.Model):
    name = models.CharField(max_length=100, unique=True)
    client_tenant = models.ForeignKey(ClientTenant, on_delete=models.CASCADE)  # Controle de inquilino

    def __str__(self):
        return self.name


class Categoria(models.Model):
    name = models.CharField(max_length=100, unique=True)
    client_tenant = models.ForeignKey(ClientTenant, on_delete=models.CASCADE)  # Controle de inquilino

    def __str__(self):
        return self.name


class Produto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=255)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ean = models.CharField(max_length=13, unique=True, blank=True, null=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    estoque = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    margem_lucro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    porcentagem_lucro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    client_tenant = models.ForeignKey(ClientTenant, on_delete=models.CASCADE)  # Controle de inquilino

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    ESPECIALIDADE_CHOICES = [
        ('cabelo', 'Cabelo'),
        ('unha', 'Unha'),
        ('maquiagem', 'Maquiagem'),
        ('massagem', 'Massagem'),
        ('estetica', 'Estética'),
        ('design_sobrancelha', 'Design de Sobrancelha'),
        ('barba', 'Barba'),
    ]

    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    comissao = models.DecimalField(max_digits=10, decimal_places=2)
    especialidade = models.CharField(max_length=20, choices=ESPECIALIDADE_CHOICES)
    client_tenant = models.ForeignKey(ClientTenant, on_delete=models.CASCADE)  # Controle de inquilino

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
