#!/usr/bin/env python
'''This is the main function for the fantasy football bust rate calculator'''
import os
import argparse
import numpy as np
import sys
from ffab import Utils, TeamSimulator

def parse_position_function(func_string):
    '''Returns the function used to calculate positional auction cost'''
    if func_string == 'mean':
        return np.mean
    elif func_string == 'median':
        return np.median
    elif func_string == 'max':
        return max
    elif func_string == 'min':
        return min
    else:
        print '%s is not a valid averaging function. Exitting.' % func_string
        sys.exit(1)

def parse_args():
    '''Parses the arguments to this script'''
    parser = argparse.ArgumentParser(description='Fantasy Football Auction Bust Rate')
    parser.add_argument('--rb-auction-file',
                        help='CSV file containing running back auction values (required)',
                        type=str, required=True)
    parser.add_argument('--rb-cost-column',
                        help='Column in RB csv file containing RB auction cost(default 4)',
                        type=int, required=False, default=4)
    parser.add_argument('--rb-rank-column',
                        help='Column in RB csv file containing RB rank (default 6)',
                        type=int, required=False, default=6)
    parser.add_argument('--rb-bust-rates', required=True, help='RB Bust rate file')
    parser.add_argument('--wr-auction-file',
                        help='CSV file containing wide receiver auction values (required)',
                        type=str, required=True)
    parser.add_argument('--wr-cost-column',
                        help='Column in WR csv file containing WR auction cost(default 3)',
                        type=int, required=False, default=3)
    parser.add_argument('--wr-rank-column',
                        help='Column in WR csv file containing WR rank (default 5)',
                        type=int, required=False, default=5)
    parser.add_argument('--wr-bust-rates', required=True, help='WR Bust rate file (required)')
    parser.add_argument('--qb-te-d-k-cost', help='Total cost spent on QB, TE, D, and K (default 4)',
                        type=int, required=False, default=4)
    parser.add_argument('--total-auction-cost',
                        help='Total money available for auction (default 100)',
                        type=int, required=False, default=100)
    parser.add_argument('--position-value-function',
                        help='Function to calculate auction position cost (mean, median, max, min)',
                        type=str, required=False, default='median')
    parser.add_argument('--num-draft-picks', help='Maximum number of picks to make (default 11)',
                        type=int, required=False, default=11)
    parser.add_argument('--num-teams', help='Number of random teams to build (default 1000)',
                        type=int, required=False, default=1000)
    parser.add_argument('--rb-weights', help='Weight for RBs by end tier (default 1,.5,.25,0,0)',
                        type=str, required=False, default='1,.5,.25,0,0')
    parser.add_argument('--wr-weights', help='Weight for WRs by end tier (default 1,.5,.25,0,0)',
                        type=str, required=False, default='1,.5,.25,0,0')
    return parser.parse_args()

def main():
    '''Runs the main function for this script'''
    args = parse_args()

    rb_value_file = os.path.abspath(args.rb_auction_file)
    wr_value_file = os.path.abspath(args.wr_auction_file)

    rb_bust_file = os.path.abspath(args.rb_bust_rates)
    wr_bust_file = os.path.abspath(args.wr_bust_rates)

    rb_rank_column = args.rb_rank_column
    rb_cost_column = args.rb_cost_column
    wr_rank_column = args.wr_rank_column
    wr_cost_column = args.wr_cost_column

    num_picks = args.num_draft_picks
    num_teams = args.num_teams
    available_cost = args.total_auction_cost - args.qb_te_d_k_cost

    rb_weights = map(float, args.rb_weights.split(","))
    wr_weights = map(float, args.wr_weights.split(","))

    cost_function = parse_position_function(args.position_value_function)
    rb_tiers = Utils.parse_value_file(rb_value_file, rb_rank_column, rb_cost_column, cost_function)
    wr_tiers = Utils.parse_value_file(wr_value_file, wr_rank_column, wr_cost_column, cost_function)

    rb_busts = Utils.parse_bust_file(rb_bust_file)
    wr_busts = Utils.parse_bust_file(wr_bust_file)

    team_simulator = TeamSimulator(rb_tiers, wr_tiers, rb_busts, wr_busts, rb_weights, wr_weights)
    team_simulator(num_teams, num_picks, available_cost)

if __name__ == '__main__':
    main()
