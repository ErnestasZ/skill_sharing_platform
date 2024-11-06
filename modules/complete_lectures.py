from datetime import datetime
from db_classes import Lecture, engine, User, get_user, Participant
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, selectinload

Session = sessionmaker(bind=engine)

user = get_user('jason51')


def get_user_compl_lecture(user):
    with Session() as session:
        courses = session.execute(select(Participant)
                                  .join(Lecture)
                                  .options(selectinload(Participant.lecture))
                                  .where(Participant.user_id == user.id, Lecture.end_at < datetime.now())
                                  ).scalars().all()

    if not courses:
        print('Kursuose dar nedalyvavai !')

    completed = [cur for cur in courses if cur.is_complete]
    uncompleted = [cur for cur in courses if not cur.is_complete]

    for comp in completed:
        print(f'Pabigtos paskaitos {comp.lecture.title} ')

    for unc in uncompleted:
        print(f'Nepabaigtos paskaitos {unc.lecture.title}')


get_user_compl_lecture(user)
# if courses:
#     for cur in courses:
#         print(f'Pabigtos paskaitose {cur.lecture.title}, {cur.is_complete} ')
# else:
#     print('Jūs neturite laukiančių paskaitų')
