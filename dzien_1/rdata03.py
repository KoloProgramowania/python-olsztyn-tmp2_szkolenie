# program r3_00_read.py
# Pierwsze wczytywanie danych i walidacja - funkcja read_datas ostateczna


# Definiujemy funkcję wczytującą dane
def read_datas():
    def float_input(user_info, user_prompt, min_value):
        print("---[ wczytujemy dane]------------")
        print(user_info)
        user_input = input(user_prompt)
        if user_input.count(".") > 1:
            return None

        if not user_input.replace(".", "").isdecimal():
            return None

        user_value = float(user_input)
        if user_value < min_value:
            print(f"Wartość {user_value} jest mniejsza niż oczekiwana {min_value}.")
            return None
        return user_value

    h_start = None
    v_start = None

    while h_start is None:
        h_start = float_input(
            "Brak poprawnej wartości dla h_start. Typ float (np: 3.14)",
            "Teraz podaj wysokość początkową (w m, min. 10): ",
            10,
        )

    while v_start is None:
        v_start = float_input(
            "Brak poprawnej wartości dla v_start. Typ float (np: 3.14)",
            "Teraz podaj prędkość początkową (w m/sek, min. 2) :",
            2,
        )

    return (h_start, v_start)


initial_values = None
while initial_values is None:
    print("Proszę, podaj dane niezbędne do wygenerowania wykresu.")
    initial_values = read_datas()

print("OK, dane początkowe wczytane - działamy dalej.")
h,v = initial_values
print(f"{h=}, {v=}") #od Python 3.8

g=9.81
total_time = ((2*h)/g) **(1/2)
max_range = v * total_time
print(f"{total_time=}, {max_range=}")
