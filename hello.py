#  File: ERsim.py
#  Description: Simulate an ER room with patients
#  Student's Name: Amy Fang
#  Student's UT EID: af27947
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 06/30/17
#  Date Last Modified: 06/30/17

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

# prints all the queues
def printQueues(critical, serious, fair):
    print("    Queues are:")
    print("   ", '{:<10}'.format("Fair:"), fair)
    print("   ", '{:<10}'.format("Serious:"), serious)
    print("   ", '{:<10}'.format("Critical:"), critical)
    print() 
    
def main():
    # open file
    infile = open("ERsim.txt", "r")

    # initialize queues
    critical = Queue()
    serious = Queue()
    fair = Queue()
    

    for line in infile:
        lst = line.split()
        command = lst[0]
        
        # add patients to respective queues
        if command == "add":
            condition = lst[1]
            name = lst[2]
            
            if condition == "Critical":
                critical.enqueue(name)
            elif condition == "Serious":
                serious.enqueue(name)
            else:
                fair.enqueue(name)

            # display command
            print("Command: Add patient", name, "to", condition, "queue")
            print()
            printQueues(critical, serious, fair)
            print()
            

        # treating patients
        elif command == "treat":
            condition = lst[1]

            # if command is "treat next"
            if condition == "next":

                # check critical queue first
                if critical.size() > 0:
                    patientName = critical.dequeue()
                    print("Command: Treat next patient on Critical queue")
                    print()
                    print("    Treating", patientName, "from Critical queue")

                # then check serious queue, if critical is empty
                elif serious.size() > 0:
                    patientName = serious.dequeue()
                    print("Command: Treat next patient on Serious queue")
                    print()
                    print("    Treating", patientName, "from Serious queue")

                # lastly, check fair queue, if both critical and serious are empty
                elif fair.size() > 0:
                    patientName = fair.dequeue()
                    print("Command: Treat next patient on Fair queue")
                    print()
                    print("    Treating", patientName, "from Fair queue")

                # if no patients
                else:
                    print("Command: Treat next patient on Critical queue")
                    print()
                    print("    No patients in queue")
                    print()
                    continue
                
                printQueues(critical, serious, fair)
                print()
                
            # if command is "treat Critical"
            elif condition == "Critical":
                print("Command: Treat next patient on Critical queue")
                print()

                if critical.size() > 0:
                    patientName = critical.dequeue()
                    print("    Treating", patientName, "from Critical queue")
                    printQueues(critical, serious, fair)
                    print()
                else:
                    print("No patients in queue")
                    print()


            # if command is "treat Serious"
            elif condition == "Serious":
                print("Command: Treat next patient on Serious queue")
                print()

                if serious.size() > 0:
                    patientName = serious.dequeue()
                    print("    Treating", patientName, "from Serious queue")
                    printQueues(critical, serious, fair)
                    print()
                else:
                    print("No patients in queue")
                    print()


            # if command is "treat Fair":
            elif condition == "Fair":
                print("Command: Treat next patient on Critical queue")
                print()

                if fairsize() > 0:
                    patientName = fair.dequeue()
                    print("    Treating", patientName, "from Critical queue")
                    printQueues(critical, serious, fair)
                    print()
                else:
                    print("No patients in queue")
                    print()

                
            # if command is "treat all"
            else:
                print("Command: treat all patients")
                print()

                # while there are still patients in queues
                while not(critical.size() == 0 and serious.size() == 0 and fair.size() == 0):
                    if critical.size() > 0:
                        patientName = critical.dequeue()
                        print("    Treating", patientName, "from Critical queue")
                    
                    elif serious.size() > 0:
                        patientName = serious.dequeue()
                        print("    Treating", patientName, "from Serious queue")
                    
                    else:
                        patientName = fair.dequeue()
                        print("    Treating", patientName, "from Fair queue")

                    printQueues(critical, serious, fair)
                    print()
                    
                # when there are no patients left
                print("    No patients in queue")
                print()
                
        # if command is "exit"
        else:
            print("Command: exit")
            break

    # close file 
    infile.close()
main()

    
    
