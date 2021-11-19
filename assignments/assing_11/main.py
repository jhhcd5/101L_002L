import time
class Clock:

    def __init__(self, hours, minutes, seconds, clock_type=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.clock_type = clock_type

    def tick(self):
        self.seconds += 1
        if self.seconds > 59:
            self.seconds = 0
            self.minutes += 1

        if self.minutes > 59:
            self.minutes = 0
            self.hours += 1

        if self.hours > 23:
            self.hours = 0

    def __str__(self):

        if self.clock_type == 0:

            return '{:02d}:{:02d}:{:02d}'.format(self.hours, self.minutes, self.seconds)
        else:

            s = "AM"
            if self.hours >= 12:
                s = "PM"
            h = self.hours

            if self.hours == 0:
                h = 12

            elif self.hours > 12:
                h = self.hours - 12

            return '{:02d}:{:02d}:{:02d} {:s}'.format(h, self.minutes, self.seconds, s)


hours = int(input("What is the current hour ==> "))
minutes = int(input("What is the current minute ==> "))
seconds = int(input("What is the current second ==> "))

clock = Clock(hours, minutes, seconds, 1)
while True:
    print(clock)
    clock.tick()
    time.sleep(1)


