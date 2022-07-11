# Generated by Django 4.0.5 on 2022-07-09 08:29

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_customer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
        migrations.CreateModel(
            name='IssuesPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Priority_Title', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['Priority_Title'],
            },
        ),
        migrations.CreateModel(
            name='IssuesProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Progress_Title', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['Progress_Title'],
            },
        ),
        migrations.CreateModel(
            name='IssuesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Title', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['Type_Title'],
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['designation'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['designation'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['designation'],
            },
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Issue_Description', models.TextField()),
                ('Issue_Created_On', models.DateTimeField(auto_now_add=True)),
                ('Issue_Closed_By', models.CharField(blank=True, max_length=200, null=True)),
                ('Issue_Closed_On', models.CharField(blank=True, max_length=200, null=True)),
                ('Issue_Complete', models.BooleanField(default=False)),
                ('Issue_Solution_Summary', models.TextField(blank=True, null=True)),
                ('Issue_Priority', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.issuespriority')),
                ('Issue_Progress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.issuesprogress')),
                ('Issue_Title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.issuestypes')),
                ('Issuer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Issue_Solver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='srs.employee')),
            ],
            options={
                'ordering': ['Issue_Description'],
            },
        ),
    ]