
from django.urls import path
from .views import FileUploadView, GetJWTTokenView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('api/token/', GetJWTTokenView.as_view(), name='token'),
]
    