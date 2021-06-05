from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import EntryView

urlpatterns = [
    path('entries/', EntryView.as_view()),
    path('entries/<int:pk>/', EntryView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
