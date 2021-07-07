import argparse
import csv
from dateutil import parser as date_parser
from datetime import datetime
from pytz import timezone
import pytz

my_timezone = timezone('US/Pacific')


def main(csv_file):
    f = open(csv_file, 'r')
    reader = csv.reader(f)
    headers = next(reader, None)

    column = {}
    for h in headers:
        column[h] = []

    for row in reader:
        for h, v in zip(headers, row):
            column[h].append(v)

    utc_hdr = headers[0]
    utc_col = column[utc_hdr]

    pst_col = []

    for utc in utc_col:
        date = date_parser.parse(utc)
        date = my_timezone.localize(date)
        date = date.astimezone(my_timezone)

        # print 'Local date & time is  :', date.strftime(date_format)
        pst_col.append(date)

    print('done.')


if __name__ == "__main__":
    # execute only if run as a script

    parser = argparse.ArgumentParser(description='Process electric usage.')
    parser.add_argument('-c', '--csv', help='CSV file to parse')

    args = parser.parse_args()
    main(args.csv)
