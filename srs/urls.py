from django.urls import path
from . views import (
IssueCreateView, IssueListView, IssueUpdateView, 
IssueDetailView,  IssueDeleteView, EmpIssueListView,
EmpUpdateView,AdminUpdateView,AdminIssueListView
)
from . import views 


from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.login_request, name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),

    path('', views.home, name='base-home'),

    path('customer_register/',views.customer_register.as_view(), name='customer_register'),
    path('employee_register/',views.employee_register.as_view(), name='employee_register'),
    path('admin_register/',views.admin_register.as_view(), name='admin_register'),

    path('issues_create/',IssueCreateView.as_view(), name='create'),
    path('issues/',IssueListView.as_view(), name='list'),

    path('emp_issues_update/<int:pk>/',EmpUpdateView.as_view(), name='emp_pdate'),
    path('admin_issues_update/<int:pk>/',AdminUpdateView.as_view(), name='admin_update'),
    path('issues_update/<int:pk>/',IssueUpdateView.as_view(), name='update'),

    path('issues_detail/<int:pk>/',IssueDetailView.as_view(), name='detail'),
    path('issues_delete/<int:pk>/',IssueDeleteView.as_view(), name='delete'), 

    path('emp_issues/',EmpIssueListView.as_view(), name='emp_issues'),
    path('admin_issues/',AdminIssueListView.as_view(), name='admin_issues'),

    

]