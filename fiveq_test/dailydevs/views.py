# Python imports
import datetime
import HTMLParser
# Django imports
from django.shortcuts import render
# Local imports
from dailydevs.models import Devotion


def count_words(text):
    """
    Given a properly marked-up HTML text, calculate the number of words.
    """
    # 'words' begins with 1, so the last in the devotion is counted.
    words = 1
    special = 0
    special_chars = ''
    for char in text:
        # Add 1 to 'words' for each ' ' (space).
        if char == ' ':
            words += 1
        # Look for the beginning of the '<p></p>' html pattern.
        if char == '<':
            special_chars = char
            special += 1
        # Add characters to test against the '<p></p>' html pattern.
        if special > 0:
            special_chars += char
            special += 1
        #
        if special == 7:
            # Add 1 to 'words' if the special_chars string matches
            #  the html pattern '<p></p>'.
            if special_chars == '<p></p>':
                words += 1
                special = 0
                special_chars = ''
            # Reset tracking variables if there is no match.
            else:
                special = 0
                special_chars = ''
    return words

def display_devotion(request, input_date):
    """
    Present a devotion from the Devotion table of the datdjango-taggit==0.10a1abase
      to the user for the date they choose.
    """
    date_list = input_date.split('-')
    request_date = datetime.datetime(
        int(date_list[0]),
        int(date_list[1]),
        int(date_list[2])
    )
    devotion = Devotion.objects.get(date=request_date)

    # Convert html entities into html markup.
    html_parser = HTMLParser.HTMLParser()
    unescaped_text = html_parser.unescape(devotion.body)

    # Fetch word count.
    words = count_words(unescaped_text)

    tv = {
        'devotion': devotion,
        'text': unescaped_text,
        'words': words
    }
    return render(request, 'display_devotion.html', tv)
