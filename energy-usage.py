import argparse
import csv
from dateutil import parser as date_parser
from datetime import datetime
from pytz import timezone
import pytz

TIMEZONE_UTC = timezone('UTC')
TIMEZONE_PST = timezone('US/Pacific')


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

    date_col = []
    time_col = []

    for utc in utc_col:
        date_raw = date_parser.parse(utc)
        date_utc = TIMEZONE_UTC.localize(date_raw)
        date_pst = date_utc.astimezone(TIMEZONE_PST)
        date_str = str(date_pst.date())
        time_str = str(date_pst.time())

        date_col.append(date_str)
        time_col.append(time_str)

    print('done.')


if __name__ == "__main__":
    # execute only if run as a script

    parser = argparse.ArgumentParser(description='Process electric usage.')
    parser.add_argument('-c', '--csv', help='CSV file to parse')

    args = parser.parse_args()
    main(args.csv)
