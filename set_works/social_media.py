


sachin_friends=["rahul","ganguly","yuvi","zaheer","raina","dhoni","laxman","srinath"]
dhoni_friends=["rahul","ganguly","yuvi","zaheer","raina","kohli","sachin"]
# display all users



all_users= set(sachin_friends).union(dhoni_friends)

print(all_users)

# display unique friends of sachin


sachin_unique_friends=set(sachin_friends).difference(dhoni_friends)

print(sachin_unique_friends)

mutual_friends = set(sachin_friends).intersection(dhoni_friends)

print(len(mutual_friends))