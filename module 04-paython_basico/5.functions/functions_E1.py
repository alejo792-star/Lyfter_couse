
# def count_letters(text,letter):
text = "programacion"
letter = "a"
text_to_list = []
text_to_list.append(text)
counter_tetter = 0
for i in text:
    if text[i] == letter:
        counter_tetter =+ 1
    print(f"has been found {letter} = {counter_tetter}")

'''
def main():
    text_analyze = input("give me a word")
    letter =input("give me a letter to find")
    counter = count_letters(text_analyze,letter)
    print(f"{counter} 😎")
'''