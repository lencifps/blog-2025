from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminDjango
from django.contrib.auth.models import Group
from apps.user.models import User

class UserAdmin(UserAdminDjango):
    fieldsets = UserAdminDjango.fieldsets + (
        (None, {'fields': ('alias', 'avatar')}),
    )

    add_fieldsets =  (
       (None, {
           'fields': ('username', 'email', 'alias', 'avatar', 'password1', 'password2'),           
       }),
   )



    def is_registrado(self, obj):
        return obj.groups.filter(name="registrado").exists()
    is_registrado.short_description = "Es Usuario Registrado"
    is_registrado.boolean = True


    def is_colaborador(self, obj):
        return obj.groups.filter(name="colaborador").exists()
    is_colaborador.short_description = "Es Usuario Colaborador"
    is_colaborador.boolean = True


    def is_moderador(self, obj):
        return obj.groups.filter(name="moderador").exists()
    is_moderador.short_description = "Es Usuario Moderador"
    is_moderador.boolean = True


    def add_to_registrado(self, request, queryset):
        registrado_group = Group.objects.get(name="registrado")
        for user in queryset:
            user.groups.add(registrado_group)
        self.message_user(
            request, f"Los usuarios seleccionados han sido agregados al grupo 'registrado'.")
    add_to_registrado.short_description = "Agregar al grupo 'registrado'"       

    
    def add_to_colaborador(self, request, queryset):
        colaborador_group = Group.objects.get(name="colaborador")
        for user in queryset:
            user.groups.add(colaborador_group)
        self.message_user(
                request, f"Los usuarios seleccionados han sido agregados al grupo 'colaborador'.")
    add_to_colaborador.short_description = "Agregar al grupo 'colaborador'"


    def add_to_moderador(self, request, queryset):
        moderador_group = Group.objects.get(name="moderador")
        for user in queryset:
            user.groups.add(moderador_group)
        self.message_user(
                request, f"Los usuarios seleccionados han sido agregados al grupo 'moderador'.")
    add_to_moderador.short_description = "Agregar al grupo 'moderador'" 

    
    actions = [add_to_registrado, add_to_colaborador, add_to_moderador]

    list_display = ['username', 'email', 'is_staff', 'is_superuser', 'is_registrado', 'is_colaborador', 'is_moderador']

    ordering = ['-date_joined']

    search_fields = ['username', 'email', 'id']
        


admin.site.register(User, UserAdmin)

    

