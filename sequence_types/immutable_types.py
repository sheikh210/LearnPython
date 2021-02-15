# Immutable objects cannot be changed

result = True
another_result = result

print(id(result))
print(id(another_result))

result = False

print(id(result)) # This will have a different id, since we bound a new value (False) to the result variable
print(id(another_result))


result = 'Correct'
another_result = result

print(id(result))
print(id(another_result))

result += 'ish'

print(id(result)) # This will have a different id, since the result variable contains a new string value
print(id(another_result))
