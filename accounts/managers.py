from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        if not email:
            raise ValueError("User must have an email address!")
        elif not phone:
            raise ValueError("User must have a phone number")

        user = self.model(
            email = self.normalize_email(email),
            phone = phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None):
        user = self.create_user(
            email,
            password = password,
            phone = phone
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
