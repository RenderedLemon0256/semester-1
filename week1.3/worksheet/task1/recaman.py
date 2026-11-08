# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = []
def numInSequence(num):
    """Checks whether a recaman is already in the sequence"""
    for x in sequence:
        if(x == num):
            return True
    return False

def getNextNum(prevNum, index):
    """Get next recaman number"""
    nextNum = prevNum - index
    if(numInSequence(nextNum) or nextNum < 0):
        nextNum = prevNum + index
    return nextNum

prevNum = 0
sequence.append(prevNum)
for i in range(1,L):
    nextnum = getNextNum(prevNum,i)
    sequence.append(nextnum)
    prevNum = nextnum
    

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence