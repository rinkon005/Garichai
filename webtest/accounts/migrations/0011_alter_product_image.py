# Generated by Django 3.2.7 on 2021-12-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='shop/image/Screenshot_from_2021-06-24_14-10-45.png', upload_to=''),
        ),
    ]