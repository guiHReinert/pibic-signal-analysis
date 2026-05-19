

def line1(n=40, color=''):
    print(color + '=-' * (n // 2) + '=')


def line2(n=40, color=''):
    print(color + '=' * n)


def title1(txt, color=''):
    print(color + f"{'='.join(txt):=^100}".upper())


def title2(txt, n=40, color=''):
    print(color + '<' + '=' * n + '>')
    print(txt.center(n))
    print('<' + '=' * n + '>\033[m')
