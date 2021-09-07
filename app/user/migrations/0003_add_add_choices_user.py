from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_add_guild_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='mode_game',
            field=models.CharField(choices=[('Mobile', 'Mobile'), ('Computer', 'Computer')], default='Mobile', max_length=50, verbose_name='Mode Game'),
        ),
    ]
