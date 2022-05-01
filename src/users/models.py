from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    DB model to alter built-in Django User model.
    
    Attributes
    ----------
    is_student : if True, student features access gained
    is_teacher : if True, teacher features access gained
    """
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
