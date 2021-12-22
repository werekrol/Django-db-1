from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('image', models.URLField(default=None)),
                ('price', models.IntegerField(default=None)),
                ('release_date', models.DateField(default=None)),
                ('lte_exists', models.BooleanField(default=None)),
                ('slug', models.SlugField(default=None)),
            ],
        ),
    ]