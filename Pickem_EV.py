import random
import statistics
import numpy as np

class Team:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def __str__(self):
        return str(self.name) + " " + str(self.rating) + " " + str(self.wins)+"-"+str(self.losses)
    



class Tournament:
    def __init__(self,teams):
        self.teams = teams
        for team in self.teams:
            team.wins = 0
            team.losses = 0
        self.threezero = []
        self.through = []
        self.out = []

    def bracket(self):
        #Creates brackets by grouping teams with the same score
        pairs = {}
        for team in self.teams:
            if (team.wins,team.losses) not in pairs.keys():
                pairs[(team.wins,team.losses)] = [team]
            else:
                pairs[(team.wins,team.losses)].append(team)
        return pairs

    def round(self,teams):
        #sort the teams by rating and pair them according to their rating (1st against last 2nd against 2nd last and so on)
        teams.sort(key=lambda team: team.rating)
        for i in range(int(len(teams)/2)):
            self.match(teams[i],teams[-1-i])

    def newround(self):
        #Update teams with teams that are still plaing. Teams with 3 wins or 3 losses are dropped
        newteams = []
        for team in self.teams:
            if team.wins >= 3:
                if team.losses == 0:
                    self.threezero.append(team.name)
                else:
                    self.through.append(team.name)
            elif team.losses >= 3:
                self.out.append(team.name)
            else:
                newteams.append(team)
        self.teams = newteams


    def match(self,team1,team2):
            #Matches two teams against each other. Updates their score.
            prob = 1/(1+10**((team2.rating-team1.rating)/400))
            event = random.uniform(0,1)
            if prob <= event:
                team2.wins += 1
                team1.losses += 1
                
            else:
                team1.wins += 1
                team2.losses += 1

    def result(self):
        #Run the tournament. Return the two teams with 3-0 score and other teams that got through.
        while len(self.teams)>0:
            pairs = self.bracket()
            for b in pairs.values():
                self.round(b)
            self.newround()
        return self.threezero, self.through








if __name__ == "__main__":
    teams = []
    for i in range(16):
        teams.append(Team(i,1200-i*30))

    arr = np.zeros((8,8))
    for i in range(7):
        for j in range(i+1,8):
            # Picks for 3-0
            picks = [i,j]
            
            #Other picks should be all of the 6 best remaining teams
            other = [i for i in range(8) if i not in picks]

            scores = []

            #Run tournament for 1000 times and take average score
            for n in range(1000):
                score = 0
                t = Tournament(teams.copy())
                a,b = t.result()
                for l in picks:
                    if l in a:
                        score += 1
                for l in other:
                    if l in b:
                        score += 1
                    elif l in a:
                        score += 1
                scores.append(score)
            arr[i,j] = statistics.fmean(scores)
    print(arr)
            

    




            
