import sys

# Max number of candidates
MAX = 9

# Array of candidates
candidates = {}


def main():

    # Check for invalid usage
    if len(sys.argv) < 2:
        print(f"Usage: plurality [candidate ...]\n")
        return 1

    # Populate array of candidates
    if len(sys.argv) > MAX:
        print(f"Maximum number of candidates is {MAX}")
        return 2

    for candidate in sys.argv[1:]:
        candidates[candidate] = 0
    
    voter_count = int(input("Number of voters:"))
    if voter_count == 0:
        print(f"Please provide a positive integer number")
        return 3
    
    # Loop over all voters
    for _ in range(voter_count):
        while True:
            if vote(input("Vote:")):
                break
            else:
                continue
    
    print_winner(candidates)


# Update vote totals given a new vote
def vote(candidate):
    try:
        candidates[candidate] += 1
        return True
    except:
        print("Invalid vote.")
        return False


# Print the winner (or winners) of the electrion
def print_winner(candidates):
    winners = []
    winner_vote_count = candidates[max(candidates, key=candidates.get)]
    for candidate in candidates:
        if candidates[candidate] == winner_vote_count:
            winners.append(candidate)
    
    for winner in winners:
        print(winner)

    
if __name__ == "__main__":
    main()
