# backend/views.py
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def try_on(request):
    if request.method == 'POST':
        try:
            # Get clothing image and avatar image from request.FILES
            clothing_image = request.FILES['clothing_image']
            avatar_image = request.FILES['avatar_image']

            # Prepare the payload for the Texel API
            payload = {
                'clothing_image': clothing_image.read(),
                'avatar_image': avatar_image.read(),
            }

            # Prepare headers
            headers = {
                'content-type': 'multipart/form-data; boundary=---011000010111000001101001',
                'X-RapidAPI-Key': '4560fcf1fdmshd302dcd512c9f67p1858cfjsn0545fd5c08b0',
                'X-RapidAPI-Host': 'texel-virtual-try-on.p.rapidapi.com',
            }

            # Make the request to the Texel API
            response = requests.post('https://texel-virtual-try-on.p.rapidapi.com/try-on-file', files=payload, headers=headers)

            # Return the Texel API response as JSON
            return JsonResponse(response.json(), status=response.status_code)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
