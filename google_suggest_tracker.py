import requests
from bs4 import BeautifulSoup
import json
import sys
import time

def print_banner():
    banner = """
    ====================================================
       Google Auto-Suggest Tracker
       Created By : Python 2.7
    ====================================================
    """
    print banner

def get_suggestions(query):
    url = "https://suggestqueries.google.com/complete/search?client=firefox&q=" + query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print "Error in retrieving data:"+ e
        return None

    suggestions_data = response.json()
    suggestions = suggestions_data[1] 

    return suggestions

def display_suggestions(suggestions):
    if suggestions:
        print "\nGoogle Search Suggestions:"
        for idx, suggestion in enumerate(suggestions, 1):
            print "{}. {}".format(idx, suggestion) 
    else:
        print "No search suggestions found."

def main(query):
    print_banner() 
    suggestions = get_suggestions(query)
    display_suggestions(suggestions)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please enter the keywords you want to track."
        print "Usage: python google_suggest_tracker.py <keyword>"
        sys.exit(1)

    query = sys.argv[1]
    main(query)
