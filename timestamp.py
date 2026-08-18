class Timestamp:
    def __init__(self, hrs=0, mins=0, secs=00.000):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs

    def __str__(self):
        return f"{self.hrs:02}:{self.mins:02}:{self.secs:06.3f}".replace(".", ",")
    
    def add(self, number):
        "Takes in a number in seconds and adds it to the timestamp."
        seconds = self.secs + number
        #print(f"Seconds: {seconds}")
        if seconds < 60:
            #print("Less than")
            self.secs = seconds
            return
        else:
            carryover = seconds // 60
            remainder = seconds - (carryover * 60)
            #print(f"Carryover: {carryover}, Remainder: {remainder}")
            self.secs = remainder
            self.mins += int(carryover)

    def convert_to_secs(self):
        "Converts the timestamp to seconds (purely for testing)"
        return self.secs + (self.mins * 60) + (self.hrs * 60 * 60)