# Generated by Django 4.0.4 on 2022-05-28 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=30)),
                ('Category', models.CharField(choices=[('Coding', 'Coding'), ('Personal', 'Personal'), ('Career', 'Career'), ('Misc', 'Misc')], max_length=100)),
                ('Updated_on', models.DateTimeField(auto_now=True)),
                ('Created_on', models.DateTimeField(auto_now_add=True)),
                ('Body', models.TextField()),
                ('Status', models.IntegerField(choices=[(0, 'Draft/Private'), (1, 'Publish')], default=0)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Created_on'],
            },
            managers=[
                ('Post', django.db.models.manager.Manager()),
            ],
        ),
    ]