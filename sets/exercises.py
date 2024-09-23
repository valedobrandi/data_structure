clara = [0, 1, 5, 9, 10]

marco = [0, 2, 8, 9, 10]


set1 = set(clara)
set2 = set(marco)

differ1 = set1.difference(set2)
differ2 = set2.difference(set1)

player1 = max(differ1) - min(differ1)
player2 = max(differ2) - min(differ2)

if player1 > player2:
    print("Clara Win")
else:
    print("Marco Win")

string = "serdevemuitolegalmasehprecisoestudarbastante"



def longer_no_repeating_substring_len(string):
    biggest = 0
    for index, _ in enumerate(string):
        substr = set()
        for letter in string[index:]:
            if letter in substr:
                break
            substr.add(letter)
        if len(substr) > biggest:
            biggest = len(substr)
    print(biggest)
    return biggest

# longer_no_repeating_substring_len(string)


def longer_no_repeating_substring_len_op(string):
    string_set = set()
    count = 0
    values = []
    for letter in string:
        print(letter)
        if letter in string_set:
            values.append(count)
            count = 0
            print("----> CLEAR <-----")
            string_set = set()
        else:
            count += 1
            print("add", count)
            string_set.add(letter)
    print(max(values))
  

longer_no_repeating_substring_len_op(string)