import factory
from django.contrib.auth import get_user_model
from faker import Faker

from .courses.models import (Content, Course, File, Image, ItemBase, Module,
                            Subject, Text, Video)

fake = Faker()
User = get_user_model()

class UserStudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = fake.email()
    password = factory.PostGenerationMethodCall(
        'set_password', 'StudentPass1!')
    is_student = True
    
    
class UserTeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = fake.email()
    password = factory.PostGenerationMethodCall(
        'set_password', 'TeacherPass1!')
    is_teacher = True
    
    
class SubjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subject
    
    title = fake.word()
    
    
class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course
        
    owner = factory.SubFactory(UserTeacherFactory)
    subject = factory.SubFactory(SubjectFactory)
    title = fake.word()
    overview = fake.paragraph(nb_sentences=3)
    
    
class ModuleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Module
        
    course = factory.SubFactory(CourseFactory)
    title = fake.word()
    

