# Generated by Django 4.1 on 2022-12-22 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('is_special', models.BooleanField(default=False)),
                ('is_vegan', models.BooleanField(default=False)),
                ('is_publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='core.food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='core.foodcategory'),
        ),
    ]
