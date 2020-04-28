from django.db import migrations
from perftest1.models import Test

def add_test(apps, schema_editor):
    test = Test.objects.create(naziv='Matematika')
    test.save()



class Migration(migrations.Migration):

    dependencies = [
        ('perftest1', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_test),
    ]
