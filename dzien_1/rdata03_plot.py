import matplotlib.pyplot as plt

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
            "Teraz podaj prędność początkową (w m/sek, min. 2) :",
            2,
        )

    return (h_start, v_start)

initial_values = None
while initial_values is None:
    print("Podaj dane:")
    initial_values = read_datas()

print(f"Wczytano: {initial_values}")


# Rozpakowywanie tupli
H_START, V_START = initial_values

print(f"{H_START=}, {V_START=}")  # od Python 3.8
print("OK, dane początkowe wczytane - działamy dalej.")

# Obliczamy najważniejsze wartości

g = 9.81  # m/s^2
total_time = ((2 * H_START) / g) ** (1 / 2)
max_range = V_START * total_time


# dodajemy wykres i umieszczamy punkt startu i spadku
title = f"""Wykres rzutu poziomego z V_START = {V_START} m/s (g = {g} m/s^2)
        Czas lotu = {round(total_time,4)} s."""

plt.scatter(0, H_START, label=f"H_START={H_START} m")
plt.scatter(max_range, 0, label=f"max_range={round(max_range,3)} m")
plt.grid()
plt.title(title)

plt.legend()
plt.show()

