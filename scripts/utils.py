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
    timeslots: set[tuple]
    
    def check_clash(self, index_list: list) -> bool:
        """Function checking if this tutorial index clashes with another tutorial index.

        Args:
            index_list: list of CourseIndex objects to compare to

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
                    if (timeslot1[0] == timeslot2[0]  # Check if days match
                        and ((timeslot1[1] <= timeslot2[1] <= timeslot1[2]) or (timeslot2[1] <= timeslot1[1] <= timeslot2[2]))  # Check if time overlap
                        and timeslot1[3].intersection(timeslot2[3])  # Check if weeks overlap
                        ):
                        return True
        return False


def parse_weeks(weeks_str: str) -> set[int]:
    """Helper function to parse the teaching week string into individual weeks.

    Args:
        weeks_str: String from the dataframe containing the weeks

    Returns:
        weeks_list: Set of weeks as integers
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


def get_user_input() -> dict:
    output = {
        'savefile': "",
        'acad_year': "",
        'sem': "",
        'blockout': None
    }
    output['savefile'] = input("Input file path of savefile (leave blank if not specified): ")
    if output['savefile'] == '':
        output['acad_year'] = input("Academic Year (XXXX): ")
        output['sem'] = input("Semester (1/2): ")

    timeslots = []
    while True:
        if input("Do you want to add a blockout period? (y/n): ").lower() == 'n':
            break
        blockout_day = input("Input blockout period day (0: Monday, 1: Tuesday etc.): ")
        blockout_period = input("Input blockout timing: ").split('-')
        timeslots.append((blockout_day, blockout_period[0], blockout_period[1], set([i for i in range(1, 14)])))
    
    output['blockout'] = CourseIndex(
        course_code='blockout',
        index=0,
        timeslots=timeslots,
    )

    return output
