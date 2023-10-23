from django.urls import path
from pinterest_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('account/login/',login_view,name='account_login'),
    path('',views.index, name="index"),
    path('create_idea_pin/',views.create_idea_pin, name="create_idea_pin"),
    path('pin_sayfa/<int:pk>',views.pin_sayfa, name="pin_sayfa"),
    path('profile/<int:pk>',views.profile, name="profile"),
    path('indir/<int:pk>', views.indir, name='indir'),
    path('comment/',views.comments,name='comment'),
   # path('blur/<int:pk>',views.blur,name="blur"),
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

