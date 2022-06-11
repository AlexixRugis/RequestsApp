from django.contrib.auth.models import BaseUserManager 

class EmployeeManager(BaseUserManager):
    def create_user(self, name, email, phone_number, password):
        user = self.model(email=email, name=name, phone_number=phone_number, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password):
        user = self.model(email=email, phone_number=phone_number, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, phone_number):
        return self.get(phone_number=phone_number)