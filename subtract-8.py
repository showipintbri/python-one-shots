'''Script for reading a HTML file with embedded CSS and,
   moving each item up 8px and over 8px for proper alignment.'''
import re

# Open the file and read all the lines into a list.
with open("test_css.html", "rt") as html:
  content = html.readlines()

# Itterate over the list. 
for i in range(0,len(content)):
  x = re.search("\s+top:\s(\d+)px;", content[i]) # Find the lines with "  top: 000px"
  y = re.search("\s+left:\s(\d+)px;", content[i]) # Find the lines with "  left: 000px"
  if x: 
    num = x.group(1) # Pull out only the number from the match
    newnum = str(int(num) - 8) # Subtract 8 from the number
    z = re.sub(num, newnum, x.group(0)) # Rebuild the entire line replacing the values.
    content[i] = z # Replace this list index with the new line.
    print(content[i]) # Print output so I can copy from stdout
  elif y: # Same process as above
    num = y.group(1)
    newnum = str(int(num) - 8)
    z = re.sub(num, newnum, y.group(0))
    content[i] = z
    print(content[i])
  else:
    print(content[i].rstrip()) # If no matches were found, print to stdout so I can copy complete output from stdout
