'''This class performs MonteCarlo team simulation'''
import numpy as np

class TeamSimulator(object):
    '''This is the team simulator class
    Inputs:
        rb_costs: rb tier cost dictionary
        wr_costs: wr tier cost dictionary
        rb_busts:  rb bust dictionary
        wr_busts: wr bust dictionary
        rb_weights: list of rb rank weights
        wr_weights: list of wr rank weights
    '''
    def __init__(self, rb_costs, wr_costs, rb_busts,
                 wr_busts, rb_weights, wr_weights):
        self.rb_costs = rb_costs
        self.wr_costs = wr_costs
        self.rb_weights = rb_weights
        self.wr_weights = wr_weights
        self.rb_busts = rb_busts
        self.wr_busts = wr_busts

    def __call__(self, num_teams, num_players, available_cost):
        '''Runs team simulation
        Inputs:
            num_teams: number of iterations to simulate
            num_players: maximum number of players on the team
            available_cost: total cost of the team
        '''
        score_mat = {}
        for i in xrange(num_teams):
            team = Team(self.rb_costs, self.wr_costs)
            players = team.build(num_players, available_cost)
            sc = self.calculate_score(players)
            players.sort()
            score_mat[sc[0]] = players
        scores = score_mat.keys()
        scores.sort()
        scores.reverse()
        for i in xrange(100):
            print ','.join(score_mat[scores[i]]),scores[i]
        return score_mat

    def calculate_score(self, players):
        rb_scores = [0.,0.,0.,0.,0.]
        wr_scores = [0.,0.,0.,0.,0.]
        for p in players:
            s = int(p[2])
            n = p[0:2]
            if n == 'RB':
                sm = self.rb_busts[s]
                for i in xrange(len(rb_scores)):
                    rb_scores[i] += sm[i]
            elif n == 'WR':
                sm = self.wr_busts[s]
                for i in xrange(len(wr_scores)):
                    wr_scores[i] += sm[i]
        score = 0.
        for i in xrange(len(rb_scores)):
            score += rb_scores[i]*self.rb_weights[i]
        for i in xrange(len(wr_scores)):
            score += wr_scores[i]*self.wr_weights[i]
        return score, rb_scores, wr_scores

class Team(object):
    '''This is a specific team
    Inputs:
        rb_costs: cost of the running back tiers
        wr_costs: cost of the wide reciever tiers
        rb_busts: bust rates of running backs by tier
        wr_busts: bust rates of wide receivers by tier
    '''
    def __init__(self, rb_costs, wr_costs):
        self.rb_costs = rb_costs
        self.wr_costs = wr_costs

    def build(self, num_players, available_money):
        '''Builds a team based on the cost, money, and number of players'''
        players = []
        while len(players) < num_players and available_money > 0:
            available_players = Team.determine_eligible_players(self.rb_costs,
                                                                self.wr_costs,
                                                                available_money)
            if len(available_players) == 0:
                print 'Breaking because no players are available'
                break
            r = np.random.randint(0,len(available_players))
            position = available_players[r]
            cost = self.determine_cost(position)
            players.append(position)
            available_money -= cost
        return players

    def determine_cost(self, position):
        cost = None
        if position.startswith('RB'):
            cost = self.rb_costs[int(position[2])]
        elif position.startswith('WR'):
            cost = self.wr_costs[int(position[2])]
        return cost

    @staticmethod
    def determine_eligible_players(rb_costs, wr_costs, available_money):
        '''Takes the cost dictionaries and selects the players available given your money'''
        available_players = []
        for ke in rb_costs.keys():
            v = rb_costs[ke]
            if v <= available_money and ke < 9:
                available_players.append('RB%d' % ke)
        for ke in wr_costs.keys():
            v = wr_costs[ke]
            if v <= available_money and ke < 9:
                available_players.append('WR%d' % ke)
        return available_players
