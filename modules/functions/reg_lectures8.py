from datetime import datetime
from ..db_classes import Lecture, engine, User, get_user, Participant
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, selectinload

Session = sessionmaker(bind=engine)

user = get_user('jason51')


def get_user_reg_lecture(user):

    with Session() as session:
        courses = session.execute(select(Lecture)
                                  .join(Participant)
                                  .where(Participant.user_id == user.id, Lecture.start_at > datetime.now())
                                  ).scalars().all()

    if courses:
        for cur in courses:
            print(f'Laukiam paskaitoje {cur.title}, {cur.start_at}')
    else:
        print('Jūs neturite laukiančių paskaitų')


# courses = get_user_reg_lecture(user)
# if courses:
#     for cur in courses:
#         print(f'Laukia paskaitose {cur.title}')
# else:
#     print('Jūs neturite laukiančių paskaitų')
