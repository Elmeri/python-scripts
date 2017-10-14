import json
import csv
import sys

output_file = 'output.csv'

def deep_get(dictionary, keys):
    return reduce(lambda d, key: d.get(key, None) if isinstance(d, dict) else None, keys, dictionary)

def parse_args(args_list):
    arguments_list = []
    for argument in args_list:
        splitted = argument.split('.')
        arguments_list.append(splitted)
    return arguments_list

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

args = sys.argv[2:]
args_list = parse_args(args)

columns = []
for d in data["data"]:
    array=[]
    for argument in args_list:
        array.append(deep_get(d, argument))
    columns.append(array)

print "Writing output to {}".format(output_file)

with open(output_file, 'wb') as csvfile:
    devicewriter = csv.writer(csvfile, delimiter='\t')
    for row in columns:
        devicewriter.writerow(row)
