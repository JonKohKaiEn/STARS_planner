from dataclasses import dataclass

@dataclass
class CourseIndex:
    """Class for storing info of a tutorial index.
    
    Args:
        index: Index number of the tutorial
        timeslots: Set containing tuples of (day, start time, end time, week) for lectures
    """
    index: int
    timeslots: set[tuple]
    
    def check_clash(self, other) -> bool:
        """Function checking if this tutorial index clashes with another tutorial index.
        
        Args:
            other: CourseIndex object to compare to

        Returns:
            boolean indicating whether there is a clash
        """
        return not self.timeslots.isdisjoint(other.timeslots)
    

def parse_weeks(weeks_str: str) -> list[int]:
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

    return weeks_list