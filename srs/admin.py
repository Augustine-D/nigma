from django.contrib import admin
from .models import User, Customer, Employee, Admin,Issues,IssuesPriority,IssuesProgress,IssuesTypes

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(Issues)
admin.site.register(IssuesPriority)
admin.site.register(IssuesProgress)
admin.site.register(IssuesTypes)