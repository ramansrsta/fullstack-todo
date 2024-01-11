from rest_framework import serializers
from .models import Student

def name_starts_with_l(value):
    if value[0].lower() != 'l':
        raise serializers.ValidationError('Name Should Start With l')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[name_starts_with_l])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Is Full')
        return value

    def validate(self,data):
        nm = data.get('name')
        if nm.lower() != 'luffy':
            raise serializers.ValidationError('Name Must Be Luffy')
        return data
