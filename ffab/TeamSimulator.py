'''This class performs MonteCarlo team simulation'''

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
        for i in xrange(num_teams):
            team = Team(self.rb_costs, self.wr_costs)
            team.build(num_players, available_cost)

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
        num_players_selected = 0
        while num_players_selected < num_players and available_money > 0:
            available_players = Team.determine_eligible_players(self.rb_costs,
                                                                self.wr_costs,
                                                                available_money)

    def determine_eligible_players(rb_costs, wr_costs, available_money):
        pass
