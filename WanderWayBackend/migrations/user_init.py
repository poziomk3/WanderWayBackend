from django.db import migrations
from django.conf import settings
from faker import Faker


def load_initial_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    faker = Faker()

    User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword')

    for _ in range(5):
        username = faker.user_name()
        email = faker.email()
        password = faker.password()
        User.objects.create_user(username=username, email=email, password=password)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL)
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]