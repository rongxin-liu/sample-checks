import sys

from plurality import vote


def main():
    global candidates
    candidates = {'Alice': 0, 'Bob': 0, 'Charles': 0}
    
    candidate = sys.argv[1]
    votes_before = candidates[candidate]
    
    if candidate in candidates:      
        # vote returns True when candidate exists
        assert vote(candidate, candidates)

        # vote adds vote to candidate
        assert (candidates[candidate] - votes_before) == 1
    else:
        # vote returns False when candidate doesn't exist
        assert not vote(candidate, candidates)

        # vote count stays the same
        assert candidates[candidate] == votes_before
    

if __name__ == "__main__":
    main()
