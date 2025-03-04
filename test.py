from scripts.utils import CourseIndex


c1 = CourseIndex(
    course_code='test1',
    index=1,
    timeslots=[(1, '1630', '1750', {1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}), (1, '1630', '1750', {3}), (3, '1330', '1450', {3}), (3, '1330', '1450', {1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}), (4, '0930', '1220', {9, 12, 6})]
)

c2 = CourseIndex(
    course_code='test2',
    index=2,
    timeslots=[('2', '0930', '1000', {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}), ('4', '0930', '1000', {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13})]
)

c3 = CourseIndex(
    course_code='test3',
    index=3,
    timeslots=[]
)

print(c2.check_clash([c1]))