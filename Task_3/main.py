from functions import *

def main():
    user_input = input('Enter path to logfile and, if desired, logging level: ')
    # Parse the string entered by the user into path_to_logfile and optional argument.
    path_to_logfile, *arg = user_input.split()
    # Check if the path exists.
    # If the path exists, then create list of dictionaries
    # consisting information about each log.
    try:
        logs_list = load_logs(path_to_logfile)
    except FileNotFoundError as excpt:
        print(f'Sorry, but {excpt}')
    else:
        # Count logs by level and print table.
        counts_dict = count_logs_by_level(logs_list)
        display_log_counts(counts_dict)
        # If there is an optional argument,
        # then display details of logs by level. 
        if arg:
            display_details_of_log_by_level(logs_list, arg[0].upper())
    


if __name__ == '__main__':
    main()

# python Task_3\main.py E:/Repository/goit-algo-hw-05/Task_3/logfile.log