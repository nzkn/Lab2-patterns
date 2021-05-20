from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import CSVLoader
from controllers.CourseController import CourseController
from controllers.ImportController import ImportController
from managers.CourseManager import CourseManager
from managers.UserManager import UserManager
from models.Base import Base

DB_PATH = 'D:/Politech/Patterns/lab2/lab.db'


def main():
    print('MAIN:')
    engine = create_engine('sqlite:///' + DB_PATH)
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        course_manager = CourseManager(session)
        user_manager = UserManager(session)

        course_controller = CourseController(
            course_manager=course_manager,
            user_manager=user_manager,
        )

        # AppView(course_controller)

        import_controller = ImportController(
            course_manager=course_manager,
            user_manager=user_manager,
        )

        # CSVLoader.generate_random_csv()
        # CSVLoader.parse_csv('data.cvs')

        import_controller.load_data_from_csv('data.cvs')
        session.commit()

        print('\nCOURSES:')
        for course in course_controller.get_all_courses()[:5]:
            print(course)
        print('\nUSERS:')
        for user in user_manager.get_all_users()[:5]:
            print(user)


if __name__ == '__main__':
    main()
