import csv
import os
import re


#Creates a filter for csv's files in all the subdirectories whose 6th column (
# excluding the # header) contains a floating point number


float_matcher = re.compile("[ ]*[+-]?([0-9]*[.])[0-9]+.*")

for path, subdirsm, files in os.walk(".."):
    for name in files:
        if name.endswith(".csv"):

            with open(os.path.join(path, name), 'r') as f:
                reader = csv.reader(f, delimiter=',')
                next(reader, None)
                for row in reader:
                    if len(row) > 4:
                        csv_matcher = float_matcher.match(row[5])
                        if csv_matcher:
                            print(os.path.join(path, name))
                            print(row[5])

                    break #break after reading the first line
