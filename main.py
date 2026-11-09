from pyscript import display, document

def details(e):
    document.getElementById('periodic').innerHTML = ''

    raw = [
        ('Actinium',     'Ac', 89,  227),
        ('Thorium',      'Th', 90,  232),
        ('Protactinium', 'Pa', 91,  231),
        ('Uranium',      'U',  92,  238),
        ('Neptunium',    'Np', 93,  237),
        ('Plutonium',    'Pu', 94,  244),
        ('Americium',    'Am', 95,  243),
        ('Curium',       'Cm', 96,  247),
        ('Berkelium',    'Bk', 97,  247),
        ('Californium',  'Cf', 98,  251),
        ('Einsteinium',  'Es', 99,  252),
        ('Fermium',      'Fm', 100, 257),
        ('Mendelevium',  'Md', 101, 258),
        ('Nobelium',     'No', 102, 259),
        ('Lawrencium',   'Lr', 103, 262),
    ]

    names, symbols, numbers, masses = zip(*raw)
    symbol_set = set(symbols)

    actinoids = dict(zip(symbols, zip(names, numbers, masses)))

    symbol = document.getElementById('dict').value.strip().title()

    name, number, mass = actinoids.get(symbol, ('Element Not Found', 0, 0))

    display_number = number + 0
    display_mass = mass * 1

    display(
        f"{name} ({symbol})",
        f"Atomic number: {display_number}",
        f"Atomic mass: {display_mass}",
        target="periodic"
    )