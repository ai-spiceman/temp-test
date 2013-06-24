=============
==temp-test==
=============

I developed this app on Windows 8 using Python 2.7.4.

See the requirements.txt file for pip-installable required packages.

Use: python manage.py import_devs <optional four-digit year>
  to import the data. The data is expected to be in the:
  'dailydevs/management/commmands' directory.
  I committed a copy to source for your convenience.

Add some tags, if you would like to see them display below the horizontal
  rule at the bottom of the page when viewing a devotion.

Word counts are also displayed under the horizontal rule.

Use: localhost:port/devotion/2013-11-01/
  to view the web page (using the appropriate host, port and date, of course).

My Experience
=============
During my initial, official 90-minute test period, I first tackled:
    - Postgres database setup
    - basic project and app starts
    - initial adjustments to the settings file
    - Devotion model
    - admin.py
    - management command to import the data

I hit two snags that crippled me as my panic grew (as mozilla says,
  'Well, this is embarrassing'):
    - The Admin wouldn't display, because I failed to 'syncdb' - I didn't
    recognize the error I was getting and wasn't coming up with the right
    answer on Google, because I hadn't made that particular mistake before.
    After you permitted me additional time, John asked to see my pgAdmin III
    and asked, "Where are your tables?" and that was all I needed on that one.
    - My management command was giving me the error, 'too many values to
    unpack' (but no line number). I thought this had to do with args being
    passed into the command and was looking for the wrong solution. Again,
    after you permitted me additional time, John asked me to move a set_trace
    I had in the code up near the top. When I did this and ran the code again,
    I saw that the problem was with csv.reader and not the args_list as I
    had imagined.

The Extended Time Period
========================
    Just a Note: John gave me no direct assistance during this period,
    beyond what is mentioned above. He did answer the question of whether
    he thought my effort on the tagging constitued incorporation in the
    affirmative and whether he thought a JSON fixture was needed in the
    negative.

    The four data issues I encountered were fun to solve.

    The first, involving the initial space (that gave me 30 strings,
    instead of the 4 I was expecting) took me the longest. I kept
    chasing after quote settings, instead of following an early instinct
    that that space after the comma looked problematic. I even noticed the
    'skipinitialspace' parameter in the python docs, but was chasing the
    quote settings at the time. When I finally read about someone's
    experience with a similar problem on stackoverflow.com,
    I could've kicked myself!

    The second, involving the missing year, I solved by allowing the
    user to supply a year with the management command or using the
    current year otherwise. Validation assures that user input is
    between the years 2000 and the current year.

    The third, involving month '22', I solved with some data validation
    code in the import command. I could have raised an exception and
    halted execution, but that would have resulted in partially imported
    data, so I chose the 'insist on good data' path.

    The fourth, involving correct output of the devotion body text took
    a bit of hunting as django filters were not doing the trick
    for me. I tried a number things using django.utils.html and
    django.utils.safestring, but to no avail. It was stackoverflow.com
    that again provided me with an introduction to HTMLParser from the
    core python library that solved my problem.

    The word count was easily solved with a django template filter, but
    since you specifically asked for a view, I wrote some python to do
    the calculation, as well (I'm sure it could be refactored into a better
    form). I displayed both in the template to compare results.

Conclusion
==========
    Thanks again for the grace you've shown me. I look forward to your
    comments on Wednesday.
