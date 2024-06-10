from rest_framework import serializers
from todo.models import ToDo
from todo.constants import (
    STATUS_CHOICES,
    COLOR_CHOICES,
    PRIORITY_CHOICES
)

# ordinary serializer
class ToDoSerializer(serializers.Serializer):
    id  = serializers.IntegerField(read_only=True) # read_only and write_only
    scheduled_at = serializers.DateTimeField(required=False)
    duration = serializers.IntegerField()
    status = serializers.ChoiceField(choices=STATUS_CHOICES, default='notstarted')
    title = serializers.CharField(max_length=200)
    color = serializers.ChoiceField(choices=COLOR_CHOICES, default='black')
    priority = serializers.ChoiceField(choices=PRIORITY_CHOICES, default='low')

    def create(self, validated_data: dict):
        """ Create and return a new 'ToDo' item , given some info"""
        todo_item = ToDo.objects.create(**validated_data)
        # check for the alternative
        return todo_item
    
    def update(self, instance, data: dict):
        instance.duration = data.get('duration', instance.duration)
        instance.status = data.get('status', instance.status)
        instance.title = data.get('title', instance.title)
        instance.color = data.get('color', instance.color)
        instance.priority = data.get('priority', instance.priority)
        instance.scheduled_at = data.get('scheduled_at', instance.scheduled_at)
        instance.save()
        return instance
    
    def to_internal_value(self, data:dict):
        print(data, "Hey i got this from the browser")
        return super().to_internal_value(data)
    
    def to_representation(self, instance):
        # do anything you want to
        return super().to_representation(instance)
    
    def validate_duration(self, value):
        if value < 0 :
            raise serializers.ValidationError("invalid duration value")
        return value
    
    def validate(self, data: dict):
        if data['duration'] < 0:
            raise serializers.ValidationError("invalid duration value")
        return data
    

class ToDoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
    # authentications and Permissions