import json
import os
import sys
from bs4 import BeautifulSoup
import components

# parse_html parses html file f and returns a json output
def parse_html(f):
    soup = BeautifulSoup(f.read(), "html.parser")
    fields = {}

    # Case Details
    fields['case_details'] = components.parse_case_details(soup)

    # Case Status
    fields['case_status'] = components.parse_case_status(soup)

    # Petitioner and Advocate
    fields['petitoner_and_advocate'] = components.parse_petitoner_and_advocate(soup)

    # Respondent and Advocate
    fields['respondent_and_advocate'] = components.parse_respondent_and_advocate(soup)

    # Acts
    fields['acts'] = components.parse_acts_table(soup)

    # History of Case Hearing
    fields['history'] = components.parse_history_table(soup)

    # Orders
    fields['orders'] = components.parse_orders_table(soup)

    return json.dumps(fields, indent=4)

# parse_file opens a file stored at filepath
def parse_file(filepath):
    file_descriptor = open(filepath,"r")
    print "Output: ", parse_html(file_descriptor)

# loop_over_files loops over all the files present in the directory
def loop_over_files(directory):
    for filename in os.listdir(directory):
        try :
            parse_file(directory+'/'+filename)
        except Exception as e:
            print "parse_html() Exception: ", e

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
        if os.path.isfile(arg):
            parse_file(arg)
        else:
            loop_over_files(arg)
    except Exception as e:
        print "usage: python html_parser.py [directory_path|file_path]"
