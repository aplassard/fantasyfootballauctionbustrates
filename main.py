#!/usr/env python
'''This is the main function for the fantasy football bust rate calculator'''
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Fantasy Football Auction Bust Rate')
    parser.add_argument('--rb-auction-values', help='CSV file containing running back auction values (required)',
                        type=str, required=True)
    parser.add_argument('--wr-auction-values', help='CSV file containing wide receiver auction values (required)',
                        type=str, required=True)
    return parser.parse_args()

def main():
    args = parse_args()

if __name__ == '__main__':
    main()
