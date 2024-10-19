from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model


class CustomUserManager(BaseUserManager):
    """
    Custom manager for Shopping_User.
    """

    def create_user(self, username, email, password=None):
        """
        Create and return a regular user with an email and password.
        """
        if not username:
            raise ValueError("The username must be set")
        if not email:
            raise ValueError("The email must be set")

        email = self.normalize_email(email)
        User = get_user_model()
        user = User(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Create and return a superuser with an email and password.
        """
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
