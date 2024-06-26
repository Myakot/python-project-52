from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0003_alter_task_options_alter_task_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLabelDependence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labels.label')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(related_name='labels', through='tasks.TaskLabelDependence', to='labels.label', verbose_name='Labels'),
        ),
    ]
