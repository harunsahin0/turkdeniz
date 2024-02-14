from django.urls import path
from . import views

urlpatterns = [
    path('',views.anasayfa, name='anasayfa'),
    path('anasayfa/', views.anasayfa, name='anasayfa'),
    path('hakkinda/', views.hakkinda, name='hakkinda'),
    path('amacvekapsam/', views.amacvekapsam, name='amacvekapsam'),
    path('kunye/', views.kunye, name='kunye'),
    path('kurullar/', views.kurullar, name='kurullar'),
    path('yayinpolitikasi/', views.yayinpolistikasi, name='yayinpolitikasi'),
    path('etik/', views.etik, name='etik'),
    path('iletisim/', views.iletisim, name='iletisim'),
    
]
