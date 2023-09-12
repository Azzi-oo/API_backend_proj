from django.contrib import admin
from django.urls import path
from mainapp import views
from mainapp.consumer import ChatConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.Books_api.as_view(), name='books_api'),
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]
