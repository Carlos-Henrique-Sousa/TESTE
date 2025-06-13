from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  PROFILE_CHOICES = (
    ('admin', 'Escola'),
    ('professor', 'Professor'),
    ('aluno', 'Aluno'),
    ('responsavel', 'Responsável'),
    ('user', 'Usuário'),
  )
  profile = models.CharField(
    max_length=20,
    choices=PROFILE_CHOICES,
    default='user',
    verbose_name='Perfil'
  )
  