from rest_framework import serializers

class DailyThoughtsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length= 100)
    content = serializers.CharField(max_length=1000)
