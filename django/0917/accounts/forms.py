from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meata:
        model=get_user_model()
        fields = ('last_name','first_name','email')