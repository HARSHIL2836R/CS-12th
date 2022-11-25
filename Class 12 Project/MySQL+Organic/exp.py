class exp():
    def m():
        def newFun():
            print("inside n")
        try:
            newFun()
        except ValueError:
            print("out")

exp.m()