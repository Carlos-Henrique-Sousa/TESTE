from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

""""
vcs tão fazendo oq agr vou jantar jaja mas
rlx

tem o que pra eu fazer, me perdi, tava fazendo coisa pra mãe
lá no olha.txt eu mandei algumas instruções pra faze
eu vi, mas tá confuso algumas 


"""

class UsuarioManage(BaseUserManager):
  def create_user(self, identificador, senha=None, email=None, **extra_fields):
    if not identificador:
      raise ValueError()
    user = self.model(identificador=identificador, email=email, **extra_fields)
        user.set_password(senha)
        user.save()
        return user

    def create_superuser(self, identificador, email=None, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(identificador, email, senha, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    identificador = models.CharField(max_length=100, unique=True)  # ex: _joao, #ana, @escola
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