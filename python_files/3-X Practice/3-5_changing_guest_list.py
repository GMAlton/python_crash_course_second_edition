guests = ["Dee", "Gary", "Jesse"]
print(f"You are invited to come to dinner {guests[0]}, if you are interested.")
print(f"You are invited to come to dinner {guests[1]}, if you are interested.")
print(f"You are invited to come to dinner {guests[2]}, if you are interested.")

print(f"Oh no, it looks like {guests[1]} can't make it!")
del guests[1]
guests.append("Meagan")

print(f"You are invited to come to dinner {guests[0]}, if you are interested.")
print(f"You are invited to come to dinner {guests[1]}, if you are interested.")
print(f"You are invited to come to dinner {guests[2]}, if you are interested.")
