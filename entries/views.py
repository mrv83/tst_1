from django.db.models import Count
from django.http import Http404
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Entry, Statistic
from .serializers import EntrySerializer, StatisticSerializer


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.groups.filter(name__in=['Manager', 'Supervisor']).exists():
            return qs
        return qs.filter(user=self.request.user)


class EntryView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            obj = Entry.objects.get(pk=pk)
            if obj.user == self.request.user or \
                    self.request.user.groups.filter(name__in=['Manager', 'Supervisor']).exists():
                return obj
            raise Http404
        except Entry.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = EntrySerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = EntrySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StatisticView(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.groups.filter(name__in=['Manager', 'Supervisor']).exists():
            return qs
        year = self.request.query_params.get('year')
        return qs.filter(user=self.request.user, year=year)


class YearsView(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if self.request.user.groups.filter(name__in=['Manager', 'Supervisor']).exists():
            user = request.GET.get('user') or self.request.user.pk
        else:
            user = self.request.user.pk
        qs = Statistic.objects.filter(user=user).values('year').order_by('year').annotate(count=Count('year'))
        return Response({'years': [y['year'] for y in qs]})
