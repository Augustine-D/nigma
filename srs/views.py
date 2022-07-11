from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, EmployeeSignUpForm, AdminSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Issues

# Create your views here.

def home(request):
    return render(request, 'srs/index.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'srs/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'srs/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



class admin_register(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'srs/admin_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')




def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                messages.info(request, 'Logged in')
                return redirect('base-home')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'srs/login.html',
    context={'form':AuthenticationForm()})



class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issues
    context_object_name = 'issue'
    fields = ["Issue_Title","Issue_Priority",
    "Issue_Description"
    ]
    template_name = 'srs/issue_form.html'
    success_url = reverse_lazy('create')
    
    def form_valid(self, form):
         form.instance.Issuer = self.request.user
         return super(IssueCreateView, self).form_valid(form)



class IssueListView(LoginRequiredMixin,ListView):
    model = Issues

    context_object_name = 'issues'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = context['issues'].filter(Issuer=self.request.user)
        context['count'] = context['issues'].filter(Issue=True).count
           


        search_bar = self.request.GET.get('search-area') or ''
        if search_bar:
            context['issues'] = context['issues'].filter(
                 Issue_Description__icontains = search_bar)
        context['search_bar'] = search_bar   
        return context



class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issues
    context_object_name = 'issue'
    fields = [ "Issue_Title","Issue_Priority",
    "Issue_Description","Issue_Progress","Issue_Complete",
    "Issue_Solution_Summary","Issue_Approve"
    ]
    template_name = 'srs/issue_update.html'
    success_url = reverse_lazy('list')

class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issues
    context_object_name= 'issue'
    template_name = 'srs/issue_detail.html'


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issues
    context_object_name = 'issue'
    template_name = 'srs/issue_confirm_delete.html'
    success_url = reverse_lazy('base-home')

#employee list view

class EmpIssueListView(LoginRequiredMixin,ListView):
    model = Issues
    context_object_name = 'emp_issues'
    template_name = 'srs/emp_issues_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = context['emp_issues'].filter(Issue_Approve=True)
        context['count'] = context['emp_issues'].filter(Issue_Approve=True).count    

        search_bar = self.request.GET.get('search-area') or ''
        if search_bar:
            context['issues'] = context['issues'].filter(
                 Issue_Description__icontains = search_bar)
        context['search_bar'] = search_bar      
        return context





class AdminIssueListView(LoginRequiredMixin,ListView):
    model = Issues
    context_object_name = 'emp_issues'
    template_name = 'srs/emp_issues_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = context['emp_issues'].filter(Issue=True)
        context['count'] = context['emp_issues'].filter(Issue=True).count    

        search_bar = self.request.GET.get('search-area') or ''
        if search_bar:
            context['issues'] = context['issues'].filter(
                 Issue_Description__icontains = search_bar)
        context['search_bar'] = search_bar      
        return context


class EmpUpdateView(LoginRequiredMixin, UpdateView):
    model = Issues
    context_object_name = 'issue'
    fields = [ "Issue_Complete",
    "Issue_Solution_Summary"
    ]
    template_name = 'srs/emp_update.html'
    success_url = reverse_lazy('emp_issues')




class AdminUpdateView(LoginRequiredMixin, UpdateView):
    model = Issues
    context_object_name = 'issue'
    fields = ["Issue_Progress","Issue_Complete",
    "Issue_Solution_Summary","Issue_Approve"
    ]
    template_name = 'srs/admin_update.html'
    success_url = reverse_lazy('admin_issues')





    