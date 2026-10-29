from django.shortcuts import redirect,render
from app.models import Employee
from app.form import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
@login_required
def home(request):
    employee=Employee.objects.all()
    return render(request,'app/home.html',{"employee":employee})
def details(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'app/employee_details.html',{"employee":employee})
def add_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(employee_success)
    else:
        form=EmployeeForm()
    return render(request,'app/add_employee.html',{'form':form})
def employee_success(request):
    return render(request,'app/employee_success.html')
def register(request):
    if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    else:
     form=UserCreationForm
    return render(request,'app/register.html',{"form":form})