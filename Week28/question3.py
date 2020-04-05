words = input("Please enter comma-separated words: ")

splitW = words.split(",")
sortW = sorted(splitW)
joinW = ",".join(sortW)

print(joinW)