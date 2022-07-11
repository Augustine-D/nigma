from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    def __str__(self):
        return self.designation

    class Meta:
        ordering= ['designation']

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    def __str__(self):
        return self.designation

    class Meta:
        ordering= ['designation']

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    def __str__(self):
        return self.designation

    class Meta:
        ordering= ['designation']


class IssuesTypes(models.Model):
    Type_Title = models.CharField(max_length=200)
    

    def __str__(self):
        return self.Type_Title

    class Meta:
        ordering= ['Type_Title']


class IssuesPriority(models.Model):
    Priority_Title = models.CharField(max_length=200)
    

    def __str__(self):
        return self.Priority_Title

    class Meta:
        ordering= ['Priority_Title']


class IssuesProgress(models.Model):
    Progress_Title = models.CharField(max_length=200)
    

    def __str__(self):
        return self.Progress_Title

    class Meta:
        ordering= ['Progress_Title']
#    Issue_Title = models.ForeignKey(IssuesTypes, on_delete=models.CASCADE, null=True, blank=True)


class Issues(models.Model):
    Issuer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Issue_Title = models.ForeignKey(IssuesTypes, on_delete=models.CASCADE, null=True, blank=True)
    Issue_Priority = models.ForeignKey(IssuesPriority, on_delete=models.CASCADE, null=True, blank=True)
    Issue_Progress = models.ForeignKey(IssuesProgress, on_delete=models.CASCADE, null=True, blank=True)
    Issue = models.BooleanField(default=True)
    Issue_Approve = models.BooleanField(default=False)
    Issue_Description = models.TextField(null=False, blank=False)
    Issue_Created_On = models.DateTimeField(auto_now_add=True)
    Issue_Closed_By = models.CharField(max_length=200,null=True, blank=True) 
    Issue_Closed_On = models.CharField(max_length=200, null=True, blank=True)
    Issue_Complete = models.BooleanField(default=False)
    Issue_Solution_Summary = models.TextField(null=True, blank=True) 
