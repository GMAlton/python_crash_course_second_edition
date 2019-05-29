guests = ["Dee", "Gary", "Jesse"]
print(f"You are invited to come to dinner {guests[0]}, if you are interested.")
print(f"You are invited to come to dinner {guests[1]}, if you are interested.")
print(f"You are invited to come to dinner {guests[2]}, if you are interested.\n")

print(f"Oh no, it looks like {guests[1]} can't make it!\n")
del guests[1]
guests.append("Meagan")

print(f"You are invited to come to dinner {guests[0]}, if you are interested.")
print(f"You are invited to come to dinner {guests[1]}, if you are interested.")
print(f"You are invited to come to dinner {guests[2]}, if you are interested.\n")

print("I found a bigger dinner table, let's invite more guests!\n")
guests.insert(0, "Gary")
guests.insert(1, "Robert")
guests.append("William")

print(f"You are invited to come to dinner {guests[0]}, if you are interested.")
print(f"You are invited to come to dinner {guests[1]}, if you are interested.")
print(f"You are invited to come to dinner {guests[2]}, if you are interested.")
print(f"You are invited to come to dinner {guests[3]}, if you are interested.")
print(f"You are invited to come to dinner {guests[4]}, if you are interested.")
print(f"You are invited to come to dinner {guests[5]}, if you are interested.")