# import os
# print(os.getcwd())
# usefull piece of code to find out what's the workign directory

def read_logs(filename):

    logs = {}
    
    with open(filename, "r") as file:  # open(filename, "r" (read mode))
                                       #    to open the file safely.
                                       # The open ... as file: guarantees the
                                       #    file is closed.
        
        for line in file:  # a file object is iterable and each iteration gives
                           #    you the string of each line including \n
        
            time_str, error = line.strip().split()  # line.strip() removes
                                                    #    leading and trailing
                                                    #    whitespace and \n.
                                                    # .split() splits the
                                                    #    string on any
                                                    #    whitespace and returns
                                                    #    a list of words.
            logs[time_str] = error
        
    return logs

def most_common_error(logs, start_time, end_time):

    counts = {}  # dictionary to store the error type as key, and the
                 #    frequence as value

    for time in logs:  # iterate over all the dictonaries values.
        if start_time <= time <= end_time:  # Chained comparison that works
                                            #    because python compares one
                                            #    character at a time
            error = logs[time]
            counts[error] = counts.get(error, 0) + 1  # default to 0

    if not counts:  # in case there are no errors logged inside that time frame
        return None
    
    max_error = None
    max_count = 0

    for error in counts:
        if counts[error] > max_count:
            max_error = error
            max_count = counts[error]

    return max_error, max_count

address = ("/home/lumaenaut/repos/portfolio/hyperskill/12_days_of_coding_2025"
    "/day_one/hyperskill-dataset-119011485.txt")

start_time = "15:00"
end_time = "15:30"

logs = read_logs(address)

print(most_common_error(logs, start_time, end_time))