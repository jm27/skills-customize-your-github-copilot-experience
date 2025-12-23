# Data Structures in Python - Starter Code
# Complete the tasks below to master lists, dictionaries, sets, and tuples

# ============================================================================
# Task 1: List Operations and Manipulation
# ============================================================================

def task_list_operations():
    """Practice list manipulation and common operations"""
    # TODO: Create a list of at least 5 numbers
    numbers = []
    
    # TODO: Add a number to the end of the list using append()
    
    # TODO: Insert a number at a specific position using insert()
    
    # TODO: Remove a number using remove() or pop()
    
    # TODO: Sort the list in ascending order
    
    # TODO: Create a new list using list comprehension that squares each number
    
    # TODO: Print the original and modified lists
    pass


# ============================================================================
# Task 2: Dictionary Creation and Data Lookup
# ============================================================================

def task_dictionary_operations():
    """Practice dictionary creation and retrieval"""
    # TODO: Create a dictionary representing a student with keys:
    #       'name', 'age', 'grade', 'courses'
    student = {}
    
    # TODO: Add a new key-value pair to the dictionary
    
    # TODO: Update an existing value using the key
    
    # TODO: Safely retrieve a value using get() method
    
    # TODO: Iterate through the dictionary and print all keys and values
    
    # TODO: Remove a key-value pair using pop() or del
    pass


# ============================================================================
# Task 3: Set Operations and Uniqueness
# ============================================================================

def task_set_operations():
    """Practice set operations and unique element management"""
    # TODO: Create a list with duplicate values
    data_with_duplicates = []
    
    # TODO: Convert the list to a set to remove duplicates
    
    # TODO: Create two sets and perform these operations:
    #       - Union (combine all elements)
    #       - Intersection (common elements)
    #       - Difference (elements in first set but not second)
    
    # TODO: Add and remove elements from a set using add() and remove()
    
    # TODO: Check if an element exists in the set using 'in'
    pass


# ============================================================================
# Task 4: Tuple Usage and Immutability
# ============================================================================

def task_tuple_operations():
    """Practice tuples and tuple unpacking"""
    # TODO: Create a tuple with at least 3 elements
    my_tuple = ()
    
    # TODO: Attempt to modify a tuple (this should raise an error - try it!)
    # Uncomment the line below to see the error:
    # my_tuple[0] = "new value"
    
    # TODO: Unpack a tuple into individual variables
    # Example: a, b, c = my_tuple
    
    # TODO: Create a function that returns multiple values as a tuple
    #       and unpack the returned values in the calling code
    
    # TODO: Create a dictionary using tuples as keys
    #       (dictionaries require hashable types like tuples, not lists)
    my_dict_with_tuple_keys = {}
    pass


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("Task 1: List Operations")
    task_list_operations()
    
    print("\nTask 2: Dictionary Operations")
    task_dictionary_operations()
    
    print("\nTask 3: Set Operations")
    task_set_operations()
    
    print("\nTask 4: Tuple Operations")
    task_tuple_operations()
