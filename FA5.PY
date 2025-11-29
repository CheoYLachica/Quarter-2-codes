destinations = []

destinations.append(input("Destination 1: "))
destinations.append(input("Destination 2: "))
destinations.append(input("Destination 3: "))
destinations.append(input("Destination 4: "))
destinations.append(input("Destination 5: "))

print("\nOriginal Travel Itinerary:")
for i, dest in enumerate(destinations):
    print(f"{i + 1}. {dest}")

print("\nLet's update your 2nd and 5th destinations.")

new_dest_2 = input("Enter a new destination for position 2: ")
destinations[1] = new_dest_2

new_dest_5 = input("Enter a new destination for position 5: ")
destinations[4] = new_dest_5

print("\nUpdated Travel Itinerary:")
for i, dest in enumerate(destinations):
    print(f"{i + 1}. {dest}")

print("\nUpdate complete! Have a great trip.")