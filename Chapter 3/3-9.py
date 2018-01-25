# Dinner Guests
guest_list = ['person1', 'person2', 'person3']
guest_list.insert(0, 'person0')
guest_list.insert(2, 'person1.5')
guest_list.append('person4') 
print ("I can only invite two guests.")
popped_guest_1 = guest_list.pop(1)
print ("I'm sorry, " + popped_guest_1.title() + ", but you're no longer invited, there's not enough space.")
popped_guest_2 = guest_list.pop(2)
print (popped_guest_2.title() + ", you're no longer invited either, as there's not enough space.")
del guest_list[2]
del guest_list[2]
print (guest_list)
len(guest_list)

print("The number of people coming to dinner is " 
+ str(len(guest_list)) + ".")