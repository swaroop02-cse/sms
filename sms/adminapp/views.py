import random
import string
from .models import Task
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm

def projecthomepage(request):
    return render(request, 'adminapp/ProjectHomePage.html')
def printpagecall(request):
    return render(request,'adminapp/printer.html')
def printpageLogic(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input:{user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)

def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')
def randomcall(request):
    return render(request,'adminapp/randomExample.html')
def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
        a1 = {'ran': ran}
        return render(request, 'adminapp/randomExample.html', a1)
    return render(request, 'adminapp/randomExample.html')
def calcualtorcall(request):
    return render(request,'adminapp/calculator.html')
def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})
from django.shortcuts import render
from datetime import datetime, timedelta
import calendar

def datetimepagecall(request):
    return render(request, 'adminapp/datetimepage.html')

def datetimepagelogic(request):
    if request.method == "POST":
        try:
            number1 = int(request.POST.get('date1', 0))
            current_date = datetime.now()
            future_date = current_date + timedelta(days=number1)
            year_of_future_date = future_date.year
            is_leap_year = calendar.isleap(year_of_future_date)

            leap_year_status = "Leap year" if is_leap_year else "Not a leap year"

            context = {
                'ran': future_date,
                'ran1': year_of_future_date,
                'ran3': leap_year_status,
                'number1': number1,
            }
        except (ValueError, TypeError):
            context = {
                'error': 'Invalid input. Please enter a valid number.',
            }

        return render(request, 'adminapp/datetimepage.html', context)
    else:
        return render(request, 'adminapp/datetimepage.html')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html', {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegister.html')


from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import User

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate


def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')


def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def UserLoginLogic(request):
    if request.method == 'POST':
        print("Form submitted")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("User authenticated")
            login(request, user)
            if len(username) == 10:
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:studentHomePage')
            elif len(username) == 4:
                return redirect('facultyapp:facultyHomePage')
            else:
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/UserLoginPage.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/UserLoginPage.html')

    return render(request, 'adminapp/UserLoginPage.html')

def logout(request):
        auth.logout(request)
        return redirect('ProjectHomePage')
from .forms import StudentForm
from .models import StudentList

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})
def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})


from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']

        # Read the CSV file
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)

        # Calculate total and average sales
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        # Group sales by month
        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()

        # Map months to names
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution per Month')

        # Save plot to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Encode image data to base64
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        context = {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'chart': image_data,
        }

        return render(request, 'adminapp/chart.html', context)

    return render(request, 'adminapp/chart.html', {'form': UploadFileForm()})
