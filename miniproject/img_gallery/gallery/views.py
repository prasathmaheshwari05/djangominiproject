from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .forms import ImageForm

def home(request):
    images = Image.objects.all()
    return render(request, 'gallery/home.html', {'images': images})

def detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm(instance=image)
    return render(request, 'gallery/detail.html', {'image': image, 'form': form})

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'gallery/add_image.html', {'form': form})
