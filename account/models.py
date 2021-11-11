import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email es obligatorio')
        user = self.model(username=username, email=email, is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20, blank=True)
    #image = models.ImageField(upload_to='accounts')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "Usuarios"
        verbose_name_plural = "Usuarios"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'diegojespana@gmail.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.name


class Address(models.Model):
    """
    Address
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, verbose_name=_("Cliente"), on_delete=models.CASCADE)
    full_name = models.CharField(_("Nombre Completo"), max_length=150)
    phone = models.CharField(_("Número de Teléfono"), max_length=50)
    postcode = models.CharField(_("Código Postal"), max_length=50)
    address_line = models.CharField(_("Dirección(Línea 1)"), max_length=255)
    address_line2 = models.CharField(_("Dirección(Línea 2)"), max_length=255)
    town_city = models.CharField(_("Ciudad"), max_length=150)
    delivery_instructions = models.CharField(_("Intrucciones de Entrega"), max_length=255)
    created_at = models.DateTimeField(_("Creado"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Actualizado"), auto_now=True)
    default = models.BooleanField(_("Predeterminado"), default=False)

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return "Address"
