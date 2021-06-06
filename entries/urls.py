from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import EntryView, EntryList

urlpatterns = [
    path('list/', EntryList.as_view()),
    path('<int:pk>/', EntryView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
