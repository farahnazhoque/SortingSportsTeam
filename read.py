from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """

    
    names = []

    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                if len(row)!= 3:
                    raise KeyError
                elif row['City'] =="":
                    raise KeyError
                elif row['Team Name'] =="":
                    raise KeyError
                elif row['Sport'] =="":
                    raise KeyError
                    
                
                
                info = (row['City'], row['Team Name'], row['Sport'])
                names.append(info)
            except KeyError:
                raise ValueError

            
                
    # TODO: Complete the function
    return names # erase this


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create
    a list of SportClubs that contain unique SportClubs with their
    corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    p = Path('.')
    plst = list(p.glob('*.csv'))

    goodfiles = 0
    goodlines = 0



    

    lst = []
    errors = []


    for files in plst:
        
        try:
            teams = readFile(files)
            goodfiles +=1
            lst+=teams
        except ValueError:
            errors.append(files)

                
    goodlines=len(lst)
    with open('report.txt', 'w') as report:
        report.write(f'Number of files read: {goodfiles}\n')
        report.write(f'Number of lines read: {goodlines}\n')
    
    for name in errors:
        with open('error_log.txt', 'a+') as error:
            error.write(str(name)+'\n')

    slst=[]
    ulst = list(set(lst))
    for t in ulst:
        s2 = SportClub(t[0], t[1], t[2], lst.count(t))
        slst.append(s2)
    return slst
    # TODO: Complete the function
