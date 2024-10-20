from .utils import CourseIndex

def search(course_dict: dict) -> list:
    """Function that does a search for possible combination of course indexes.

    Args:
        course_dict (dict): Dictionary containing details of all the courses as lists of CourseIndex objects

    Returns:
        index_combo_list (list): List of possible combinations
    """
    course_indexes = list(course_dict.values())
    
    def recursive_search(curr_index_combo: list[CourseIndex], course_index_list: list[list[CourseIndex]]) -> list[list]:
        """Function that is recursively called to search for possible combinations of index combinations

        Args:
            course_index_list (list): Nested list of CourseIndex objects

        Returns:
            index_combo_list (list): List of possible combinations
        """

        index_combos = []
        
        # base case: if there is only one course left
        if len(course_index_list) == 1:
            for index in course_index_list[0]:
                if not index.check_clash(curr_index_combo):
                    index_combos.append(curr_index_combo + [index])
            return index_combos
        
        # recursive case
        else:
            for index in course_index_list[0]:
                if not index.check_clash(curr_index_combo):
                    index_combos.extend(recursive_search(curr_index_combo + [index], course_index_list[1:]))
            return index_combos
        
    return recursive_search([], course_indexes)