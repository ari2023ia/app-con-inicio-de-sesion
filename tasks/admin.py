from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task

class CustomUserAdmin(UserAdmin):
    ordering = ('nombre_de_usuario',)
    list_display = ('nombre_de_usuario', 'correo_electronico', 'es_superusuario')
    search_fields = ('nombre_de_usuario', 'correo_electronico')
    readonly_fields = ('fecha_union',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre_de_usuario', 'correo_electronico', 'password1', 'password2'),
        }),
    )

    fieldsets = (
        (None, {'fields': ('nombre_de_usuario', 'correo_electronico', 'password')}),
    )

    list_filter = ('nombre_de_usuario', 'correo_electronico')

    # Eliminar los campos groups y user_permissions
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task)