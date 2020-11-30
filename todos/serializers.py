from rest_framework import serializers

from todos.constants import STATUS_CHOICES


class TodoSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200, read_only=True)
    name = serializers.CharField(max_length=200)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    due_date = serializers.DateTimeField()
