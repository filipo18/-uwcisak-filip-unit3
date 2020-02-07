# this program will demonstrate filter function

import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)
print(list(filter(lambda x: x > avg, data)))

countries = ["", "ffdsjflksd", "fdklsčfkdčs", "", "", "dlsfkčkdk", "fdkjdslf", ""]
print(list(filter(None, countries)))