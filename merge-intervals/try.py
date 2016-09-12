# Merge Overlapping Intervals
# Given a set of time intervals in any order, merge all 
# overlapping intervals into one and output the result which
#  should have only mutually exclusive intervals. Let the 
#  intervals be represented as pairs of integers for simplicity. 
# For example, let the given set of intervals be 
# {{1,3}, {2,4}, {5,7}, {6,8} }. The intervals
#  {1,3} and {2,4} overlap with each other, so they 
#  should be merged and become {1, 4}. Similarly {5, 7} 
#  and {6, 8} should be merged and become {5, 8}

#!/usr/bin/env python

intervals = [[1, 3], [6, 8], [5, 7], [2, 4]]
intervals = [[5, 7], [7, 11], [14, 18], [12, 16], [30, 40], [2, 8]]


intervals = list(sorted(intervals, key=lambda x: x[0]))

merged = []

for inter in intervals:
	if not len(merged):
		merged.append(inter)
		continue

	top = merged.pop()

	if inter[0] <= top[1] or inter[0] == top[1] + 1:
		if inter[1] > top[1]:
			if inter[0] <= top[0]:
				merged.append([inter[0], inter[1]])

			else:
				merged.append([top[0], inter[1]])

		else:
			merged.append(top)

	else:
		merged.append(top)
		merged.append(inter)

print(merged)
