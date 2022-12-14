#P TRÓJKĄTA = 1/2 · a · h

def pt_assert(a,h):
    assert isinstance(a, (int, float))
    assert isinstance(h, (int, float))
    wynik = 1/2*a*h
    return (wynik)


#print(pt_assert(20, 20))
#print(pt_assert(1, "a"))


def pt_try(a, h):
    try:
        wynik = 1/2*a*h
    except ZeroDivisionError:
        return (False, float("+inf"))
    except TypeError:
        return (False, "Tylko liczby")
    except Exception as e:
        return (False, e)

    return (True, wynik)

#print(pt_try(20, 50))
#print(pt_try(50, 0))
#print(pt_try(50, "s"))

def pt_try_min(a, h):
    try:
        wynik = 1/2*a*h
        if wynik < 30:
            wynik = float("+inf")
    except ZeroDivisionError:
        return (False, float("+inf"))
    except TypeError:
        return (False, "Tylko liczby")
    except Exception as e:
        return (False, e)

    return (True, wynik)

print(pt_try_min(20, 50))
print(pt_try_min(50, 0))
print(pt_try_min(50, "s"))