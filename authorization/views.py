from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            errors = form.errors.as_data()
            for field, error_msgs in errors.items():
                for error_msg in error_msgs:
                    messages.error(request, str(error_msg)[2:-3])
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
