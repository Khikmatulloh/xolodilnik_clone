from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db  import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel
from users.manager import UserManager

class User(AbstractBaseUser,PermissionsMixin,BaseModel):
    email= models.EmailField(_("Email"),max_length=255,unique=True)
    phone_number=models.CharField(_("Phone Number"), max_length=20, null=True,blank=True)
    first_name=models.CharField(max_length=100, null=True, blank=True)
    last_name=models.CharField(max_length=100, null=True, blank=True)
    avatar=models.ImageField(upload_to="avatars", null=True, blank=True)
    is_confirmed=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_spuruser=models.BooleanField(default=False)


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=UserManager()

    class Meta:
        verbose_name=_("User")
        verbose_name_plural=_("Users")

    def __str__(self):
        return self.email
    



