from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name' , 'roll', 'city']
        # both are ways to make fields read only
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {
        #     'name' : {"read_only" : True}
        # }

    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Is Full')
        return value

    def validate(self, data):
        nm = data.get('name')
        print(nm)
        if nm.lower() == 'luffy':
            raise serializers.ValidationError('Name Cannot Be Luffy')
        return data
            



