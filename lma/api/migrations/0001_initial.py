# Generated by Django 3.1.1 on 2020-09-15 03:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=50)),
                ('membership', models.CharField(max_length=20)),
                ('payment_info', models.CharField(max_length=100)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=50)),
                ('assigned_date', models.DateField()),
                ('due_date', models.DateField()),
                ('description', models.TextField(max_length=500)),
                ('completed', models.BooleanField()),
                ('deleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=150)),
                ('is_active', models.BooleanField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('due_date', models.DateField()),
                ('issue_date', models.DateField()),
                ('title', models.CharField(max_length=75)),
                ('bill_to_name', models.CharField(max_length=75)),
                ('bill_to_address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=150)),
                ('cost', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.sale')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('tank_number', models.IntegerField()),
                ('canister_number', models.IntegerField()),
                ('top_id', models.IntegerField()),
                ('father', models.CharField(max_length=50)),
                ('mother', models.CharField(max_length=50)),
                ('units', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('sub_type', models.CharField(max_length=50)),
                ('header_image', models.CharField(max_length=150)),
                ('profile_image', models.CharField(max_length=150)),
                ('tag_number', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('breed', models.CharField(max_length=50)),
                ('father', models.CharField(max_length=50)),
                ('mother', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('attachment', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='api.user')),
            ],
        ),
    ]
