from dataclasses import dataclass

@dataclass
class CourseIndex:
    """Class for storing info of a tutorial index.
    
    Args:
        index: Index number of the tutorial
        timeslots: list of tuples of the form (day, start time, end time, weeks)
    """
    course_code: str
    index: int
    timeslots: list[tuple]
    
    def check_clash(self, index_list: list) -> bool:
        """Function checking if this tutorial index clashes with another tutorial index.
        
        Args:
            other: CourseIndex object to compare to

        Returns:
            True if there is clash, False otherwise
        """
        # if index_list is empty, return False
        if len(index_list) == 0:
            return False
        
        # iterate through all the indexes in the index list
        for other_index in index_list:
            # Iterate over each timeslot in this index and check if it clashes with any timeslot in the other index
            for timeslot1 in self.timeslots:
                for timeslot2 in other_index.timeslots:
                    if (timeslot1[0] == timeslot2[0]                      # Check if days match
                        and timeslot1[1] <= timeslot2[1] <= timeslot1[2]  # Check if time overlap
                        and timeslot1[3].intersection(timeslot2[3])       # Check if weeks overlap
                        ):
                        return True
        return False

def parse_weeks(weeks_str: str) -> set[int]:
    """Helper function to parse the teaching week string into individual weeks.

    Args:
        weeks_str (str): String from the dataframe containing the weeks

    Returns:
        weeks_list (list): List of weeks as integers
    """
    weeks_str_list = weeks_str.split(',')
    
    weeks_list = list()
    for item in weeks_str_list:
        if '-' in item:
            week_range = item.split('-')
            weeks_list.extend([i for i in range(int(week_range[0]), int(week_range[1])+1)])
        else:
            weeks_list.append(int(item))

    return set(weeks_list)