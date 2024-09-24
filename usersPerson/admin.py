from django.contrib import admin
from .models import User, Client, ClientTenant, TenantUser, Professional, Administrator

# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(ClientTenant)
admin.site.register(TenantUser)
admin.site.register(Professional)
admin.site.register(Administrator)
