from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

class CourseApiView(APIView):
    """_summary_
        API de curso
        
    Args:
        APIView (_type_): _description_
    """
    
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class EvaluationApiView(APIView):
    """_summary_
            API de avaliação
    Args:
        APIView (_type_): _description_\\\\\\\\
    """
    
    def get(self, request):
        print(request.user)
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EvaluationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)