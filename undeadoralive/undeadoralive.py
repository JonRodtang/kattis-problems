string = input()

if ":)" in string and ":(" in string:
    print("double agent")
elif ":)" in string:
    print("alive")
elif ":(" in string:
    print("undead")
else:
    print("machine")
