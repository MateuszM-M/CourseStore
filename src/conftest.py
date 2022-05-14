import pytest

from pytest_factoryboy import register
from .factories import (UserStudentFactory, UserTeacherFactory, SubjectFactory,
                       CourseFactory, ModuleFactory
                       )


register(UserStudentFactory)
register(UserTeacherFactory)
register(SubjectFactory)
register(CourseFactory)
register(ModuleFactory)


@pytest.fixture
def student1(db, user_student_factory):
    student = user_student_factory.create()
    return student

@pytest.fixture
def teacher1(db, user_teacher_factory):
    teacher = user_teacher_factory.create()
    return teacher

@pytest.fixture
def subject1(db, subject_factory):
    subject = subject_factory.create()
    return subject

@pytest.fixture
def course1(db, course_factory):
    course = course_factory.create()
    return course

@pytest.fixture
def module1(db, module_factory):
    module = module_factory.create()
    return module