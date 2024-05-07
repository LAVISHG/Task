# Generated by Django 3.0.5 on 2024-05-05 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20240506_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.Customer')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.PurchaseOrder')),
            ],
        ),
    ]
