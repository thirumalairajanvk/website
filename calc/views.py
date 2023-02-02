# views.py
import PIL 
from django.shortcuts import render
from PIL import Image
from django.http import HttpResponse

def compress_image(input_image, quality):
    input_image.save("compressed.jpeg", "JPEG", quality=quality)
    return Image.open("compressed.jpeg")

def index(request):
    if request.method == 'POST':
        input_image = Image.open(request.FILES['input_image'])
        quality = int(request.POST['quality'])
        output_image = compress_image(input_image, quality)
        response = HttpResponse(content_type="image/jpeg")
        output_image.save(response, "JPEG")
        return response
    return render(request, 'index.html')