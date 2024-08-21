# courses/urls.py

from django.urls import path
from .views import (
    CourseListCreate, CourseDetail,
    CourseInstanceListCreate, CourseInstanceDetail,
    CourseInstanceByYearSemester
)

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('instances/', CourseInstanceListCreate.as_view(), name='course-instance-list-create'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceByYearSemester.as_view(), name='course-instance-by-year-semester'),
    path('instances/<int:pk>/', CourseInstanceDetail.as_view(), name='course-instance-detail'),
]
