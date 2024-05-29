# views.py
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import AnnotatedImage, Annotation


def photo_list(request):
    annotated_images = AnnotatedImage.objects.all()
    context = {
        'annotated_images': annotated_images
    }
    return render(request, 'photo_list.html', context)

""""@csrf_exempt
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
"""
def index(request):
    return render(request, 'index.html')

def save_annotation(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        json_data = json.loads(request.POST.get('json_data'))

        annotated_image = AnnotatedImage.objects.create(image=image, json_data=json_data)
        return JsonResponse({'status': 'success', 'image_id': annotated_image.id})
    return JsonResponse({'status': 'error'}, status=400)

"""def edit_annotations(request, image_id):
    image_url = get_image_url(image_id)  # Implement this function to get the image URL based on image_id
    annotations = Annotation.objects.filter(image_id=image_id)
    annotations_json = json.dumps([annotation.to_dict() for annotation in annotations])  # Implement to_dict method in Annotation model

    context = {
        'annotations': annotations_json,
        'image_url': image_url,
        'patient_info': {
            'age': '',
            'gender': '',
            'symptoms': ''
        },
        'csrf_token': request.csrf_token
    }
    return render(request, 'edit_annotations.html', context)"""
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

def edit_annotations(request, image_id):
    annotated_image = get_object_or_404(AnnotatedImage, id=image_id)
    context = {
        'image_url': annotated_image.image.url,
        'annotations': json.dumps(annotated_image.json_data['annotations']),
        'patient_info': json.dumps(annotated_image.json_data['patientInfo'])
    }
    return render(request, 'edit_annotations.html', context)