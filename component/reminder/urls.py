from django.urls import path

from component.reminder.views import ReminderListCreateView, DeleteReminder

urlpatterns = [
    path(r'all/', ReminderListCreateView.as_view(), name='reminder-list-create'),
    path(r'delete/<int:id>/', DeleteReminder.as_view(), name='board-rud')
]
