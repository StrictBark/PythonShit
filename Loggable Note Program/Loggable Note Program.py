from time import sleep
from pathlib import Path


notes_list = []
p = Path(__file__).with_name('noteslist.txt')
with p.open('r') as fp:
    for line in fp:
        x = line[:-1]
        notes_list.append(x)

print("Python Notes Program 0.2")
print("To Save and Exit Option 6 MUST be Used!")
print()
run=1
while run == 1:
    run=0
    notes=int(input("What would you like to do? (1)Add to Notes  (2)Remove Note  (3)View Notes (4)Sort Notes (5)Clear Notes  (6)Stop Program "))
    #Add notes
    if notes == 1:
        note1=input("Please enter your note: ")
        notes_list.append(note1)
        print("Current Notes")
        print(notes_list)
        print()
        run=1
    #Remove notes
    elif notes == 2:
        print(notes_list)
        remove=input("Please type note you want removed: ")
        notes_list.remove(remove)
        print("Note has been removed");sleep(1)
        print()
        print("Current Notes")
        print(notes_list)
        print()
        run=1
    #View Notes
    elif notes == 3:
        print("Current Notes")
        print(notes_list)
        print()
        run=1
    #Sort notes
    elif notes == 4:
        sort=int(input("(1) Sort A-Z  (2)Sort Z-A  (3)Sort in Reverse Order: "))
        if sort == 1:
            notes_list.sort()
            print("Sorting from A-Z...");sleep(1)
            print()
            print("Current Notes")
            print(notes_list)
            print()
            run=1
        elif sort == 3:
            notes_list.reverse()
            print("Sorting in Reverse...");sleep(1)
            print()
            print("Current Notes")
            print(notes_list)
            print()
            run=1
        elif sort == 2:
            notes_list.sort()
            notes_list.reverse()
            print("Sorting from Z-A...");sleep(1)
            print()
            print("Current Notes")
            print(notes_list)
            print()
            run=1
        else:
            print("Wrong input")
            print()
            run=1

    elif notes == 5:
        rus=input("Are you sure you want to clear notes? yes/no ")
        if rus.lower() == "yes":
            notes_list.clear()
            print("Clearing Notes...");sleep(1)
            print()
            print("Current Notes")
            print(notes_list)
            print()
            run=1
        elif rus.lower() == "y":
            notes_list.clear()
            print("Clearing Notes...");sleep(1)
            print()
            print("Current Notes")
            print(notes_list)
            print()
            run=1
        else:
            print("Not Clearing");sleep(.5)
            print()
            print("Current Notes")
            print(notes_list)
            print()
            run=1

    elif notes == 6:
        with p.open('w') as fp:
            for item in notes_list:
             fp.write("%s\n" % item)
        print("Saving and Exiting...");sleep(3)
        run=0
        exit()
        
    else:
        print("Wrong input")
        print()
        run=1