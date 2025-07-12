import datetime as DT
import random as R
import time as T


# Method to get datetime
def getDT(self):
    return DT.datetime.now()


# Method to get week
def getWeek(self):
    global PT
    return PT.strftime("%A")


# Method to display the WeekDay & PT
def display_DT(self):
    global PT, WeekDay
    print(WeekDay, PT, "\n")


class PermissionAccess:

    def __init__(self):
        self.generated_otp = None  # Store the generated OTP
        self.attempts = 0  # Count the number of attempts

    # Method to generate a 6-character OTP
    def genOTP(self):
        self.generated_otp = R.randint(100000,
                                       999999)  # Generate a 6-digit OTP
        return self.generated_otp

    # Method to input OTP and check if it matches the generated OTP
    def input_otp(self):
        user_input = int(input("Enter the OTP: "))  # Prompt user for OTP
        if user_input == self.generated_otp:
            return True  # Return True if OTP is valid
        else:
            self.attempts += 1
            print("Permission access failed.", end=" ")
            return False  # Return False if OTP is invalid

    # Method to implement wait time between attempts
    def attempt_wait_time(self, seconds):
        if self.attempts > 5:  # Wait after 5 failed attempts
            print(f"Waiting for {seconds} seconds before the next attempt...")
            T.sleep(seconds)  # Wait for specified seconds


class ProgInfo:
    # Initialize the program information
    def __init__(self, name, ver, prog_lang, power, supporting):
        self.name = name
        self.ver = ver
        self.prog_lang = prog_lang
        self.power = power
        self.supporting = supporting

    # Display method to show program information
    def display_info(self):
        return (
            f">> {self.name} / Version: {self.ver} / Language: {self.prog_lang} "
            f"/ Powered by: {self.power} / Support for: {self.supporting}\n")


class ProgCore:
    # Initialize the Core
    def __init__(self, generation, ver, copyright):
        self.generation = generation
        self.ver = ver
        self.copyright = copyright

    # Display method to show Core information
    def display_info(self):
        return (f">> {self.generation}--{self.ver} / {self.copyright}\n")


# Create instances of the classes
PT = getDT("")
WeekDay = getWeek("")
PA = PermissionAccess()
prog = ProgInfo("P3VC--25", 1.0, "Python-3.10.**", "Thonny", "Python.org")
core = ProgCore("Prototype", 1,
                "copyright belongs to [cyruschuikc@gmail.com]\n")

# Output program and core information
display_DT("")
print(prog.display_info())
print(core.display_info())

# Generate an OTP
otp = PA.genOTP()
print(f"Generated OTP: {otp}")

# Allow user to attempt to enter the OTP
while True:
    if PA.input_otp():  # Check if the OTP is valid
        print("Permission access successful.")
        break  # Exit the loop if OTP is valid
    PA.attempt_wait_time(5)  # Wait for next attempt after 5 failed attempts
