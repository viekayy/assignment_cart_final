import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cart_backend.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = "viekayy"
password = "admin123"
email = "viekayy.1234@gmail.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created.")
else:
    print("Superuser already exists.")