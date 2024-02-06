###########################################################################################
# Dupchu Wangmo
# Software Eng
# 02230282
############################################################################################
# References
# https://chat.openai.com/c/95935b8f-9556-46b3-98fa-1af0f3c2064a
# 


############################################################################################
# Solution
# Task 1: There were 20000 people assigned and there are 6452 of overlapping space assignments
# Task 2: There are 2427 of overlapping space assignments in the same line
# 

# Read the input.txt file

def count_all_overlaps(lines):
    total_overlaps = 0
    total_complete_overlaps = 0
    total_people = len(lines) * 2 
    for line in lines:
        spaces = line.split(' ')
        for i in range(len(spaces)):
            for j in range(i+1, len(spaces)):
                space1 = spaces[i].replace(',', '')
                space2 = spaces[j].replace(',', '')
                if '-' in space1:
                    start1, end1 = map(int, space1.split('-'))
                else:
                    start1 = end1 = int(space1)
                if '-' in space2:
                    start2, end2 = map(int, space2.split('-'))
                else:
                    start2 = end2 = int(space2)
                # Check for total overlaps
                if max(start1, start2) <= min(end1, end2):
                    total_overlaps += 1
                # Check for complete overlaps
                if start1 <= start2 and end1 >= end2:
                    total_complete_overlaps += 1
    return total_overlaps, total_complete_overlaps, total_people

file_path = '/home/blackmoon/Desktop/CSF/RA CAP 2/input_2_cap2.txt' 

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        overlaps, complete_overlaps, people = count_all_overlaps(lines)
        print(f"There were {people} people assigned and there are {overlaps} of overlapping space assignments")
        print(f"There are {complete_overlaps} of overlapping space assignments in the same line")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
