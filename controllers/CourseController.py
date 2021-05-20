class CourseController:
    def __init__(self, course_manager, user_manager):
        self.course_manager = course_manager
        self.user_manager = user_manager

    def get_course(self, course_id):
        return self.course_manager.get_course(course_id)

    def get_all_courses(self):
        return self.course_manager.get_all_courses()

    def add_course(self, name, subject, language, author):
        return self.course_manager.add_course(name, subject, language, author)

    def remove_course(self, course_id):
        return self.course_manager.remove_course(course_id)

    def get_all_users(self):
        return self.user_manager.get_all_users()

    def enroll_to_course(self, user, subject):
        return self.user_manager.enroll_to_course(user, subject)

    def finish_course(self, user, course):
        return self.finish_course(user, course)
