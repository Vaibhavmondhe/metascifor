from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_add_user_to_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='user',
        ),
    ]
