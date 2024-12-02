from .models import Task
from .forms import TaskCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import EditAccountForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from .forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

@login_required
def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('tasks:detalles_cuenta')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'tasks/edit_password.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('tasks:login')
    return render(request, 'tasks/delete_account.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('tasks:detalles_cuenta'))  # Redirige a la pantalla de detalles de la cuenta
            else:
                print("Error al autenticar al usuario")  # Mensaje de depuración
        else:
            print("Formulario inválido")  # Mensaje de depuración
    return render(request, 'tasks/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('tasks:detalles_cuenta'))  # Redirige a la pantalla de detalles de la cuenta
            else:
                print("Error al autenticar al usuario")  # Mensaje de depuración
        else:
            print("Formulario inválido")  # Mensaje de depuración
    else:
        form = AuthenticationForm(request)
    return render(request, 'tasks/login.html', {'form': form})

@login_required
def delete_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks:index')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def edit_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_detail', pk=pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})
@login_required
def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def edit_account(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('tasks:detalles_cuenta')
    else:
        form = EditAccountForm(instance=request.user)
    return render(request, 'tasks/edit_account.html', {'form': form})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('tasks:account')
    else:
        form = ChangePasswordForm(instance=request.user)
    return render(request, 'tasks/change_password.html', {'form': form})

@login_required
def edit_account_view(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('tasks:account')
    else:
        form = EditAccountForm(instance=request.user)
    return render(request, 'tasks/edit_account.html', {'form': form})

@login_required
def account_view(request):
    return render(request, 'tasks/account.html', {'user': request.user})

@login_required
def delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/delete_account.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('tasks:login')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        task = Task(title=title, content=content)
        task.save()
        return redirect('tasks:index')
    else:
        params = {
            'form': TaskCreationForm(),
        }
        return render(request, 'tasks/create.html', params)


def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    params = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', params)


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.title = request.POST['title']
        task.content = request.POST['content']
        task.save()
        return redirect('tasks:detail', task_id)
    else:
        form = TaskCreationForm(initial={
            'title': task.title,
            'content': task.content,
        })
        params = {
            'task': task,
            'form': form,
        }
        return render(request, 'tasks/edit.html', params)


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.delete()
        return redirect('tasks:index')
    else:
        params = {
            'task': task,
        }
        return render(request, 'tasks/delete.html', params)

def detalles_cuenta(request):
    return render(request, 'tasks/detalles_cuenta.html')

@login_required
def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

