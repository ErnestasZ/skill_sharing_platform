from faker import Faker
from constant import DEFAULT_PASSWORD, DB_ADDRESS
import bcrypt
import random
from datetime import datetime, time, timedelta
from sqlalchemy import create_engine, insert, select
from sqlalchemy.orm import sessionmaker
import db_classes as sql


salt = bcrypt.gensalt()
fake = Faker()

engine = create_engine(DB_ADDRESS)
Session = sessionmaker(bind=engine)


def create_users(number):
    # users = []

    with Session() as session:
        for _ in range(number):
            user = sql.User(
                first_name=fake.name(),
                last_name=fake.name(),
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                password=bcrypt.hashpw(DEFAULT_PASSWORD.encode(), salt)
            )

            skill = create_skill()
            user.skills.append(skill)
            session.add(user)
            session.commit()
            print(user.id, skill.id)
            # return
            lecture = create_lecture(skill)
            session.add(lecture)
            session.commit()

    # return users


def create_skill():
    skills = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'SQL', 'NoSQL', 'AI', 'ML', 'Data Science',
              'UX/UI Design', 'UX/UI Development', 'Frontend Development', 'Backend Development', 'Full Stack Development']
    # user_double_skills = random.sample(skills, 2)

    return sql.Skill(title=random.choice(skills), description=fake.paragraph(nb_sentences=3))
    # user['skills'] = [
    #     skill for skill in skills if fake.random.choice([True, False])]
    # return user


def create_lecture(skill):
    formats = [
        "Mastering {}: From Basics to Advanced Techniques",
        "{} Essentials: Building Interactive Applications",
        "{} Programming: Best Practices and Design Patterns",
        "{} for Beginners: Your First Steps in Development",
        "A Hands-On Approach to {}",
        "{} Deep Dive: Efficient Management and Querying",
        "{}: Principles and Applications",
        "Creating User-Centric Digital Experiences in {}",
        "Crafting Dynamic User Interfaces with {}",
        "Building Robust Server-Side Applications with {}",
        "Exploring the World of {}: Techniques and Tools",
        "Advanced Concepts in {}: A Comprehensive Guide",
        "Practical Applications of {} in Real-World Projects",
        "Innovations in {}: Trends and Future Directions",
        "Getting Started with {}: Your Roadmap to Success"
    ]

    lectures_title = random.choice(formats).format(skill.title)

    start_date_str = '2024-10-01'
    end_date_str = '2024-12-01'
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    generate_date = fake.date_between_dates(start_date, end_date)
    final_start_at = datetime.combine(generate_date, time(9, 0))

    return sql.Lecture(
        skill_id=skill.id,
        user_id=skill.user_id,
        title=lectures_title,
        description=fake.paragraph(nb_sentences=3),
        start_at=final_start_at,
        end_at=final_start_at + timedelta(hours=random.randint(1, 4))
    )


def create_participants(number):
    # participants = []
    with Session() as session:
        for _ in range(number):
            users = session.execute(select(sql.User)).scalars().all()
            user = random.choice(users)
            lectures = session.execute(select(sql.Lecture).where(
                sql.Lecture.user_id != user.id)).scalars().all()
            lecture = random.choice(lectures)

            if lecture.end_at < datetime.now():
                completed = False
                rating = False
            else:
                completed = True
                rating = True

            participan = sql.Participant(
                user_id=user.id,
                lecture_id=lecture.id,
                is_complete=completed,
                lecture_rating=rating,
                subscribed_at=lecture.start_at -
                timedelta(days=random.randint(1, 3))
            )
            session.add(participan)
            session.commit()
            # sql.Participant(user_id=user.id, lecture_id=lecture.id)
            # )

# create_users(5)


def fill_db():
    create_users(15)
    create_participants(10)


fill_db()
