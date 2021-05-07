from rest_framework import serializers

from component.reminder.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = [
            'id',
            'text',
            'delay',
            'email'
        ]
