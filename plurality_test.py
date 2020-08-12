import sys

from plurality import vote


def main():
    candidates_ = {'Alice': 0, 'Bob': 0, 'Charles': 0}

    global candidates
    candidates = dict.copy(candidates_)

    candidate = sys.argv[1]

    if candidate in candidates:
        # vote returns True when candidate exists
        assert vote(candidate, candidates)

        # vote adds vote to candidate
        assert (candidates[candidate] - candidates_[candidate]) == 1

        assert vote(candidate, candidates)
        assert (candidates[candidate] - candidates_[candidate]) == 2

        # vote doesn't change any other candidates' votes
        assert all(candidates[c] == candidates_[c] for c in candidates_ if c != candidate)
    else:
        # vote returns False when candidate doesn't exist
        assert not vote(candidate, candidates)

        # vote count stays the same
        assert candidates == candidates_


if __name__ == "__main__":
    main()
