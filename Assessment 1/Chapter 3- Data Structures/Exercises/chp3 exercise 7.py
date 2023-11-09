 # first lets make a list of places i want to visit 
 
Places = ["Japan","Canada","Germany","France"]

# print orignal list

print("original list:\n",Places)

# Use sorted() to print your list in alphabetical order without modifying the actual list.

print("\nAlphabetical order:\n",sorted(Places))

# Show that your list is still in its original order by printing it.

print("\noriginal list:\n",Places)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

print("\nReverse alphabetical order:\n",sorted(Places, reverse=True))

#Show that your list is still in its original order by printing it again.

print("\noriginal list:\n",Places)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.

Places.reverse()
print("\nReversed order of list:\n",Places)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

Places.reverse()
print("\nReversed it to orginal form:\n",Places)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

Places.sort()
print("\nsort list:\n",Places)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

Places.sort(reverse=True)

print("\nReverse sort list:\n",Places)

























