def split_list():

    input_list = list(map(int, input("Введіть елементи списку через пробіл: ").split()))

    while True:
  
        split_value = int(input("Введіть значення для розбиття: "))

        if split_value in input_list:
            break 
        else:
            print(f"Число {split_value} не знайдено у списку. Спробуйте ще раз.")

    index = input_list.index(split_value) + 1
    
    first_list = input_list[:index]  
    second_list = input_list[index:]  

    print(f"Перший список (до і включаючи {split_value}): {first_list}")
    print(f"Другий список (після {split_value}): {second_list}")

split_list()

def found_words():

    words = input("Введіть слова списку через пробіл: ").split()

    while True:
        search_word = input("Введіть слово для пошуку: ")

        if search_word in words:
            print(f"Слово '{search_word}' знайдено в списку!")
            break  
        else:
            print(f"Слово '{search_word}' не знайдено в списку. Спробуйте ще раз.")

    print(f"Весь список: {words}")

found_words()

def sum_char():
    digit_set = {str(i) for i in range(10)}  
    result = set() 

    while not result:  
        char = input("Введіть символи початкової множини через пробіл: ")
        char_set = set(char.split())  

        print(f"Початкова множина символів: {char_set}")
        print(f"Множина цифр: {digit_set}")

        result = char_set & digit_set  

        if result:
            print(f"Результуюча множина: {result}")
        else:
            print("Цифри не знайдені. Спробуйте ще раз.")

sum_char()