  
import check50

@check50.check()
def exists():
    """plurality.py exists"""
    check50.exists("plurality.py")
    check50.include("plurality_test.py")


@check50.check(exists)
def vote_check1():
    """vote returns true when given name of first candidate"""
    check50.run("python3 plurality_test.py Alice").exit(0)


@check50.check(exists)
def vote_check2():
    """vote returns true when given name of middle candidate"""
    check50.run("python3 plurality_test.py Bob").exit(0)


@check50.check(exists)
def vote_check3():
    """vote returns true when given name of last candidate"""
    check50.run("python3 plurality_test.py Charles").exit(0)


@check50.check(exists)
def vote_check4():
    """vote returns false when given name of invalid candidate"""
    check50.run("python3 plurality_test.py RickRoll").exit(0)


@check50.check(exists)
def vote_check5():
    """vote produces correct counts after some have already voted"""
    check50.run("python3 plurality_test.py Alice").exit(0)


@check50.check(exists)
def vote_check6():
    """vote leaves vote counts unchanged when voting for invalid candidate"""
    check50.run("python3 plurality_test.py RickRoll").exit(0)


@check50.check(exists)
def print_winner_check1():
    """print_winner identifies Alice as winner of election"""
    check50.run("python3 plurality.py Alice Bob")\
        .stdin("2").stdin("Alice").stdin("Alice").stdout("Alice\n").exit(0)


@check50.check(exists)
def print_winner_check2():
    """print_winner identifies Bob as winners of election"""
    check50.run("python3 plurality.py Bob Charles")\
        .stdin("3").stdin("Bob").stdin("Bob").stdin("Charles").stdout("Bob\n").exit(0)

@check50.check(exists)
def print_winner_check3():
    """print_winner identifies Charles as winners of election"""
    check50.run("python3 plurality.py Alice Bob Charles")\
        .stdin("4").stdin("Charles").stdin("Charles").stdin("Alice").stdin("Bob").stdout("Charles\n").exit(0)


@check50.check(exists)
def print_winner_check4():
    """print_winner prints multiple winners in case of tie"""
    check50.run("python3 plurality.py Alice Bob Charles").stdin("5")\
        .stdin("Alice").stdin("Alice").stdin("Bob").stdin("Bob").stdin("Charles").stdout("Alice\nBob\n").exit(0)


@check50.check(exists)
def print_winner_check5():
    """print_winner prints all names when all candidates are tied"""
    check50.run("python3 plurality.py Alice Bob Charles").stdin("3")\
        .stdin("Alice").stdin("Bob").stdin("Charles").stdout("Alice\nBob\nCharles\n").exit(0)
