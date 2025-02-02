import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

total_friends = len(friends)
selected_friend = random.randint(0, total_friends-1)

print(friends[selected_friend])
