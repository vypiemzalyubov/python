# 7 kyu
# Naughty or Nice
# 
# Santa is coming to town and he needs your help finding out who's been naughty or nice. You will be given an entire year of JSON data following this format:
# 
# {
#     January: {
#         '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
#     },
#     February: {
#         '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
#     },
#     ...
#     December: {
#         '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
#     }
# }
# 
# Your function should return "Naughty!" or "Nice!" depending on the total number of occurrences in a given year (whichever one is greater). If both are equal, return "Nice!"

def naughty_or_nice(data):
    c = sum([1 if v == 'Nice' else -1 for val in data.values() for v in val.values()])
    return 'Nice!' if c >= 0 else 'Naughty!'



# Best Practices

def naughty_or_nice(data):
    s = str(data)
    return 'Nice!' if s.count('Nice') >= s.count('Naughty') else 'Naughty!'

import json
def naughty_or_nice(data):
    parsed_data = json.dumps(data)
    return "Nice!" if parsed_data.count("Nice") >= parsed_data.count("Naughty") else "Naughty!"