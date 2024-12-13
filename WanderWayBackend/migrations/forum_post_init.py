import random
from faker import Faker
from django.db import migrations


def load_initial_data(apps, schema_editor):
    forum_post_model = apps.get_model('WanderWayBackend', 'ForumPost')
    Route = apps.get_model('WanderWayBackend', 'Route')
    User = apps.get_model('auth', 'User')
    faker = Faker()

    users = list(User.objects.all())
    routes = [Route.objects.get(id=i) for i in range(1, 6)]

    forum_posts = [
        {'title': 'Great Route', 'rating': 5, 'route': routes[0]},
        {'title': 'Nice Experience', 'rating': 4, 'route': routes[1]},
        {'title': 'Good but crowded', 'rating': 3, 'route': routes[2]},
        {'title': 'Beautiful Scenery', 'rating': 5, 'route': routes[3]},
        {'title': 'Average Route', 'rating': 3, 'route': routes[4]},
    ]

    for post in forum_posts:
        post['author'] = random.choice(users)
        post['body'] = faker.text(max_nb_chars=random.randint(10, 150))
        forum_post_model.objects.create(**post)


class Migration(migrations.Migration):

    dependencies = [
        ('WanderWayBackend', 'forum_post')
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]