from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
  type = serializers.CharField(max_length=1000, required=True)

  def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
    return Todo.objects.create(**validated_data)

  def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
    instance.type = validated_data.get('type', instance.type)
    instance.result = validated_data.get('result', instance.result)
    instance.status = validated_data.get('status', instance.status)
    instance.timeout = validated_data.get('timeout', instance.timeout)
    
    instance.save()
    return instance

  class Meta:
    model = Todo
    fields = '__all__'
