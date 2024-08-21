# courses/views.py

from rest_framework import generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Course Views
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseInstanceListCreate(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        queryset = CourseInstance.objects.all()
        year = self.request.query_params.get('year')
        semester = self.request.query_params.get('semester')
        course = self.request.query_params.get('course')

        if year is not None:
            queryset = queryset.filter(year=year)
        if semester is not None:
            queryset = queryset.filter(semester=semester)
        if course is not None:
            queryset = queryset.filter(course__id=course)

        return queryset


class CourseInstanceDetail(generics.RetrieveDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

class CourseInstanceByYearSemester(generics.ListAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)
