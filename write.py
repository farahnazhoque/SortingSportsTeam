import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"),
    SportClub("LA", "Angels", "MLB")],
    return the iterable [
    [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")],
    [SportClub("LA", "Angels", "MLB")]
    ]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    # TODO: Complete the function
    sportNames = []
    for sport in all_clubs:
        s = sport.getSport()
        sportNames.append(s)

    sportNames = set(sportNames)
    a = {}

    for names in sportNames:
        for sport in all_clubs:
            if names not in a:
                a[names] = list()
            if sport.getSport() == names:
                a[names].append(sport)

    a = list(a.values())
    return a 

    
        
def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80),
    SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130),
    SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport


    Returns:
        A sorted list of the SportClubs  
    """
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    a = sorted(sport, key=lambda s: s.name)
    a.reverse()
    a = sorted(a, key=lambda s: s.count)
    a.reverse()
    
    return a  # erase this


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current
    working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked"
    for the top 3 teams in each sport.

    Args:
        sorted_sports:
        an Iterable of different sports,
        each already sorted correctly
    """
    
    # TODO: Complete the function
    with open('survey_database.csv', 'w', newline='') as sportCSV:
        writing = csv.writer(sportCSV)

        writing.writerow(['City', 'Team Name', 'Sport', 'Number of Times Picked'])

        for sports in sorted_sports:
            count=0
            for sport in sports:
                writing.writerow([sport.getCity(), sport.getName(), sport.getSport(), sport.count])
                count+=1
                if count==3:
                    break
