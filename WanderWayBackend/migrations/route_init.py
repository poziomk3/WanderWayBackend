import os
from django.db import migrations
from WanderWayBackend.settings import BASE_DIR


def load_initial_data(apps, schema_editor):
    route_model = apps.get_model('WanderWayBackend', 'Route')

    if not os.path.exists(BASE_DIR / '/gpx'):
        os.mkdir(BASE_DIR / '/gpx')
    else:
        for file in os.listdir(BASE_DIR / '/gpx'):
            if file.endswith('.gpx'):
                route_model.objects.create(
                    filePath=file
                )



class Migration(migrations.Migration):

    dependencies = [
        ('WanderWayBackend', 'route'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]


