from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

def set_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Resume = apps.get_model('builder', 'Resume')
    
    # Create a default user if no users exist
    default_user, created = User.objects.get_or_create(
        username='default_user',
        defaults={'email': 'default@example.com'}
    )
    
    # Set all existing resumes to the default user
    Resume.objects.filter(user__isnull=True).update(user=default_user)

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('builder', '0003_remove_resume_github_remove_resume_website_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(set_default_user),
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL),
        ),
    ]
