#first we will make a list of people i would like to invite

friends = ["Fahad","Mohsin","Tayyab","Shahab"]

# we will use for loop to print invitation message

for friend in friends:
    Invitation_msg = f"Dear {friend},\nYou are Invited to dinner at my place.\n"
    print(Invitation_msg)
    
#friends who can't Make it 

friend_cant_make_it ="Fahad"
print(f"\nsadly,{friend_cant_make_it} Can't make it to the dinner.")

# now we will replace fahad with a new friend 

friends.remove('Fahad')
friends.insert(0,"Asad")

#now we will print new set of invitations
print("\nSecond updated list\n")
for friend in friends:
    New_set_of_invitations = f"Dear {friend},\nYou are Invited to dinner at my place.\n"
    print(New_set_of_invitations)
    
print("\nYou can only invite two persons for dinner\n")   #only two friends are allowed for dinner

#now we will remove two persons from the list

poped_friend=friends.pop(2)
print(f"\nSorry,{poped_friend} I can't invite you for dinner.\n")

poped_friend=friends.pop(1)
print(f"\nSorry,{poped_friend} I can't invite you for dinner.\n")

#we will print the two remaining persons who are still invited 

for friend in friends:
    Still_invited = f"Dear {friend},\nYou guys are still Invited for dinner at my place.\n"
    print(Still_invited)

# now we will use del to remove last to person and print empty list
del friends[:]
print(friends)























