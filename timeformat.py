def formatted_time(elapsed_time):

    hours_elapsed = elapsed_time / 3600
    mins_elapsed = ((elapsed_time % 3600) / 60)
    seconds_elapsed = ((elapsed_time % 3600) % 60)

    if hours_elapsed < 10:
        hours_elapsed = "0" + str(int(hours_elapsed))

    if mins_elapsed < 10:
        mins_elapsed = "0" + str(int(mins_elapsed))

    if seconds_elapsed < 10:
        seconds_elapsed = "0" + str(int(seconds_elapsed))

    time = (str(hours_elapsed) + ":" + str(mins_elapsed)) + ":" + str(seconds_elapsed)

    return time


