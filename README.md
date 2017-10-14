# python-scripts

Useful python scripts for various things.

Currently contains:
1. JSON to CSV parser


## JSON to CSV parser

How to use:
Takes 2-n arguments, first being the input file name and rest being keys to extract from the document. Nested keys can be used with separating the keys with a dot `.` . Output is a csv file with n columns and m rows where n is number of arguments given and m number of entries in the json file.

Example:
```python parse_json_to_csv.py input.json example_key nested_key_1.nested_key_2```
