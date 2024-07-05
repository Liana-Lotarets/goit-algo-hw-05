import re

# Create decorator for checking format of log.
def error_format_of_log(fun):
    def inner(line: str):
        match = re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ((INFO)|(ERROR)|(DEBUG)|(WARNING)) .+$', line)
        if match:
            return fun(line)
        else:
            print(f'Incorrect format of logfile: {line.strip()}')
            return None
    return inner

# Convert log line into a dictionary.
@error_format_of_log
def parse_log_line(line: str) -> dict:
    keys = ('date','time','logging_level','message')
    values = tuple(line.split(maxsplit=3))
    log_dict = {key: value for key, value in zip(keys, values)}
    return log_dict

# Open logfile and return its lines in the form of dictionary.
def load_logs(file_path: str) -> list[dict]:
    with open(file_path, 'r', encoding='utf-8') as log_file:
            lines = [parse_log_line(line) for line in log_file.readlines() if parse_log_line(line)]
    return lines

# Filter logs by level.
def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
     list_logs_by_level = [log for log in logs if log['logging_level'] == level]
     return list_logs_by_level

# Count logs by level.
def count_logs_by_level(logs: list[dict]) -> dict[int]:
    keys = ('INFO','ERROR','DEBUG','WARNING')
    values = tuple([len(filter_logs_by_level(logs,key)) for key in keys])
    dict_count_logs = {key: value for key, value in zip(keys, values)}
    return dict_count_logs

# Print table "Logging level & Quantity".
def display_log_counts(counts: dict[int]):
    # width of the first column = 15, 
    # width of the second_column = 10
    display = ' Logging level | Quantity \n'\
        + '-'*15 + '|' + '-'*10 + '\n'
    for key, value in zip(counts.keys(),counts.values()):
        display += ' ' + key + ' '*(15-len(key)-1) +'|' + ' ' + str(value) + '\n'
    print(display)

# Print details of log by the level.
def display_details_of_log_by_level(logs: list[dict], level: str):
    list_logs_by_level = filter_logs_by_level(logs, level)
    if list_logs_by_level == []:
        print(f'Such level {level} does not exist.')
    else:
        print(f'Details of logs for level {level}: ')
        for log in list_logs_by_level:
            print(' '.join(log.values()).strip())


