from scripts.getter import get_course_dict
from scripts.search import search
from scripts.utils import CourseIndex

def main():

    courses = ['IE2110', 'E2110L', 'IE2107', 'EE2102', 'EE3011', 'E3011L', 'EE2073', 'CM5002']

    course_dict = get_course_dict(courses, save_output=False)
    possible_combinations = search(course_dict)
    for combo in possible_combinations:
        if len(combo) != len(courses):
            print(combo)

if __name__ == "__main__":
    main()