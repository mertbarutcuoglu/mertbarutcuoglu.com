# Generated by Django 3.0.6 on 2020-05-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_on_github', models.BooleanField()),
                ('github_link', models.URLField(blank=True, null=True)),
                ('is_on_blog', models.BooleanField()),
                ('blog_link', models.URLField(blank=True, null=True)),
                ('used_technologies', models.ManyToManyField(to='portfolio.Technology')),
            ],
        ),
    ]
