
import pickle

friends1 = {"Ahmed": [20, "Sligo", "0851909583"], "Mahad": [21, "Dublin", 
"0851234675"]}

friends2 = {"Ali": [35, "Paris", "0851349583"], "Yusuf": [40, "Barcelona", 
"0851231175"]}

friends = (friends1, friends2)


with open("friends.txt", "wb") as f:
    pickle.dump(friends, f)

with open("friends.txt", "rb") as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)