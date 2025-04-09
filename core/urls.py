from django.urls import path
from core.view import *


urlpatterns = [
    path("cursos/", CoursesAPiView.as_view(), name='courses'),
    path("curso/<int:pk>/", CourseAPiView.as_view(), name='course'),
    
    path("curso/<int:course_pk>/avaliações", EvaluationsApiView.as_view(), name='courses_evaluations'),
    path("curso/<int:course_pk>/avaliação/<int:evaluation_pk>/", EvaluationApiView.as_view(), name='course_evaluation'),
    
    path("avaliações/", EvaluationsApiView.as_view(), name='evaluations'),
    path("avaliação/<int:evaluation_pk>/", EvaluationApiView.as_view(), name='evaluation'),
]
