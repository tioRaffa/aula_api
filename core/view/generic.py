from rest_framework import generics

from core.models import Course, Evaluation
from core.serializers import CourseSerializer, EvaluationSerializer
from django.shortcuts import get_object_or_404


class CourseAPiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

class CoursesAPiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
    
# Avaliação
class EvaluationApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    lookup_url_kwarg = 'evaluation_pk'
    
    def get_object(self):
        if 'course_pk' in self.kwargs:
            return get_object_or_404(
                self.get_queryset(),
                course_id=self.kwargs.get('course_pk'),
                pk=self.kwargs.get('evaluation_pk')
            )

# AVALIAÇOESS
class EvaluationsApiView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    
    def get_queryset(self):
        if 'course_pk' in self.kwargs:
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        
        return self.queryset.all()

     