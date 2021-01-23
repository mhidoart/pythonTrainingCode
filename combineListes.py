movies =["spiderman","batman","superman","noodleguy","dipshit"]
ratings = [5,10,7,4,9]
merged_list = []
for tree in zip(movies,ratings):
    merged_list.append(tree)
print(merged_list)