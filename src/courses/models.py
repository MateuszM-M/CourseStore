from django.db import models
from django.contrib.auth import get_user_model


class Subject(models.Model):
    """
    DB to represent subject - a course category.
    
    Attributes
    ----------
    title : title of subject
    slug : slug of subject
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        
    def __str__(self):
        return self.title


class Course(models.Model):
    """
    DB to represent course
    """
    owner = models.ForeignKey(get_user_model(),
                              related_name='course_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.title
    

class Module(models.Model):
    """
    DB to represent module
    """
    course = models.ForeignKey(Course, 
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    discription = models.TextField(blank=True)
    
    def __str__(self):
        return self.title