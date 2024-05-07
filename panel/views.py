from django.shortcuts import render, redirect, get_object_or_404
from .models import MyUsers
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def add_users(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        mobile_num = request.POST.get('mobileno')
        email = request.POST.get('email')

        users = MyUsers.objects.create(
            first_name = first_name,
            last_name = last_name,
            mobile_num = mobile_num,
            email = email
        )
        users.save()
        return redirect('panel:index')
    return render(request, 'users.html')


@login_required
def users_dashboard(request):
    users = MyUsers.objects.all()
    return render(request, 'users_dashboard.html', {'users':users})


def delete_user(request, id):
    user = get_object_or_404(MyUsers, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('panel:users_dashboard')
    

def edit_user(request, id):
    user = get_object_or_404(MyUsers, id=id)
    if request.method == 'post':
        return redirect('panel:add_users')