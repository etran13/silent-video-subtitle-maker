from main import Timestamp

test = Timestamp()
start = test
end = test
string1 = str(test)
print(string1)
end.add(1)

string2 = str(test)
print(string1, string2)