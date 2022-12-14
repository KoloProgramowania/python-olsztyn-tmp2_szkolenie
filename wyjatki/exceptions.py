def dodawanie(a, b):
    # assert isinstance(a, (int, float))
    # assert isinstance(b, (int, float))
    try:
        wynik = a + b
    except Exception as e:
        print(f"ERROR - {e=}")
        wynik = None

    return wynik


def dziel(a, b):
    try:
        wynik = a / b
    except ZeroDivisionError:
        return float("+inf")
    except TypeError:
        return "Tylko liczby"
    except Exception as e:
        print(e)
        return None

    return wynik


def dziel_t(a, b):
    try:
        wynik = a / b
    except ZeroDivisionError:
        return (False, float("+inf"))
    except TypeError:
        return (False, "Tylko liczby")
    except Exception as e:
        return (False, e)

    return (True, wynik)


c = dodawanie(1, 4)
d = dodawanie(1, "4")
print(dziel_t(1, 3))
print(dziel_t(1, 0))
print(dziel_t(1, "A"))
print(dziel_t("A", 4))

ok, wart = dziel_t(5, 6)
if ok:
    print(wart)
else:
    print("Error", wart)

ok, wart = dziel_t("A", 6)
if not ok:
    print("Error", wart)
else:
    print(wart)