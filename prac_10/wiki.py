"""Wikipedia exercise"""

import wikipedia


# get summary

search_phrase = input("Enter search phrase: ")
while search_phrase != "":
    summary = wikipedia.summary(search_phrase)
    print(summary)
    search_phrase = input("Enter search phrase: ")

# get page

search_phrase = input("Enter search phrase: ")
while search_phrase != "":
    # page = wikipedia.page(search_phrase, auto_suggest=False)
    # print(page.title, page.summary, page.url)
    try:
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(page.title, page.summary, page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("Enter search phrase: ")
