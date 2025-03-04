from scripts.getter import get_course_dict
from scripts.search import search
from scripts.utils import CourseIndex, get_user_input
import pickle


def main():
 
    course_dict = dict() 
    input_params = get_user_input()

    print(input_params['savefile'])

    if input_params['savefile']:
        with open(input_params['savefile'], 'rb') as f:
            course_dict = pickle.load(f)
    else:
        courses = ['IE2110', 'IE2107', 'EE2102', 'EE3011', 'EE2073', 'LK5001']
        course_dict = get_course_dict(courses,
                                    acadsem=(input_params['acad_year'], input_params['sem']),
                                    save_output=True)
            
    if input_params['blockout'] is not None:
        course_dict['blockout'] = [input_params['blockout']]

    print(course_dict)

    possible_combinations = search(course_dict)
    print(len(possible_combinations))
    print(possible_combinations[0])

if __name__ == "__main__":
    main()
