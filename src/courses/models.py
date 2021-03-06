from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify

class Subject(models.Model):
    """
    Table to represent subjects - a course category.
    
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
    Table to represent courses
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
    Table to represent modules
    """
    course = models.ForeignKey(Course, 
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    discription = models.TextField(blank=True)
    
    def __str__(self):
        return self.title


class Content(models.Model):
    """
    Table to represent contents
    """
    module = models.ForeignKey(Module, 
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                      on_delete=models.CASCADE,
                                      limit_choices_to={'model__in':(
                                          'text',
                                          'video',
                                          'image',
                                          'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    
    
class ItemBase(models.Model):
    """
    Abstract table to represent different type items
    """
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.CASCADE,
                              related_name='%(class)s_related')
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title
    
    
class Text(ItemBase):
    """
    Table to represent item in type of text
    """
    content = models.TextField()
    
    
class File(ItemBase):
    """
    Table to represent item in type of file
    """
    file = models.FileField(upload_to='files')
    

class Image(ItemBase):
    """
    Table to represent item in type of image
    """
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    """
    Table to represent item in type of video
    """
    url = models.URLField()
