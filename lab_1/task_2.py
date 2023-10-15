free_space = 1.44   # Mbyte
symbol = (4 / 1024) / 1024  # Mbyte
strings_number = 50
pages_number = 100
symbols_number = 25

book = symbol * symbols_number * strings_number * pages_number
print(round(free_space // book))
