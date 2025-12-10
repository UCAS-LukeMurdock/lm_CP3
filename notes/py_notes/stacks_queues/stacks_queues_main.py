# LM  Stacks and Queues Notes


# What is time complexity in programming?
    # Just big O notation
    # How many equations have to be run. How long will it take for the program to run.
    # Worst case time complexity for a program. How long it would take for that worst case

    # O(1) is the fastest. One thing is happening. It doesn't matter how long the list. You know the information you need. Ideal, you just go grab it since you know where it is.
    
# What are the levels of time complexity?
    # O(1)  |  aka 1,  stacks and queues except queues in C++ arrays and things like that since then it would be O(n^2) or O(n) for remaking the array
    # O(n)  | linear, direct connection between size of data and time it takes. Sequential searching (could be the last item so might take whole list)
    # O(n log(n))  | quick sort and merge sort, deals with most sorting algorithms
    # O(n^2)  | Quadratic time. Bubble sort, selection sort, insert sort. the length of the data squared is the time it will take or something
    
# What is a stack?
    # A list that you can only access things from the top (add, remove, view)
    
# What does LIFO stand for?
    # L ast-
    # I n,
    # F irst-
    # O ut

    # LIFO, or Last-In, First-Out, is an accounting method for inventory where it's assumed that the most recently purchased goods are the first ones sold. This contrasts with the FIFO method, which assumes the oldest goods are sold first. LIFO can be beneficial during periods of inflation because it results in a higher cost of goods sold, which in turn lowers a company's taxable income. 
    # LIFO, or Last-In, First-Out, is a principle in coding where the last item added to a data structure is the first one to be removed. This is the same logic used by a stack, a fundamental data structure where new elements are added to the top, and removal also happens from the top. A common analogy is a stack of pancakes; you remove the last one you put on top first. 
    # How it works in coding
        # Stack data structure: A stack is the most common implementation of LIFO.
        # Push: When a new item is added, it's pushed onto the top of the stack.
        # Pop: When an item is removed, it's the most recently "pushed" item that is popped off from the top.
    # Examples:
        # Function calls: When a function calls another function, the system uses a LIFO stack to manage the order. The most recent function call is the first one to finish and return.
        # Undo/Redo: In a text editor, each action you take is pushed onto a LIFO stack. Pressing "undo" removes the last action from the stack and reverses it.
        # Event handling: LIFO can be used to manage a stack of events, processing the most recent event first to ensure a responsive interface. 
        # Stack of cards or plates

# What are the things that a stack can do?
    # Protects all of the items except the front one.
    # Can be used to store timeline event things
    # Etc.
    
# How are stacks normally written in python?
    # As a class with methods
    
# What is a queue?
    # A list that you can add to the back and remove from the front. Also, you can look at the first item
    # FIFO (First In, First Out)
    # Uses Linked Lists, array managing
    
# How are queues different from stacks?
    # Queues have to interact with the start of the list which makes all the indexes need to change
    # You can remove things from the bottom
