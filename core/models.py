from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


class UsuarioManager(BaseUserManager):
    def create_user(self, identificador, senha=None, email=None, **extra_fields):
        if not identificador:
            raise ValueError("O identificador deve ser informado")
        user = self.model(
            identificador=identificador, email=email, **extra_fields
        )
        user.set_password(senha)
        user.save()
        return user

    def create_superuser(self, identificador, email=None, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser deve ter is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser deve ter is_superuser=True.")

        return self.create_user(identificador, senha=senha, email=email, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    identificador = models.CharField(max_length=100, unique=True) 
    email = models.EmailField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True)

    tipo = models.CharField(max_length=20, choices=[
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('escola', 'Escola'),
        ('admin', 'Administrador'),
    ])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'identificador'
    REQUIRED_FIELDS = ['email']

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.tipo.upper()} | {self.identificador}"
