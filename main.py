#!/usr/bin/env python
'''This is the main function for the fantasy football bust rate calculator'''
import os
import argparse

def parse_args():
    '''Parses the arguments to this script'''
    parser = argparse.ArgumentParser(description='Fantasy Football Auction Bust Rate')
    parser.add_argument('--rb-auction-values',
                        help='CSV file containing running back auction values (required)',
                        type=str, required=True)
    parser.add_argument('--rb-cost-column',
                        help='Column in RB csv file containing RB auction cost(default 4)',
                        type=int, required=False, default=4)
    parser.add_argument('--rb-rank-column',
                        help='Column in RB csv file containing RB rank (default 6)',
                        type=int, required=False, default=6)
    parser.add_argument('--wr-auction-values',
                        help='CSV file containing wide receiver auction values (required)',
                        type=str, required=True)
    parser.add_argument('--wr-cost-column',
                        help='Column in WR csv file containing WR auction cost(default 4)',
                        type=int, required=False, default=4)
    parser.add_argument('--wr-rank-column',
                        help='Column in WR csv file containing WR rank (default 6)',
                        type=int, required=False, default=6)
    parser.add_argument('--qb-te-d-k-cost', help='Total cost spent on QB, TE, D, and K (default 4)',
                        type=int, required=False, default=4)
    parser.add_argument('--total-auction-cost',
                        help='Total money available for auction (default 200)',
                        type=int, required=False, default=200)
    return parser.parse_args()

def main():
    '''Runs the main function for this script'''
    args = parse_args()
    rb_value_file = os.path.abspath(args.rb_auction_values)
    wr_value_file = os.path.abspath(args.wr_auction_values)

if __name__ == '__main__':
    main()
