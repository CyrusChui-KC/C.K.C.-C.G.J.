import datetime, random, time

class Core:
    def __init__(self,bunch,name,ver):
        self.bunch = bunch
        self.name = name
        self.ver = ver
    def DateTime(self):
        return datetime.datetime.now()
    def WeekDay(self):
        Datetime = self.DateTime()
        return Datetime.strftime("%A")
    def displayTIME(self):
        __Datetime__ = self.DateTime
        Week = self.WeekDay()
        print(Week, datetime.datetime.now())
    def vUser(self):
        user = input(str("Your PC username:"))
        return user
    def gen_OTP(self):
        OTP = random.randint(100000,999999)
        return OTP
    def enter_OTP(self):
        times = 0
        Password = self.gen_OTP()
        print("Please enter this OTP to verify that you are not a robot", Password)
        password = int(input(""))
        while password != Password:
            print("Authentication failed! Please retry.")
            times += 1
            if times >=5:
                print("You entered wrong OTP several times! Please wait",times,"sec.(s) then rerty.")
                time.sleep(times)
                print("Please enter this OTP to verify that you are not a robot", Password)
                password = int(input(""))
            else:
                print("Please enter this OTP to verify that you are not a robot", Password)
                password = int(input(""))
        else:
            print("Authentication pass!")
    def path(self):
        User = self.vUser()
        print(f"{self.bunch}/User/{User}|>{self.name}/{self.ver}|>-")

### you could add your ideas here
    ## lets discrover your galaxy
        # Your new journery are wait for you

if __name__ == "__main__":
    __mode__ = input("Please choose a mode:(.=demo|0=original) ") # "."=demo, 0=original
    if __mode__ == ".":
        bunch = "DemoBunch"
        prog_name = "DemoOfPython3VirtualCore-OpenSource"
        version = "1.0"
    elif __mode__ == "0":
        bunch = "ProgConsole C:"
        prog_name = "Python3VirtualCore-OpenSource"
        version = "1.0"
    else:
        bunch = "DemoBunch"
        prog_name = "DemoOfPython3VirtualCore-OpenSource"
        version = "1.0"
    core = Core(bunch, prog_name, version)
    core.displayTIME()
    core.gen_OTP()
    core.enter_OTP()
    core.displayTIME()
    core.path()
    