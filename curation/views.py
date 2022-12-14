from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ContactForm, CategoryForm
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required


# Create your views here.
# Only uncomment this line if you don't want people to see the homepage if they aren't logged in.
def index(request):
    return render(request, 'curation/index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'curation/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'curation/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'curation/thanks.html')
    else:
        context = {'form': form}
        return render(request, 'curation/contact.html', context)


@login_required(login_url='login')
def view_category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'curation/category.html', context)


@login_required(login_url='login')
def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_category')
    else:
        return render(request, 'curation/submit.html', {'form': form})


@login_required(login_url='login')
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('view_category')
    else:
        return render(request, 'curation/submit.html', {'form': form})


@login_required(login_url='login')
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('view_category')
    else:
        return render(request, 'curation/delete.html', {'category': category})
