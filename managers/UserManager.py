from models.Course import Course
from models.User import User


class UserManager:
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        return self.session.query(User).all()

    def enroll_to_course(self, user, subject):
        course = self.session.query(Course).filter(
            Course.subject == subject).one_or_none()
        print(course)
        if course:
            user.courses = user.courses.append(course)

    def finish_course(self, user, course):
        if course.id:
            current_course = self.session.query(Course).filter(
                Course.id == course.id).one_or_none()
            if current_course:
                user.finished_courses = user.finished_courses.append(course)
                user.courses = user.courses.remove(course)

    def add_user_from_csv(self, user_headers, user_data):
        user = User()
        user.from_csv(user_headers, user_data)
        self.session.add(user)
