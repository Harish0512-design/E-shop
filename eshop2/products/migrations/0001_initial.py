# Generated by Django 3.0.7 on 2020-06-09 02:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('p_name', models.CharField(max_length=100)),
                ('p_price', models.FloatField()),
                ('p_img', models.ImageField(upload_to='images')),
                ('p_quantity', models.IntegerField(default=1, null=True)),
                ('amount', models.FloatField(default=0)),
                ('p_instock', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_price', models.FloatField()),
                ('p_date', models.DateTimeField(auto_now_add=True)),
                ('p_des', models.TextField()),
                ('p_img', models.ImageField(upload_to='images')),
                ('p_instock', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_price', models.FloatField()),
                ('p_img', models.ImageField(upload_to='images')),
                ('p_quantity', models.IntegerField(default=1, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('p_instock', models.IntegerField(default=1)),
                ('sold_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(null=True, upload_to='images')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=100)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('hno', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('dist', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('user_register_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('hno', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('dist', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('sold_on', models.DateTimeField(auto_now_add=True)),
                ('delivered_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='products.Sold')),
            ],
        ),
    ]
