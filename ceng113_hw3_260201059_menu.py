import ceng113_hw3_260201059 as hw3
friendships = {}
while True :
    print("Menu:")
    print("[1] Add A Friend")
    print("[2] Remove A Friend")
    print("[3] Add A User")
    print("[4] Delete A User")
    print("[5] Offer A Friend")
    print("[6] Exit program")
    option = input("Please enter an option:")
##############################################
    if option == "1" :
        person,newFriend = input("Who do you want to add to whom ? Please type 'contact newfriend'  ").split(" ")
        if person in friendships.keys() and newFriend in friendships.keys():
            hw3.addAFriend(person,newFriend,friendships)
            print(friendships)
        else:
            print("Invalid person")
##############################################
    elif option == "2" :
        person,oldFriend = input("Who do you want to remove to whom ? Please type 'contact oldfriend'  ").split(" ")
        if person in friendships.keys() and oldFriend in friendships.keys():
            hw3.removeAFriend(person,oldFriend,friendships)
            print(friendships)
        else:
            print("Invalid person")
##############################################
    elif option == "3" :
        person = input("Who do you want to add ? ")
        hw3.addAUser(person,friendships)
        print(friendships)
##############################################
    elif option == "4" :
        person = input("Who do you want to delete ? ")
        if person in friendships.keys():
            hw3.deleteAUser(person,friendships)
            print(friendships)
        else:
            print("Invalid person")
##############################################
    elif option == "5" :
        person = input("Do you offer a friend for who ? ")
        if person in friendships.keys():
            print(hw3.offerAFriend(person,friendships))
        else:
            print("Invalid person")
##############################################
    elif option == "6" : break
    else: print("Invalid option")
    input("Please enter to continue.")