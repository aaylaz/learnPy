from datetime import datetime, timedelta
import calendar


def meetup_date(year, month, nth=-1, weekday=3):
    """
    returns the workday specified as a datetime object
    """
    # get last day of the month
    last_day_of_month = calendar.monthrange(year, month)[1]

    # create string from input
    if len(str(month)) == 1:
        month = '0' + str(month)
    start_date_string = str(year) + '-' + str(month) + '-01'
    end_date_string = str(year) + '-' + str(month) + '-' + str(last_day_of_month)

    # create datetime object
    my_date = datetime.strptime(start_date_string, "%Y-%m-%d")
    my_end_date = datetime.strptime(end_date_string, "%Y-%m-%d")
    one_day = timedelta(days=1)

    # if counting from the end of the month
    last_day_count = last_day_of_month
    day_count = 0
    if nth < 0:
        while last_day_count > 0:
            last_day_count -= 1
            if my_end_date.weekday() == weekday:
                return (datetime.date(my_end_date))
            my_end_date = my_end_date - one_day


    # Search for the specific day
    for day in range(1, last_day_of_month + 1):
        if my_date.weekday() == weekday:
                day_count += 1
        if (day_count == nth):
            return (datetime.date(my_date))
        my_date = my_date + one_day


print(meetup_date(2020, 1, nth=4, weekday=4))