# views.py
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import AnnotatedImage, Annotation


def photo_list(request):
    # Funkcja zwracająca listę wszystkich zdjęć wraz z ich adnotacjami.
    annotated_images = AnnotatedImage.objects.all()
    context = {
        'annotated_images': annotated_images
    }
    return render(request, 'photo_list.html', context)


def index(request):
    # Funkcja renderująca stronę główną aplikacji.
    return render(request, 'index.html')

def save_annotation(request):
    # Funkcja obsługująca zapisywanie nowych adnotacji dla obrazu.
    if request.method == 'POST':
        image = request.FILES.get('image')
        json_data = json.loads(request.POST.get('json_data'))

        annotated_image = AnnotatedImage.objects.create(image=image, json_data=json_data)
        return JsonResponse({'status': 'success', 'image_id': annotated_image.id})
    return JsonResponse({'status': 'error'}, status=400)


@csrf_exempt
def upload_annotations(request):
    # Funkcja obsługująca przesyłanie adnotacji dla istniejących lub nowych obrazów.
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_file = request.FILES.get('imageFile')
        json_data = json.loads(request.POST.get('jsonFile'))

        if image_id:
            # Aktualizujemy istniejący obraz.
            annotated_image = get_object_or_404(AnnotatedImage, id=image_id)
            if image_file:
                annotated_image.image = image_file
            annotated_image.json_data = json_data
            annotated_image.save()
        else:
            # Tworzymy nowy obraz.
            annotated_image = AnnotatedImage(image=image_file, json_data=json_data)
            annotated_image.save()

        return redirect('photo_list')

    return render(request, 'upload_annotations.html')

def edit_annotations(request, image_id):
    # Funkcja renderująca formularz edycji adnotacji dla danego obrazu.
    annotated_image = get_object_or_404(AnnotatedImage, id=image_id)
    context = {
        'annotated_image': annotated_image,
        'image_url': annotated_image.image.url,
        'annotations': json.dumps(annotated_image.json_data['annotations']),
        'patient_info': json.dumps(annotated_image.json_data['patientInfo'])
    }
    return render(request, 'edit_annotations.html', context)
