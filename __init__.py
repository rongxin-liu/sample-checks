import check50

@check50.check()
def install_packages():
    pass
    # test_command = "pip3 install cowsay"
    # code = check50.run(test_command).exit()
    # if code != 0:
    #     raise check50.Failure(f"expected exit code 0, not {code}")

@check50.check(install_packages)
def example_test():
    code = check50.run("python3 hello.py").exit()
    if code != 0:
        raise check50.Failure(f"expected exit code 0, not {code}")