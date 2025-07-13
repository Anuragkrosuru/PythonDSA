class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    #intialize pointer to the head
    target = clues
    curr = clues.next
    # iterate throiugh the list 
    while curr:
    # check if its equal to the head
        if curr.value == target.value:
            return True
        curr = curr.next
    # return true
    # retuirn false
    return False


clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

def collect_false_evidence(evidence):
    if not evidence:
        return None
    
    values = []
    occured = {}
    curr = evidence
    cycle_start = ""
    # loop to find the first repeat (begining of the cycle)
    while curr:
        if curr.value not in occured:
            occured[curr.value] = 0
        else:
            cycle_start = curr.value
            break
        curr = curr.next
    
    start = evidence
    #traversing ot he cycle start
    while start and start.value != cycle_start:
        start = start.next

    # start appending items to alist started at the value
    while start:
        values.append(start.value)
        if start.next.value == cycle_start:
            break
        start = start.next
    # stop appending when we rech the first valeu again
    return values


clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    lesser_head = lesser = Node(None)
    greater_head = greater = Node(None)
    middle_head = middle = Node(None)

    curr = suspect_ratings
    while curr:
        if curr.value < threshold:
            lesser.next = Node(curr.value)
            lesser = lesser.next
        elif curr.value == threshold:
            middle.next = Node(curr.value)
            middle = middle.next
        elif curr.value > threshold:
            greater.next = Node(curr.value)
            greater = greater.next
        print(lesser)
        print(greater)
        print(middle)
        curr = curr.next
    
    greater.next = middle_head.next
    middle.next = lesser_head.next
    
    

    return greater_head.next

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))