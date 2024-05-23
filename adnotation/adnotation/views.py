# views.py
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import AnnotatedImage

def photo_list(request):
    annotated_images = AnnotatedImage.objects.all()
    context = {
        'annotated_images': annotated_images
    }
    return render(request, 'photo_list.html', context)

@csrf_exempt
def upload_annotations(request):
    if request.method == 'POST':
        image_file = request.FILES['imageFile']
        json_data = json.loads(request.POST['jsonFile'])

        annotated_image = AnnotatedImage(
            image=image_file,
            json_data=json_data
        )
        annotated_image.save()

        return redirect('index')  # Redirect to the index page
    return HttpResponse('Invalid request method.')

def index(request):
    return render(request, 'index.html')

def save_annotation(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        json_data = json.loads(request.POST.get('json_data'))

        annotated_image = AnnotatedImage.objects.create(image=image, json_data=json_data)
        return JsonResponse({'status': 'success', 'image_id': annotated_image.id})
    return JsonResponse({'status': 'error'}, status=400)
