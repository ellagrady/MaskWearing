# data sets pulled from :
# masks data: https://www.kaggle.com/paultimothymooney/nytimes-covid19-data
# election data: https://www.nytimes.com/interactive/2020/11/03/us/elections/results-president.html?action=click&module=Spotlight&pgtype=Homepage&action=click&module=Spotlight&pgtype=Homepage 

import math

class State:

    
    
    def process_file(self, filename):
        """ proccess file"""

        
        file1 = open(filename) 

        file_list = []
        for line in file1:
            section_line = line.strip()
            section_strings = section_line.split(',') # Split the line on runs of whitespace
            strings = [str(n) for n in section_strings] # Convert to strings
            file_list.append(strings) # Add the "row" to your list.


        file1.close()
  
        return file_list


    def state_winner(self, state):
        """ finds and returns winner from given state """

        election_list = self.process_file('electionresults.txt')

        for row in range(len(election_list)):
            if election_list[row][0]== state:
                return election_list[row][1]

    def state_loser(self, state):
        """ finds and returns loser from given state """

        election_list = self.process_file('electionresults.txt')

        for row in range(len(election_list)):
            if election_list[row][0]== state:
                return election_list[row][4]

    def state_count(self, state, candidate):
        """ finds and returns vote count for given state and candidate """

        election_list = self.process_file('electionresults.txt')

        for row in range(len(election_list)):
            for col in range(len(election_list[0])):
                if election_list[row][0]== state:
                    if election_list[row][col] == candidate:
                        return election_list[row][col+1]

    def state_percentage(self, state, candidate):
        """ finds and returns vote percentage for given state and candidate """
        
        election_list = self.process_file('electionresults.txt')

        for row in range(len(election_list)):
            for col in range(len(election_list[0])):
                if election_list[row][0]== state:
                    if election_list[row][col] == candidate:
                        return election_list[row][col+2]

    def vote_margin(self, state):
        """ determines the vote margin for the given state """
        

        winner = self.state_winner(state)
        loser = self.state_loser(state)

        winner_votes = int(self.state_count(state, winner))
        loser_votes = int(self.state_count(state, loser))
        margin = winner_votes - loser_votes
        
        return '+' + str(margin)

    def party(self, candidate):
        """ returns the party for given candidate """
        if candidate == 'Biden':
            party = 'Democrat'
        else:
            party = 'Republican'

        return party


    def national_winner(self):
        """ finds and returns the national winner """
        
        election_list = self.process_file('electionresults.txt')

        trump = 0
        biden = 0
        uncounted = 0

        for row in range(len(election_list)):
            if election_list[row][1] == 'Trump':
                trump += 1
            elif election_list[row][1] == 'Biden':
                biden += 1   
            else:
                uncounted += 1

        winner = max(trump, biden, uncounted)
        return winner

    def mask_wearing(self, state):
        """ finds and returns the percentages of mask 
        wearing in given state """

        mask = self.process_file('maskresults.txt')

        
        for row in range(len(mask)):
            if mask[row][0] == state:
                return mask[row]



    def print_winner(self, state):
        """prints winner's results for given state """

        winner = self.state_winner(state)
        winner_count = self.state_count(state, winner)
        winner_percent = self.state_percentage(state, winner)
        winner_party = self.party(winner)
        margin = self.vote_margin(state)
        
        winner = str('WINNER: '+ winner + '\n') + str('PARTY: ' + winner_party +'\n') + str('VOTES: ' + winner_count + '\n') + str('PERCENT OF VOTES: ' +  winner_percent + '\n') + str('MARGIN OF VICTORY: ' + margin)
        return str(winner)


    def print_loser(self, state):
        """prints loser's results for given state """

        loser = self.state_loser(state)
        loser_count = self.state_count(state, loser)
        loser_percent = self.state_percentage(state, loser)
        loser_party = self.party(loser)
        loser = str('LOSER: ' + loser + '\n') + str('PARTY: ' + loser_party + '\n') +  str('VOTES: ' + loser_count + '\n') + str('PERCENT OF VOTES: ' + loser_percent)
        return str(loser)


    def print_masks(self, state):
        """prints mask results for given state """

        masks = self.mask_wearing(state)
        masks = str('FREQUENCY OF MASK WEARING'+ '\n') + str('NEVER: '+ masks[1] + '\n') + str('RARELY: ' + masks[2] + '\n') + str('SOMETIMES: ' + masks[3] + '\n') + str('FREQUENTLY: ' + masks[4] + '\n') + str('ALWAYS: ' + masks[5])
        return str(masks)


