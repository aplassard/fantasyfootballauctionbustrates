'''Useful utilities for the FFAB'''
import numpy as np

def parse_value_file(file_path, rank_column, cost_column, cost_func):
    '''Parses a player value file'''
    file_reader = open(file_path, 'r')
    file_reader.readline() # assuming there is a header. Yolo
    d_tmp = {}
    for line in file_reader:
        line = line.strip().split(",")
        if len(line) == 0:
            continue
        player_rank = int(line[rank_column]) if line[rank_column] else -1
        if player_rank < 0:
            continue
        player_cost = int(line[cost_column])
        player_tier = ((player_rank-1)/6)+1
        v_tmp = d_tmp.get(player_tier,[])
        v_tmp.append(player_cost)
        d_tmp[player_tier] = v_tmp
    tier_values = {}
    for ke in d_tmp.keys():
        tier_values[ke] = int(cost_func(d_tmp[ke]))
    return tier_values

def parse_bust_file(file_path):
    '''Parses a bust rate file in the specified format'''
    f_reader = open(file_path, 'r')
    n=0
    bust_d = {}
    for line in f_reader:
        line = line.strip().split(",")
        n += 1
        bust_d[n] = [float(x)/100 for x in line[1:]]
    return bust_d
