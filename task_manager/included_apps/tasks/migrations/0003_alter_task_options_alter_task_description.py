from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['id'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Description'),
        ),
    ]
