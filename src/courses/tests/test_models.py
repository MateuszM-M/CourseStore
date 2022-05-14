import pytest

from courses.models import Subject, Course, Module


def test_subject_str(db, subject1):
    assert subject1.__str__() == subject1.title
    

def test_courses_str(db, course1):
    assert course1.__str__() == course1.title
    

def test_module_str(db, module1):
    assert module1.__str__() == module1.title