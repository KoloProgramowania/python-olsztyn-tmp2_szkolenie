def read_datas():
    h_start = float(input("Teraz podaj wysokość początkową w m [>10m] "))
    v_start = float(input("Teraz podaj prędkość początkową w m/s [>2m/s]"))

    if h_start < 10:
        print("niestety wysokość zbyt niska")
        return None

    if v_start < 2:
        print("niestety prędkość za mała")
        return None
    return (h_start , v_start)

initial_values = None
while initial_values is None:
    print("Podaj dane")
    initial_values=read_datas()



print(f": {initial_values}")
h,v = initial_values
print(f"{h=}, {v=}") #od Python 3.8
