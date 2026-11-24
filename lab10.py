# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    # Restate: Evaluate a mathematical expression written in postfix notation.
    # Example: ["2", "1", "+"] = 3
    # Approach:
    # Create an empty stack.
    # Loop through each token.
    # If it is a number, convert it to an integer and push it.
    # If it is an operator, pop the last two numbers.
    # Perform the operation and push the result.
    # Return the final number.
    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = [] 

    for token in tokens: 
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))

        else: 
            b= stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            elif token == "/":
                result = int(a / b)

            stack.append(result)

    return stack.pop()


def decode_string(s):
    # Outline:
    # Restate: Decode a string by repeating the characters inside brackets.
    # Example: "3[a]" = "aaa"
    # Approach:
    # Create an empty stack and current string.
    # Loop through each character.
    # If it is a digit, build the repeat number.
    # If it is an opening bracket, save the current string and number.
    # If it is a closing bracket, pop the saved values.
    # Repeat the current string and combine it with the previous string.
    # Otherwise, add the character to the current string.
    # Return the decoded string.
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    
    stack = []
    current_string = ""
    number = 0 

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)

        elif char == "[":
            stack.append((current_string,number))
            current_string = ""
            number =0

        elif char == "]":
            previous_string, repeat = stack.pop()
            current_string = previous_string + current_string * repeat

        else:
            current_string += char

    return current_string


def daily_temperatures(temps):
    # Outline:
    # Restate: Find how many days until a warmer temperature for each day.
    # Example: [30, 40, 50, 60] = [1, 1, 1, 0]
    # Approach:
    # Create a result list filled with zeros.
    # Create an empty stack to store day indices.
    # Loop through each day.
    # While the stack is not empty and today's temperature is warmer:
    # Pop the previous day from the stack.
    # Calculate the number of days waited.
    # Store the result at the previous day's index.
    # Push today's index onto the stack.
    # Return the result list.
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while len(stack) > 0 and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass 


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
