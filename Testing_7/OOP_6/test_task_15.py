import pytest
from OOP_6.task_15 import StudentITM



def test_student_creation_valid():
    student = StudentITM("Основы Python", 50.0, True)
    assert student.current_topic == "Основы Python"
    assert student.learning_progress == 50.0
    assert student.education_status is True


def test_setters_and_getters():
    student = StudentITM("Python", 10.0, True)

    # Смена темы
    student.current_topic = "ООП"
    assert student.current_topic == "ООП"

    # Смена прогресса
    student.learning_progress = 75.5
    assert student.learning_progress == 75.5

    # Смена статуса
    student.education_status = False
    assert student.education_status is False


def test_invalid_current_topic_type():
    with pytest.raises(TypeError):
        StudentITM(123, 10.0, True)

    student = StudentITM("Python", 10.0, True)
    with pytest.raises(TypeError):
        student.current_topic = 42


def test_invalid_learning_progress_type():
    with pytest.raises(TypeError):
        StudentITM("Python", "50%", True)
    with pytest.raises(TypeError):
        StudentITM("Python", True, True)
    with pytest.raises(ValueError):
        StudentITM("Python", 120, True)

    student = StudentITM("Python", 10.0, True)
    with pytest.raises(TypeError):
        student.learning_progress = "30%"
    with pytest.raises(TypeError):
        student.learning_progress = False
    with pytest.raises(ValueError):
        student.learning_progress = -10


def test_invalid_education_status_type():
    with pytest.raises(TypeError):
        StudentITM("Python", 20.0, "Учится")

    student = StudentITM("Python", 10.0, True)
    with pytest.raises(TypeError):
        student.education_status = "отчислен"


def test_str_output():
    student = StudentITM("Git", 30.0, True)
    output = str(student)
    assert "Текущая изучаемая тема: Git" in output
    assert "Прогресс обучения: 30.0" in output
    assert "Статус обучения: True" in output