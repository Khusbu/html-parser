# HTML parser

Parser for parsing court cases html files. It either takes a directory path or a file path as input and prints all the data parsed in structured format i.e. json. In case of a directory path, it loops over all the files present in that directory and outputs data from each file whereas in case of a file path it outputs data of the input file only.

# Input format
Refer to file [sample.html](https://github.com/Khusbu/html-parser/blob/master/sample.html) as sample input

# Output format
Outputs parsed data in JSON format.

## Dependencies

- Python 2.7.10
- Python Library - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Usage

```
python html_parser.py [directory_path|file_path]
```

For example,
```
python html_parser.py sample.html
```
