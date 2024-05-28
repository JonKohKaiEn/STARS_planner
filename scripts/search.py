from .utils import CourseIndex

def search(course_dict: dict) -> list:
    """Function that does a search for possible combination of course indexes.

    Args:
        course_dict (dict): Dictionary containing details of all the courses as lists of CourseIndex objects

    Returns:
        index_combo_list (list): List of possible combinations
    """

    index_combo_list = []
    curr_combo_list = []
    curr_idx_list = [0 for _ in range(len(course_dict))]
    combined_timings_set = set()

    for course_code in course_dict:
        # TODO: Finish this function