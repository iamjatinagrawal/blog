# Generated by Django 2.2.9 on 2020-08-15 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200614_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberEmailModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.BaseModel')),
                ('email_id', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Subscriber Email',
                'verbose_name_plural': 'Subscriber Emails',
                'db_table': 'SubscriberEmailModel',
            },
            bases=('blog.basemodel',),
        ),
    ]
