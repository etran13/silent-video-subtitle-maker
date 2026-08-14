from main import Timestamp

test = Timestamp()
print(test)

# test.add(1)
# print(f"{test}, {test == "00:00:01.000"}")

test.add(60)
answer = "00:01:00.000"
print(str(test) == answer)

test.add(61)
answer = "00:02:01.000"
print(str(test) == answer)

test.add(61.22)
answer = "00:03:02.220"
print(str(test))
print(str(test) == answer)
