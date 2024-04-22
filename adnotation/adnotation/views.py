# views.py
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo


def page(request):
    return render(request, 'page.html')


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')  # Przekieruj użytkownika na stronę z listą zdjęć
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})


def photo_list(request):
    photos = Photo.objects.all()  # Pobierz wszystkie obiekty Photo
    return render(request, 'photo_list.html', {'photos': photos})  # Przekazanie listy zdjęć do szablonu

# from django.http import JsonResponse
# from django.shortcuts import render
# from .forms import PhotoForm


# def save_image(request):
#     if request.method == 'POST':
#         description = request.POST.get('description')
#         image_file = request.FILES.get('photo')
#
#         try:
#             Photo.objects.create(description=description, image=image_file)
#             return JsonResponse({'success': True})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)})
#     return JsonResponse({'success': False, 'error': 'Invalid request'})
