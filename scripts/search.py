from .utils import CourseIndex


def search(course_dict: dict) -> list:
    """Function that does a search for possible combination of course indexes.

    Args:
        course_dict (dict): Dictionary containing details of all the courses as lists of CourseIndex objects

    Returns:
        index_combo_list (list): List of possible combinations
    """
    course_indexes = list(course_dict.values())
    n_courses = len(course_indexes)

    valid_combos = []
    stack = [[]]

    while stack:
        curr_combo = stack.pop()

        if len(curr_combo) == n_courses:
            valid_combos.append(curr_combo)
        else:
            for course_index in course_indexes[len(curr_combo)]:
                if not course_index.check_clash(curr_combo):
                    stack.append(curr_combo + [course_index])

    return valid_combos

