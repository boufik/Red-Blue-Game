from random import randrange, shuffle
choices = ["BBB", "BBR", "BRB", "BRR", "RBB", "RBR", "RRB", "RRR"]
N = len(choices)

# Function 1 - Make black/red ---_. red/black
def opposite(letter):
    if letter == "B":
        return "R"
    return "B"

# Function 2 - Find the wanted sequence
def findTheWinningSequence(sequence):
    if len(sequence) != 3:
        print("Error while using function '" + findTheWinningSequence.__name__ + "'")
        return -1000
    first = opposite(sequence[1])
    winningSequence = first + sequence[0:2]
    return winningSequence

# Function 3 - Create a random shuffled cards deck with black and red cards
def createRandomDeck():
    deck1 = ["B" for i in range(26)]
    deck2 = ["R" for i in range(26)]
    deck1.extend(deck2)
    shuffle(deck1)
    shuffle(deck1)
    return "".join(deck1)

# Function 4 - Calculate theoritical possibility of winning
def calculatePossibility():
    poss = [2, 2, 2, 2, 3, 3, 7.5, 7.5]
    SUM = sum(poss)
    average = SUM / len(poss)
    possibility = average / (average + 1)
    possibility = round(100 * possibility, 3)
    return possibility          # Answer = 78.378

# Function 5 - Find the winner
def findWinner():
    # I will return a tuple = (winner, deck, lastIndex)
    deck = createRandomDeck()
    sequence = choices[randrange(N)]
    winningSequence = findTheWinningSequence(sequence)
    print("Deck = " + str(deck))
    print("Sequence = " + str(sequence) + ", winningSequence = " + str(winningSequence))
    # Throw the 1st 3 letters
    table = deck[0:3]
    counter = 2
    # I will return 1, if 1st player wins, otherwise I will return 2
    if sequence == table:
        return 1, deck, counter
    elif winningSequence == table:
        return 2, deck, counter
    # We enter the while-loop, if the first 3 letters don't match any of the 2 sequences
    while table[len(table)-3:len(table)] != sequence and table[len(table)-3:len(table)] != winningSequence:
        counter += 1
        table = table[len(table)-2:len(table)] + deck[counter]
        if sequence == table:
            return 1, deck, counter
        elif winningSequence == table:
            return 2, deck, counter


# Function 6 - Pretty winner
def prettyWinner(winner, deck, counter):
    indexesString = "Check deck in indexes " + str(counter-2) + ", " + str(counter-1) + ", " + str(counter)
    print("Player " + str(winner) + " wins! " + indexesString)
    if counter == 2:
        print(str(deck[0:3]) + " - " + str(deck[3:]))
    else:
        result1 = deck[0:counter-2]
        result2 = deck[counter-2:counter+1]
        result3 = deck[counter+1:]
        print(str(result1) + " - " + str(result2) + " - " + str(result3))
    print()

# MAIN FUNCTION
LIMIT = 10**4
winner2Counter = 0
for i in range(1, LIMIT+1):
    print("**************************** Round " + str(i) + " ****************************")
    winner, deck, counter = findWinner()
    prettyWinner(winner, deck, counter)
    if winner == 2:
        winner2Counter += 1

# Now, I have to do the stats
percentage = 100 * winner2Counter / LIMIT
percentage = round(percentage, 3)
print("Player 2 winning percentage  = " + str(percentage) + " %.")
print("Expected player 2 percentage = " + str(calculatePossibility()) + " %.")
