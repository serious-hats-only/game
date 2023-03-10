from __future__ import print_function
from __future__ import division
from collections import Counter
import math
import random
import operator
"""

this library handles the combination of dictionaries of suggestions

"""

#### SORTING ####

# given a list of tuples, returns its items sorted descending by score
def sort_descending(d):
	return list(reversed(sorted(d.items(),key=operator.itemgetter(1))))

# given a list of tuples, returns its items sorted ascending by score
def sort_ascending(d):
	return sorted(d.items(),key=operator.itemgetter(1))

#### LISTING ####

# returns the subset of d that is on the whitelist
def whitelist(d, WL):
	return {k: v for k, v in d.items() if k in WL}

# returns the subset of d that is not on the blacklist
def blacklist(d, BL):
	return {k: v for k, v in d.items() if k not in BL}


######## SET LOGIC ########

# combines several dictionaries into one, adding scores that share the same key
def union(dicts):
	if len(dicts) == 0:
		return dicts
	
	new_dicts = list(dicts)
	union = {k: v for k,v in new_dicts.pop().items()}	# deep copy
	while len(new_dicts) > 0:
		to_add = new_dicts.pop()
		for k, v in to_add.items():
			if k in union:
				union[k] += v
			else:
				union[k] = v
	return union

# union that combines scores according to associated weights
def weighted_union(dicts, weights):
	weighted_dictionaries = [{k: v*weights[i] for k, v in dicts[i].items()} for i in range(len(dicts))]
	return union(weighted_dictionaries)

# returns a single combined dictionary with only keys common to all dicts
def intersect(dicts):
	return whitelist(union(dicts), WL=set.intersection(*[set(d.keys()) for d in dicts]))

# intersection that combines scores according to associated weights
def weighted_intersect(dicts, weights):
	return whitelist(weighted_union(dicts, weights), WL=set.intersection(*[set(d.keys()) for d in dicts]))

# returns the keys in the base with the keys in the addition added, if they're in the base
def augment(base, addition, base_wt, add_wt):
	return whitelist(weighted_union(dicts=[base, addition], weights=[base_wt, add_wt]), WL=base.keys())

def normalize(d):
	total = sum(d.values())
	return {k: v/total for k, v in d.items()}


#### COMPARISON ####

def delta(signal, baseline):
	return {k: signal[k]/baseline[k] for k in signal if k in baseline}

# returns number of keys in d1 that map to same value in d2
def kv_matches(d1, d2):
	return len([k for k in d1.keys() if k in d2 and d2[k] == d1[k]])

# returns proportion of keys in d1 that have same value in d2
def similarity(d1, d2):
	simscore = kv_matches(d1, d2) / (len(d1)+1)
	return simscore




#### PRUNING ####

# returns list of top n scores in d
def top_n(d, n):
	return sort_descending(d)[:n]

# returns list of scores in the top nth percentile
def up_to_threshold(d, threshold):
	sorted_and_normed = sort_descending(normalize(d))
	index = 0
	total = 0
	for key, rate in sorted_and_normed:
		total += rate
		index += 1
		if total > threshold:
			return sorted_and_normed[:index]
	return sorted_and_normed

# returns all entries whose values are equal to or greater than the threshold
def clears_threshold(d, threshold):
	return {k: v for k, v in d.items() if v>=threshold}

# returns all entries whose value is longer than a minimum length
def long_entries(d, min_length):
	return {k: v for k, v in d.items() if len(v) >= min_length}


### CHOICE ####


def random_choice(d):
	return random.choice(d.items())


def stochastic_choice(d):
	total = sum(d.values())
	threshold = total * random.uniform(0,1)
	cumulative = 0
	for k, v in d.items():
		cumulative += v
		if cumulative > threshold:
			return (k, v)
	print("Error: did not reach threshold")
	return None

### ENTROPY MEASURES ###

# entropy of a given decision tree
def entropy(tree):
	return -1 * sum([tree[option] * math.log(tree[option]) for option in tree])

### TESTS ###

def basic_test():
	d1 = {'a': 10, 'b': 15, 'c': 43}
	d2 = {'a': 4, 'y': 21, 'c': 9}

	print(augment(d1,d2,1,1))
	print(union([d1,d2]))
	print(intersect([d1,d2]))
	print(weighted_intersect([d1,d2],[1,5]))
	print(normalize(d1))

#### SAVING AND LOADING ####

def to_tab_delimited(d, path):
	with open(path, 'w') as f:
		for k, v in sort_descending(d):
			f.write(k + '\t' + str(v) + '\n')


def from_tab_delimited(path):
	with open(path) as f:
		return {line.split('\t')[0]: float(line.split('\t')[1]) for line in f.readlines()}


#### USER INTERACTION ####


def inspect_loop(d):

	while True:
		term = raw_input('Input term >\n')
		print(d[term][:20])



if __name__ == '__main__':
	pass


def stochastic_test():
	import time
	options = {'a': 10, 'b': 5, 'c': 0.1}
	while True:
		print(stochastic_choose_n(options, 2))
		time.sleep(0.01)




	