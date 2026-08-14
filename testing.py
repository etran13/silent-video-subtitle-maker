from main import Timestamp

test = Timestamp()
ans = 0.0

print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

test.add(360)
ans += 360
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

test.add(360)
ans += 360
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

test.add(360)
ans += 360
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

#Decimal addition
test.add(360.233244322)
ans += 360.233244322
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

test.add(360.233244322)
ans += 360.233244322
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

test.add(360.233244322)
ans += 360.233244322
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

test.add(60.232)
ans += 60.232
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

test.add(60.232)
ans += 60.232
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")

test.add(60.231)
ans += 60.231
print(f"{test.convert_to_secs() == ans}, exp: {ans}, actual: {test.convert_to_secs()}")