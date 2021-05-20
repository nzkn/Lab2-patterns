from models.Course import Course


class CourseManager:
    def __init__(self, session):
        self.session = session

    def get_all_courses(self):
        return self.session.query(Course).all()

    def get_course(self, course_id):
        return self.session.query(Course).filter(
            Course.id == course_id).one_or_none()

    def add_course(self, name, subject, language, author):
        course = Course()
        course.name = name
        course.subject = subject
        course.language = language
        course.author = author
        self.session.add(course)

    def remove_course(self, course_id):
        course = self.get_course(course_id)
        if course:
            self.session.delete(course)

    def add_course_from_csv(self, course_headers, course_data):
        course = Course()
        course.from_csv(course_headers, course_data)
        self.session.add(course)
