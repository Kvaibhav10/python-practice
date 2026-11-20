# i will make the list of things
# i will creat count of dict to store
# use loops to check and store the count
topics = ["python", "llm", "python", "api", "llm", "python"]

count = {}

for topic in topics:

    if topic in count :
        count[topic] += 1
    else:
         count[topic] = 1

for topic in count:
    if count[topic] > 1:
        print(topic, count[topic])