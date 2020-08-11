import sys
from plurality import vote, print_winner

def main():

    global candidates
    candidates = {'Alice': 0, 'Bob': 0, 'Charles': 0}
    before_vote = {'Alice': 0, 'Bob': 0, 'Charles': 0}
    
    if len(sys.argv) == 1:
        try:
            assert(candidates==before_vote)
            return 0
        except:
            return 1
    
    if sys.argv[1] == "RickRollRoll":
        vote(sys.argv[1], candidates)
        try:
            assert(candidates==before_vote)
            return 0
        except:
            return 1

    if vote(sys.argv[1], candidates):
        if candidates[sys.argv[1]] - before_vote[sys.argv[1]] == 1:
            return 0
        else:
            return 1
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
