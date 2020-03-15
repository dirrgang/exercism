def reverse(text):
    """String slicing can accept a third parameter in addition to two index numbers. The third 
    parameter specifies the stride, which refers to how many characters to move forward after the 
    first character is retrieved from the string. So far, we have omitted the stride parameter, and 
    Python defaults to the stride of 1, so that every character between two index numbers is retrieved. 
    
    Additionally, you can indicate a negative numeric value for the stride, 
    which we can use to print the original string in reverse order if we set the stride to -1: """
    return text[::-1]
