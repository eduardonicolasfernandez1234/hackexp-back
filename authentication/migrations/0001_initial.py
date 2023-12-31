# Generated by Django 4.2 on 2023-10-27 11:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_user_id', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='role_category', to='core.categoryrole')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_user_id', models.PositiveIntegerField(default=0)),
                ('short_code', models.CharField(max_length=3)),
                ('profile_image', models.ImageField(default=None, null=True, upload_to='')),
                ('phone', models.CharField(default=None, max_length=15, null=True)),
                ('web_site', models.URLField(default=None, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='admin_city', to='core.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='admin_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_user_id', models.PositiveIntegerField(default=0)),
                ('short_code', models.CharField(max_length=3)),
                ('profile_image', models.ImageField(default=None, null=True, upload_to='')),
                ('phone', models.CharField(default=None, max_length=15, null=True)),
                ('ci', models.CharField(default=None, max_length=10, null=True)),
                ('other_position', models.CharField(default=None, max_length=10, null=True)),
                ('other_area', models.CharField(default=None, max_length=10, null=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='employee_area', to='core.area')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='employee_business', to='authentication.useradmin')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='employee_city', to='core.city')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='employee_position', to='core.position')),
                ('roles', models.ManyToManyField(default=[], related_name='employee_roles', to='authentication.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='employee_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_user_id', models.PositiveIntegerField(default=0)),
                ('short_code', models.CharField(max_length=3)),
                ('profile_image', models.ImageField(default=None, null=True, upload_to='')),
                ('phone', models.CharField(default=None, max_length=15, null=True)),
                ('web_site', models.URLField(default=None, null=True)),
                ('name_business', models.CharField(default=None, max_length=40, null=True)),
                ('nit', models.CharField(default=None, max_length=12, null=True)),
                ('address', models.CharField(default=None, max_length=120, null=True)),
                ('telephone', models.CharField(default=None, max_length=15, null=True)),
                ('other_industry', models.CharField(default=None, max_length=120, null=True)),
                ('total_employeers', models.PositiveIntegerField(default=0)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='business_city', to='core.city')),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='business_industry', to='core.industry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='business_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')])),
                ('user_type', models.PositiveSmallIntegerField(choices=[(0, 'Business'), (1, 'Employee'), (2, 'Admin')])),
                ('is_deleted', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_groups', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', to='auth.permission', verbose_name='User permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
