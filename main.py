# Импортируем нужные библиотеки
from chemistry import *
from human import *
from math import * 
from matplotlib import pyplot as plt

# Создаём человека
human = Human('Василий', immune_strength=0.9)

# Создаём болезнь
cholera = Bacteria('Холера', lambda l: abs(10 * sin(l) + 0.5 * l))

# Заражаем человека
human.infect(cholera)

health_history = []

for i in range(100):
    # Обновляем человека
    human.tick()
    
    if not human.alive:
        break

    current_hp = human.hp
    is_infected = len(human.bacterias) > 0
    
    print('-' * 15)
    print('День', i)
    print(f'Здоровье: {current_hp} единиц')
    print(f'Василий {"болен" if is_infected else "здоров"}')
    
    health_history.append(current_hp)

# Строим график единиц HP
plt.plot(health_history)
plt.show()