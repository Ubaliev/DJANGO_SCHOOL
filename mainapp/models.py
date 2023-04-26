from django.db import models

class School(models.Model):
    name = models.CharField(max_length=127)
    number = models.PositiveBigIntegerField(default=1)
    address = models.CharField(max_length=127)

    class Meta:
        verbose_name = 'школа'
        verbose_name_plural = 'школы'

    def __str__(self):
        return f'школа {self.name} номер {self.number}'

    @property
    def clas_amount(self):
        return self.classes.count()
    

class Clas(models.Model):
    room_number = models.PositiveBigIntegerField(default=1)
    teacher_name = models.PositiveBigIntegerField(default=1)
    student_amount = models.PositiveIntegerField(default=1)
    grade = models.CharField(max_length=127)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE,
        related_name='classes'
        )

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        
        def __str__(self):
            return f'{self.grade} класс в школе {self.school.number}'

    @property
    def student_amount(self):
        return self.students.count()
    
class Student(models.Model):
    name = models.CharField(max_length=127)
    age = models.PositiveBigIntegerField(default=1)
    grade = models.CharField(max_length=127)
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE, 
    related_name='students', null=True)
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'имя {self.name} возраст {self.age} Класс {self.grade}'
    