from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.info(f"User logged in: {user.email} from IP: {get_client_ip(request)}")


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.info(f"User logged out: {user.email}")


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    return (
        x_forwarded_for.split(",")[0]
        if x_forwarded_for
        else request.META.get("REMOTE_ADDR")
    )
