# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
music = {
    "David Bowie" : ["The Rise And Fall Of Ziggy Stardust And The Spiders From Mars","Heroes"],
    "Don McLean" : ["American Pie","Don McLean" , "Chain Lightning"],
    "Pink Floyd" : ["The Wall", "The Dark Side Of The Moon"]
}
# (keys are artist names, values are lists of album names)

# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist
pprint(music["Don McLean"][0])
