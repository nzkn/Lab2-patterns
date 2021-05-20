import CSVLoader


class ImportController:
    def __init__(self, course_manager, user_manager):
        self.course_manager = course_manager
        self.user_manager = user_manager

    def load_data_from_csv(self, filename):
        parsed_csv = CSVLoader.parse_csv(filename)
        user_headers, user_datalist = parsed_csv['user']
        course_headers, course_datalist = parsed_csv['course']
        for user_data in user_datalist:
            print('Loading user')
            print(user_data)
            self.user_manager.add_user_from_csv(user_headers, user_data)
        for course_data in course_datalist:
            print('Loading course')
            print(course_data)
            self.course_manager.add_course_from_csv(course_headers, course_data)
