from django.urls import path

from .views import *


urlpatterns = [
    path("cursos/", CourseApiView.as_view(), name='course'),
    path("avaliações/", EvaluationApiView.as_view(), name='evaluation'),
]

