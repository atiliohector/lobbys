from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('type_user', models.CharField(max_length=50)),
                ('mode_game', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('guild', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
    ]
