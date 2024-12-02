from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, nombre_de_usuario, correo_electronico, password=None):
        if not nombre_de_usuario:
            raise ValueError('El nombre de usuario es obligatorio')
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')

        user = self.model(
            nombre_de_usuario=nombre_de_usuario,
            correo_electronico=self.normalize_email(correo_electronico),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre_de_usuario, correo_electronico, password=None):
        user = self.create_user(
            nombre_de_usuario,
            correo_electronico,
            password=password,
        )
        user.es_superusuario = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    nombre_de_usuario = models.CharField(max_length=150, unique=True, db_index=True)
    correo_electronico = models.EmailField(unique=True)
    edad = models.PositiveIntegerField(default=0)
    es_superusuario = models.BooleanField(default=False)
    es_personal = models.BooleanField(default=False)
    esta_activo = models.BooleanField(default=True)
    fecha_union = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'nombre_de_usuario'
    REQUIRED_FIELDS = ['correo_electronico']

    objects = CustomUserManager()

    def __str__(self):
        return self.nombre_de_usuario

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.es_superusuario

    @property
    def is_superuser(self):
        return self.es_superusuario

    @property
    def is_active(self):
        return self.esta_activo


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title