from main import Timestamp

test = Timestamp()
print(test)

# test.add(1)
# print(f"{test}, {test == "00:00:01.000"}")

test.add(60)
print(f"{test}, {test == "00:01:00.000"}")

test.add(61)
print(f"{test}, {test == "00:02:01.000"}")
