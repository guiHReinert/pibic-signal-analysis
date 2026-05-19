

def bool_int(n):
    if n.replace('-', '').isnumeric():
        return True
    else:
        return False


def bool_float(n, c=False):
    if n is float() and not c:
        return True
    elif n.replace(',', '.') is float() and c:
        return True
    else:
        return False


def read_int(txt, wrong_txt='\033[31mERROR! Please, insert a valid integer number\033[m',
             no_txt='\033[31mThe user chose not to register the value.\033[m'):
    while True:
        try:
            n = int(input(txt).strip())
            return int(n)

        except (ValueError, TypeError):
            print(wrong_txt)

        except KeyboardInterrupt:
            print(no_txt)


def read_float(txt, wrong_txt='\033[31mERROR! Please, insert a valid numeric value\033[m',
               no_txt='\033[31mThe user chose do not register the value.\033[m'):
    while True:
        try:
            n = input(txt).strip()
            return float(n.replace(',', '.'))

        except (ValueError, TypeError):
            print(wrong_txt)

        except KeyboardInterrupt:
            print(no_txt)


def read_coin(txt, wrong_txt='\033[31mERROR! Please, insert a valid numeric value\033[m',
              no_txt='\033[31mThe user chose do not register the value.\033[m'):
    while True:
        try:
            n = input(txt).strip()
            return float(n.replace(',', '.'))

        except (ValueError, TypeError):
            print(wrong_txt)

        except KeyboardInterrupt:
            print(no_txt)
