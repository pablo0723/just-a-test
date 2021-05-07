from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from component.reminder.models import Reminder
from component.reminder.serializers import ReminderSerializer


class ReminderListCreateView(ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [AllowAny] # Just for fast testing
    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend
    ]
    search_fields = [
        'email',
        'text'
    ]
    ordering_fields = [
        'email'
        'delay'
    ]
    filterset_fields=[
        'email'
    ]


class DeleteReminder(DestroyAPIView):
    queryset = Reminder.objects.all()
    permission_classes = [AllowAny] # Just for fast testing
    serializer_class = ReminderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
