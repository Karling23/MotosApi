from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

Usuario = get_user_model()

def create_user(username, email='', password='Password123!', is_staff=False):
    if not email:
        email = f"{username}@example.com"
    user = Usuario.objects.create_user(
        username=username,
        email=email,
        password=password,
    )
    if is_staff:
        user.is_staff = True
        user.save()
    return user

def get_tokens(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token), str(refresh)
