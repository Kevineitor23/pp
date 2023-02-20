from django.shortcuts import render, redirect
from .forms import MyModelForm

def home(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MyModelForm()
    return render(request, 'home/index.html', {'form': form})
  