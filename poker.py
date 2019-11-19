from collections import Counter

input_filename = 'poker.txt'
card_values = {'A': 14, 'K': 13, 'J': 11, 'Q': 12, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6, '9': 9, '8': 8, 'T': 10}
straight_values = [
    (14, 13, 12, 11, 10),
    (13, 12, 11, 10, 9),
    (12, 11, 10, 9, 8),
    (11, 10, 9, 8, 7),
    (10, 9, 8, 7, 6),
    (9, 8, 7, 6, 5),
    (8, 7, 6, 5, 4),
    (7, 6, 5, 4, 3),
    (6, 5, 4, 3, 2),
    (14, 5, 4, 3, 2)
]
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

def rank(hand):
	sorted_hands = sorted(((v, card_values[k]) for k,v in Counter(x[0] for x in hand).items()), reverse=True)
	score = zip(*sorted_hands)
	score[0] = ranks.index(score[0])
	if len(set(card[1] for card in hand)) == 1: score[0] = 5
	if score[1] in straight_values: score[0] = 8 if score[0] == 5 else 4
	return score

hands = (line.split() for line in open(input_filename))
print "Player 1 wins {} hands".format(sum(rank(hand[:5]) > rank(hand[5:]) for hand in hands))
