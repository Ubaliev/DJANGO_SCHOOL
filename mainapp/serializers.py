from rest_framework import serializers

from mainapp.models import(
    School, Clas, Student,

)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id', 'name', 'age', 'grade', 'clas'
        )

class ClasSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True)
    class Meta:
        model = Clas
        fields = ('student_amount',
            'id', 'room_number', 'teacher_name', 'room_number', 'student_amount',
            'grade', 'school', 'students',
        )


class SchoolSerializer(serializers.ModelSerializer):
    classes = ClasSerializer(read_only=True, many=True)
    class Meta:
        model = School
        fields = ('clas_amount',
            'id', 'name', 'number', 'address', 'classes',
        )