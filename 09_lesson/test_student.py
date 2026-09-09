import time
from sqlalchemy import select
from models import Student, Subject


def test_add_student(db_session):

    # Добавление студента Марины Шанауровой с уникальным email.

    unique_email = f"marinashanaurova_{int(time.time())}@yandexru"

    new_student = Student(
        name="Марина Шанаурова",
        email=unique_email
    )
    db_session.add(new_student)
    db_session.commit()

    result = db_session.execute(
        select(Student).where(Student.email == unique_email)
    ).scalar_one()

    assert result is not None
    assert result.name == "Марина Шанаурова"


def test_update_subject(db_session):

    # Изменение предмета 'английский язык' на 'китайский язык'.
    # Если предмета нет – создаём его временно.

    subject = db_session.execute(
        select(Subject).where(Subject.name == "English")
    ).scalar_one_or_none()

    if subject is None:
        subject = Subject(name="English", description="Изучение английского")
        db_session.add(subject)
        db_session.commit()

    subject.name = "Chinese"
    db_session.commit()

    updated = db_session.execute(
        select(Subject).where(Subject.id == subject.id)
    ).scalar_one()
    assert updated.name == "Chinese"

    # После теста транзакция откатится – название вернётся обратно


def test_delete_subject(db_session):
    
    # удаление временного предмета.
    
    temp = Subject(name="временный предмет", description="будет удалён")
    db_session.add(temp)
    db_session.commit()

    db_session.delete(temp)
    db_session.commit()

    result = db_session.execute(
        select(Subject).where(Subject.id == temp.id)
    ).scalar_one_or_none()
    assert result is None
