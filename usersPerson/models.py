from django.contrib.auth.models import AbstractUser
from django.db import models

class ClientTenant(models.Model):
    name = models.CharField(max_length=100)
    CNPJCPF = models.CharField(max_length=20, unique=True)
    responsible = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    # Profile image field
    profileImage = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    # Address fields
    street = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    # Status
    isActive = models.BooleanField(default=True)

    # Adding related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Use a unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Use a unique related name
        blank=True
    )

    def __str__(self):
        return self.username

class Client(User):
    service_history = models.TextField(blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)
    
    # Permission field
    permission = models.CharField(max_length=50, default='Client')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Professional(User):
    specialty = models.CharField(max_length=100, blank=True, null=True)
    availability = models.CharField(max_length=50, blank=True, null=True)  # e.g., 'Full-time', 'Part-time'
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    
    # Permission field
    permission = models.CharField(max_length=50, default='Professional')

    class Meta:
        verbose_name = 'Professional'
        verbose_name_plural = 'Professionals'


class Administrator(User):
    #admin_permissions = models.TextField(blank=True, null=True)  # e.g., JSON data for specific permissions
    
    # Permission field
    permission = models.CharField(max_length=50, default='Administrator')

    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'


class TenantUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_tenant = models.ForeignKey(ClientTenant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.client_tenant.name}"
