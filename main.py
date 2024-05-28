from scripts.getter import get_course_dict
from scripts.search import search
from scripts.utils import CourseIndex

def main():

    courses = ['EE2102', 'EE2073', 'IE2107', 'IE2110']

    course_dict = get_course_dict(courses, save_output=False)
    possible_combinations = search(course_dict)

if __name__ == "__main__":
    main()