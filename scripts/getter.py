import bs4 as bs
import requests
import pandas as pd
import pickle
from io import StringIO
from .utils import CourseIndex, parse_weeks

url = 'https://wish.wis.ntu.edu.sg/webexe/owa/AUS_SCHEDULE.main_display1'

def get_course_dict(course_codes: list, save_output: bool = True) -> dict:
    """Function that scrapes course site for course details and extracts it to a dictionary.

    Args:
        course_codes (list): List of course codes
        save_output (bool): Whether to save the output as a pickle file

    Returns:
        course_dict (dict): Dictionary containing course details
    """

    course_dict = {}
    for course_code in course_codes:

        print(f"Getting course info for {course_code}...")

        request_params = {
            'staff_access': 'false',
            'acadsem': '2024;1',
            'r_search_type': 'F',
            'boption': 'Search',
            'r_subj_code': course_code
            }

        # send scraping request
        source = requests.get(url, request_params)
        soup = bs.BeautifulSoup(source.text, 'lxml')

        # convert table to pandas DataFrame
        course_df = pd.read_html(StringIO(soup.prettify()))[1]

        n_indexes = course_df['INDEX'].count()
        print(f"Found {n_indexes} indexes for {course_code}\n")
        row_interval = len(course_df) // n_indexes

        course_dict[course_code] = list()
        
        for idx in range(0, len(course_df), row_interval):
            course_index_df = course_df.iloc[idx:idx+row_interval,:]

            course_index_number = int(course_index_df.iat[0,0])

            course_timings_df = course_index_df[['DAY', 'TIME',  'REMARK']]

            timeslots = list()
            for row in course_timings_df.itertuples(index=False):

                start_time, end_time = row.TIME.split('-')
                weeks = parse_weeks(row.REMARK.lstrip('Teaching Wk') if type(row.REMARK) == 'str' else '1-13')
                day_map = {'MON': 0, 'TUE': 1, 'WED': 2, 'THU': 3, 'FRI': 4, 'SAT': 5}
                timeslots.append((day_map[row.DAY], start_time, end_time, weeks))

            course_dict[course_code].append(CourseIndex(course_code=course_code, index=course_index_number, timeslots=timeslots))

    if save_output:
        filename = '-'.join(course_codes) + ".pkl"
        print(f"Writing to pickle file {filename}")
        with open(filename, 'wb') as f:
            pickle.dump(course_dict, f, pickle.HIGHEST_PROTOCOL)

    return course_dict