# Python imports
import csv
import datetime
# Django imports
from django.conf import settings
from django.core.management.base import BaseCommand
# Local imports
from dailydevs.models import Devotion


class Command(BaseCommand):
    """
    Populates the Devotion table from a file in CSV format file.

    import_devs takes an optional four-digit year:
        python manage.py import_devs [four-digit year]
    """
    args = '<year>'
    help = (
        'Imports daily devotions from a CSV file\n'
        '  into the Devotion table of the database.\n\n'
        'arguments\n'
        '   year: 2012 (yyyy)'
    )

    def handle(self, *args, **options):
        args_list = list(args)
        # Verify first argument is a valid integer;
        #  otherwise replace with the current year.
        try:
            year = int(args_list[0])
        except:
            year = datetime.datetime.today().year
        # Verify that the year is within the range 2000 to current year;
        #  otherwise except new input from the user.
        valid_year = False
        while not valid_year:
            if year > datetime.datetime.today().year or year < 2000:
                text = ('Error: Year must be between 2000 and %d'
                    % datetime.datetime.today().year)
                data = 'Year provided was: %d' % year
                year = int(
                    raw_input("%s\n%s\nEnter the year: " % (text, data))
                )
            else:
                valid_year = True
        # Absolute filepath of the input CSV file.
        filename = '%sprogramming-sample.tab' % settings.IMPORT_ROOT
        # Read CSV into a variable. Skip initial spaces in the data file.
        with open(filename, 'rb') as csvfile:
            devotions = csv.reader(csvfile, skipinitialspace=True)
            steps = 1
            for title, month, day, body in devotions:
                # Skip the first line of the input file
                #  if csv.Sniffer determines that they are headers.
                sniff = csv.Sniffer()
                if steps == 1:
                    if sniff.has_header(filename):
                        steps += 1
                        continue
                # Validation for month and day data.
                valid_date = False
                while not valid_date:
                    try:
                        date = datetime.date(int(year), int(month), int(day))
                        valid_date = True
                    except ValueError as ve:
                        if 'month' in ve.message:
                            devo = 'For the devotion titled: "%s",' % title
                            data = 'the month provided was: "%s".' % month
                            month = raw_input(
                                "Error: %s\n%s %s\nEnter a valid month: "
                                % (ve, devo, data)
                            )
                        if 'day' in ve.message:
                            devo = 'For the devotion titled: "%s",' % title
                            data = 'the day provided was: "%s"' % day
                            day = raw_input(
                                "Error: %s\n%s %s\nEnter a valid day: "
                                % (ve, devo, data)
                            )
                # Populate an instance of Devotion and save to the database.
                dev = Devotion()
                dev.title = title
                dev.date = date
                dev.body = body
                dev.save()
