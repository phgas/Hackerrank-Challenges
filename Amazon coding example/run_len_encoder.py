def run_len_enconder(string: str) -> str:
    """This function encodes a given by using run length encoding.
    \nExample: 
        Input[str]: aaaabbccca
        Return[str]: 4a2b3c1a
    \nTime & Space complexity: O(n), where n equals to the length of characters in string
    """
    # letters can occure multiple times aaaaba -> 4a1b1a
    # input isn't malicious (only letters)
    # conditions: is there any max length of the input? -> no
    first_run = True
    counter = 1
    encoded_string = ""
    for i in range(len(string)):
        left_pointer = i - 1
        right_pointer = i
        if string[left_pointer] == string[right_pointer] and left_pointer != -1:
            counter += 1
        elif first_run == True:
            first_run = False
        else:
            encoded_string += f"{counter}{string[left_pointer]}"
            counter = 1

    encoded_string += f"{counter}{string[right_pointer]}"

    return encoded_string

if __name__ == "__main__":
    encoding = run_len_enconder("aaaabbccca")
    print(encoding)