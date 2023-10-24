# MaskWearing
Correlation between mask-wearing and 2020 presidential election results by state

December 4, 2020
Mask Wearers and Who They Voted For
The program is designed to create a graphical user interface (GUI) window that contains
a grid of buttons, each representing a different state in the United States. Upon clicking one state
button another window is created, giving the percentages and vote counts of both presidential
candidates, showing the winner and loser of the state, along with the results of a New York
Times study on the frequency of mask-wearing in a given state, showing the data that can be
used to make conclusions about the influences of a state’s party leanings and frequency of mask
wearing. Additionally, a button along the top labeled “Map of Winners” will create another
window with a map of the states colored by the winner in each state (red for Trump, blue for
Biden).
To run the program, ensure all three code files (final_window.py, final_map.py,
final_state.py) are downloaded and saved to the same location, as well as the two text files
(maskresults.txt, electionresults.txt). Open and run the final_window.py, and a GUI window will
pop up. From there, to view the results of a state, simply press the button of the given state and a
new window with that state’s data will appear. Additionally, the electoral victory map can be
viewed by pressing the button “Map of Winners.” Doing so will create another new window with
a map of the states colored by the winner of the election. If this window is open, in order to view
the data for another state, the map window must first be closed before a state button can be
pressed.

YouTube demo: https://youtu.be/tEOtgLW0qAM

Reflection:
1. In creating the project, I learned about other libraries in Python, specifically the Cartopy
library. Originally, the plan was to use the Basemap library, as that had been the library I
had researched, however, after I learned Basemap was discontinued, I had to readjust and
learn how to work with Cartopy. There was a lot of difficulty in simply downloading the
library as it required several other libraries that also had to be downloaded. The original
idea was to create an interactive map that when a state was clicked, created a pop-up
window with the information on that state, however, I quickly found out that Cartopy
does not have the capability of creating an interactive map. I had also planned to use
what I knew from statistics to list the correlation between mask-wearing and the winner
in an individual state, but there was not enough data to calculate the correlation, as that
requires a full set of data, more than just one pair, so I had to move away from that idea.
2. I learned more about the Cartopy library which was difficult to figure out when 
downloading. Once downloaded, I used and built off example code from Stack Overflow
to create the map. I also had to do some research on how to create buttons in a GUI
window, with assigned functions, and arrange them into a grid, the information I learned from
Real Python. I struggled a lot with the libraries and learning to download them, and also
struggled a little with the GUI window, but once I had learned, implementing it was
relatively simple and satisfying.
3. Note on Senior Capstone: Don’t forget to plan out the project step by step and remember
to pick a topic that really interests you, and not something you think other people want to
see, because if you’re not interested in the topic you will not want to work on it.
