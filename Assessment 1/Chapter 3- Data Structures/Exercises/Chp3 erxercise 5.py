#first we will make a list of people i would like to invite

friends = ["Fahad","Mohsin","Tayyab","Shahab"]

# we will use for loop to print invitation message

for friend in friends:
    Invitation_msg = f"Dear {friend},\nYou are Invited to dinner at my place."
    print(Invitation_msg)
    
#friends who can't Make it 

friend_cant_make_it ="Fahad"
print(f"\nsadly,{friend_cant_make_it} Can't make it to the dinner.")

# now we will replace fahad with a new friend 

friends.remove('Fahad')
friends.insert(0,"Asad")

#now we will print new set of invitations
print("\nSecond updated list")
for friend in friends:
    New_set_of_invitations = f"Dear {friend},\nYou are Invited to dinner at my place."
    print(New_set_of_invitations)
    


