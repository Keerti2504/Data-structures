import ast

string = ast.literal_eval(input())     # converts list-string to actual list

write = 0
count = 1

for i in range(1, len(string) + 1):

    # same character continues
    if i < len(string) and string[i] == string[i - 1]:
        count += 1
    else:
        # write the character
        string[write] = string[i - 1]
        write += 1

        # write the count if > 1
        if count > 1:
            for c in str(count):
                string[write] = c
                write += 1

        count = 1

print(write)
