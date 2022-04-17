from chemistry import *


class Human:
    def __init__(self, name, immune_strength=None):
        # Имя человека
        self.name = name
        # Единицы здоровья
        self.hp = 100
        # Список заболеваний
        self.bacterias = []
        # Показатель жизни
        self.alive = True
        # Инициализируем иммунитет
        self.immune = Immune(self, immune_strength)

    def damage(self, amount):
        # Наносим урон человеку
        self.hp -= amount
        if self.hp < 0 and self.alive:
            self.alive = False
            print(f'Гражданин {self.name} трагично умер.')

    def infect(self, bacteria):
        # Заражаем человека
        self.bacterias.append(bacteria)

    def heal(self, amount):
        # Исцеляем человека (максимальное HP равно 100)
        self.hp = min(self.hp + amount, 100)

    def tick(self):
        # Обновление человека,
        # Обработка заболеваний

        for bacteria in self.bacterias:
            delta_health = bacteria.tick()
            self.damage(delta_health)

        # Действия иммунитета
        self.immune.tick()
        