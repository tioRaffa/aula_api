from django.urls import path
from core.view import *


urlpatterns = [
    path("cursos/", CoursesAPiView.as_view(), name='courses'),
    path("curso/<int:pk>/", CourseAPiView.as_view(), name='course'),
    path("cursos/<int:course_pk>/avaliações", CoursesAPiView.as_view(), name='courses_evaluation'),
    path("curso/<int:course_pk>/avaliação/<int:evaluation_pk", CoursesAPiView.as_view(), name='courses_evaluation'),
    
    path("avaliações/", EvaluationsApiView.as_view(), name='evaluations'),
    path("avaliação/<int:pk>/", EvaluationApiView.as_view(), name='evaluation'),
]
