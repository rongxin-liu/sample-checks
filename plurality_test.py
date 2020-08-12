import sys
from plurality import vote, print_winner

def main():
    global candidates
    candidates = {'Alice': 0, 'Bob': 0, 'Charles': 0}
    before_vote = dict.copy(candidates)

    if sys.argv[1] in candidates:

        # vote returns true when given name of first candidate
        # vote returns true when given name of middle candidate
        # vote returns true when given name of last candidate
        assert vote(sys.argv[1], candidates) == True

        # vote produces correct counts after some have already voted
        assert candidates[sys.argv[1]] - before_vote[sys.argv[1]] == 1
        del candidates[sys.argv[1]]
        del before_vote[sys.argv[1]]
        assert candidates == before_vote
    else:

        # vote returns false when given name of invalid candidate
        assert vote(sys.argv[1], candidates) == False

        # vote leaves vote counts unchanged when voting for invalid candidate
        assert candidates == before_vote
    

if __name__ == "__main__":
    main()
