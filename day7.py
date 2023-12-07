from collections import Counter, defaultdict


IN = open("in.txt").read().splitlines()

CARD_VALUES = {
  "A": 13,
  "K": 12,
  "Q": 11,
  "T": 10,
  "9": 9,
  "8": 8,
  "7": 7,
  "6": 6,
  "5": 5,
  "4": 4,
  "3": 3,
  "2": 2,
  "J": 1,
}

def get_rank(hand):
  
  counter = Counter(hand)
  joker = counter[1]
  counter[1] = 0
  occur = Counter(counter.values())
  if (occur[5] == 1): # straight flush
    return 7
  elif (occur[4] == 1): # four of a kind
    return 6 + joker
  elif (occur[3] == 1 and occur[2] == 1): # full house
    return 5
  elif (occur[3] == 1): # three of a kind
    if joker == 1:
      return 6
    elif joker == 2:
      return 7
    return 4 
  elif (occur[2] == 2): # two pair
    if joker == 1:
      return 5
    return 3
  elif (occur[2] == 1): #   one pair
    if joker == 1:
      return 4
    elif joker == 2:
      return 6
    elif joker == 3:
      return 7    
    return 2
  else:
    if joker == 1:
      return 2
    elif joker == 2:
      return 4
    elif joker == 3:
      return 6
    elif joker == 4:
      return 7
    elif joker == 5:
      return 7
    return 1 # high card

def lexico_sort(hands: list[list[int]]):
  return sorted(hands, key=lambda x: (x[0], x[1], x[2], x[3], x[4]))

ranks = defaultdict(list)
bets = defaultdict(int)
for line in IN:
  hand, bet = line.split()
  hand = [CARD_VALUES[x] for x in hand]
  ranks[get_rank(hand)].append(hand)
  bets[tuple(hand)] = int(bet)

for r in ranks:
  ranks[r] = lexico_sort(ranks[r])

out = 0
index = 1
for i in range(1, 8):
  if i in ranks:
    for hand in ranks[i]:
      out += bets[tuple(hand)] * index
      print(hand, bets[tuple(hand)], index)
      index += 1

print(out)    