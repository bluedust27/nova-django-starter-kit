from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

import logging

logger = logging.getLogger(__name__)


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        logger.info(f"Team saved: {self.name}")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        logger.warning(f"Team deleted: {self.name}")
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["name"]


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, team_name=None, password=None, **extra_fields):
        if not email:
            logger.warning("Attempt to create user without email.")
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)

        # Ensure team_name is either None or a valid TeamName instance
        if team_name and not isinstance(team_name, Team):
            logger.error(f"Invalid team_name type: {team_name} ({type(team_name)})")
            raise ValueError("team_name must be a valid TeamName instance or None")

        user = self.model(email=email, name=name, team_name=team_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        logger.info(f"User created: {email}, Team: {team_name}")
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        logger.info(f"Superuser created: {email}")
        return self.create_user(
            email, name, team_name=None, password=password, **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Email as the unique identifier
    name = models.CharField(max_length=255)
    team_name = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
