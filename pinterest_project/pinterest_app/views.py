from django.shortcuts import render,redirect
from pinterest_app.models import İmage, Profile, Comment
from pinterest_app.forms import İmageForm,EditForm,CommentForm
from django.shortcuts import render, get_object_or_404
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.conf import settings
import os



#def login_view(request):
 #   return render(request, 'account_login')

def index(request):
    images=İmage.objects.all()
    context={
        'images1':images
    }
    return render(request,"index.html",context)

def create_idea_pin(request):
    return render(request,"create_idea_pin.html")

def pin_sayfa(request,pk):
    images=İmage.objects.get(id=pk)
    comments=Comment.objects.filter(post=pk)

    context={
        'resim':images,
        'comments1':comments,
    }
    return render(request,"pin_sayfa.html",context)

def profile(request,pk):
    profile=Profile.objects.get(id=pk)

    context={
        'sayfa':profile,
    }
    return render(request,"profile.html",context)

def indir(request,pk):
    images=İmage.objects.get(id=pk)
    file_path = os.path.join(f'media/{images.image}')  # Dosya yolunu belirtin
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image')
        response['Content-Disposition'] = 'attachment; filename=deneme.png'
        return response
   
def comments(request):
    comments = Comment.objects.all()

    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(content=comment)
        return redirect('comments')

    return render(request, 'comment.html', {'comments': comments})

# def blur(request, pk):
#     image = İmage.objects.get(id=pk)
#     style = '<style>.blurred-image { filter: blur(5px); }</style>'
#     content = f'<img src="{{ resim.image.url }}" alt="Image" class="blurred-image">'
#     return HttpResponse(f'{style}{content}')

# def blur(request, pk):
#     image = İmage.objects.get(id=pk)
#     return render(request, 'blur.html', {'image': image})
