"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")

# TODO: apply a sequence of string methods to produce a cleaned_message
cleanedMessage = raw_message.strip()
strippedMessage = cleanedMessage.lower()
messageParts = strippedMessage.split(" ")
cleanedMessage = ""
capitalise = True
for part in messageParts:
    if( part == " "):
        continue
    if(capitalise):
        cleanedMessage += part.capitalize() + " "
        capitalise = False
    else:
        cleanedMessage += part + " "
    endingCharacter = part[len(part)-1]
    if(endingCharacter == "." or endingCharacter == "?" or endingCharacter == "!"): #start of a new sentence so we capitalise
        capitalise = True
cleanedMessage = cleanedMessage.strip() #the code above leaves a trailing whitespace so this is the easiest way to remove it
print(f"This is the original message, which had {len(raw_message)} characters: {raw_message}")
print(f"This the cleaned message, which has {len(cleanedMessage)} characters: {cleanedMessage}")
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version
