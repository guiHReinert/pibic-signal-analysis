

def coin(n=0):
    """
    -> A function that format a float or int value to a coin value, in R$
    :param n: The num to be formatted
    :return: The formatted num in str, in R$
    """
    r = ('R$' + str(round(n, 2))).replace('.', ',')
    return r


def double(n=0, c=False):
    """
    -> A function that doubles and format a float or int value to a coin value, in R$
    :param n: The num to be formatted
    :param c: (optional) The bool that determines the coin-formatting, in R$
    :return: The number doubled and coin-formatted
    """
    n *= 2
    return n if c is False else coin(n)


def half(n=0, c=False):
    """
    -> A function that cut in half and format a float or int values to a coin value, in R$
    :param n: The number to be formatted
    :param c: (optional) The bool that determines the coin-formatting, in R$
    :return: The number cut in half and coin-formatted
    """
    n /= 2
    return n if c is False else coin(n)


def increase(n=0, p=100, c=False):
    """
    -> A function that increases a float or int number by a percentage and format it in a coin value, in R$
    :param n: The number to be formatted
    :param p: The percentage that increase the number
    :param c: (optional) The bool that determines the coin-formatting, in R$
    :return: The number increased and coin-formatted
    """
    n += n * (p / 100)
    return n if c is False else coin(n)


def decrease(n=0, p=100, c=False):
    """
    -> A function that decreases a float or int number by a percentage and format it in a coin value, in R$
    :param n: The number to be formatted
    :param p: The percentage that decrease the number
    :param c: (optional) The bool that determines the coin-formatting, in R$
    :return: The number decreased and coin-formatted
    """
    n -= n * (p / 100)
    return n if c is False else coin(n)


def resume(n=0, color=''):
    """
    -> A function that build a chart organizing a lot of mathematical coin-operations based in a float or int number
    :param n: The number to be used
    :param color: (optional) A single str that colors the chart
    :return: The chart with a lot of mathematical coin-operations based in the number
    """
    print(color + '=' * 39 + '>')
    print(f"{' '.join('price resume'):^40}".upper())
    print('=' * 39 + '>')

    print("Price Analysed:      " + f'{coin(n): <20}')
    print("Double-Price:        " + f"{double(n, True): <20}")
    print("Half-Price:          " + f'{half(n, True): <20}')
    print("88% Increased:       " + f'{increase(n, 88, True): <20}')
    print("35% Decreased:       " + f'{decrease(n, 35, True): <20}')

    print('=' * 39 + '>')
