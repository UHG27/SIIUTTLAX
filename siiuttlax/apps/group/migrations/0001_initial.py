
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0002_alter_category_options_alter_professor_options_and_more'),
        ('career', '0001_initial'),
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=1)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.period')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.semester')),
                ('students', models.ManyToManyField(to='academy.student')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.professor')),
            ],
        ),
    ]
