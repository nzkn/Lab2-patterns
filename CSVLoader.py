import random
import string

databases = ['user', 'course']
names = ['Denis', 'Nick', 'Warren', 'Josh', 'Craig', 'Sean', 'Evan', 'Ivan', 'Denis', 'Teo']
course_names = ['Math Basics', 'Python', 'Flutter Mobile Course', 'Android Development', 'Java Junior Dev Course', 'English for rookies', 'Data Science']
course_subjects = ['Programming', 'Math', 'Languages']
course_languages = ['English', 'Ukrainian']


def generate_random_csv(filename='data.cvs', entries_per_db=20):
    user_headers = 'id,email\n'
    data_list = []
    for id in range(1, entries_per_db + 1):
        email = ''.join(random.choices(string.ascii_lowercase + string.digits,
                                       k=random.randint(4, 8))) + '@gmail.com'
        data_list.append(','.join([str(id), email]) + '\n')
    with open(filename, 'w') as file:
        file.write('user\n')
        file.write(user_headers)
        file.writelines(data_list)

    data_list = []
    course_headers = 'id,name,subject,language,author,user\n'

    for id in range(1, entries_per_db + 1):
        name = ''.join(random.choice(course_names))
        subject = ''.join(random.choice(course_subjects))
        language = ''.join(random.choice(course_languages))
        author = random.randint(0, 20)
        user = random.randint(0, 20)
        data_list.append(','.join([str(id), name, subject, language, str(author), str(user)]) + '\n')
    with open(filename, 'a') as file:
        file.write('course\n')
        file.write(course_headers)
        file.writelines(data_list)


def parse_csv(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line[:-1] for line in lines if line.endswith('\n')]

    user_table_idx = lines.index('user')
    user_headers = lines[user_table_idx + 1]
    course_table_idx = lines.index('course')
    course_headers = lines[course_table_idx + 1]
    users_list = lines[user_table_idx + 2: course_table_idx]
    courses_list = lines[course_table_idx + 2:]

    print(user_table_idx)
    print(course_table_idx)
    print('Adding users:')
    print(user_headers)
    print(users_list)
    print('Adding courses:')
    print(course_headers)
    print(courses_list)

    return {
        'user': (user_headers, users_list),
        'course': (course_headers, courses_list),
    }
