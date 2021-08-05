#!/usr/bin/python

'''
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.
Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
'''

def main():
    pile = list(map(int, input("Enter array: ").strip().split()))
    alex = 0
    lee = 0
    pile.sort()

    def pick(pile):
        if pile[0] > pile[-1]: 
            pile.pop(0)
        else:
            pile = pile[:-1]        
        return (pile)
        
    l = len(pile)
    while (l) > 2:
        a = max(pile[0], pile[-1])
        alex = a + alex
        pile = pick(pile)
        b = max(pile[0], pile[-1])
        lee = b + lee
        pile = pick(pile)
        l -= 2

    if alex > lee:
        print("true")

if __name__ == "__main__":
    main()
