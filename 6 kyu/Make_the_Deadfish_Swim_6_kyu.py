# Create a parser to interpret and execute the Deadfish language.
# Deadfish operates on a single value in memory, which is initially set to 0.
# It uses four single-character commands:
# i: Increment the value
# d: Decrement the value
# s: Square the value
# o: Output the value to a result array
# All other instructions are no-ops and have no effect.
# Examples
# Program "iiisdoso" should return numbers [8, 64].
# Program "iiisdosodddddiso" should return numbers [8, 64, 3600].

def parse(data):
    output = 0
    output_array = []
    for letter in data:
        if letter == "i":
            output +=1
        elif letter == "d":
            output -=1
        elif letter == "s":
            output *= output
        elif letter == "o":
            output_array.append(output)
    return output_array
