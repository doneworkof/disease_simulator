from random import uniform
from utils import *

class Bacteria:
    def __init__(self, name, formula, delta=1):
        # Уровень развития бактерии
        self.level = 0
        # Скорость развития болезни
        self.delta = delta
        # Имя болезни
        self.name = name
        # Формула подсчёта урона
        self.formula = formula
        # Показатель жизни
        self.alive = True

    def downgrade(self, amount):
        # Совершаем деградацию заболевания
        self.level -= amount
        if self.level < 0 and self.alive:
            self.alive = False

    def slow_down(self, amount):
        # Замедляем процесс развития заболевания
        self.delta = max(0, self.delta - amount)

    def tick(self):
        # Обновляем болезнь и возвращаем урон
        self.level += self.delta
        return self.formula(self.level)

class Immune:
    def __init__(self, owner, strength=None):
        # Сила иммунитета, F ∈ [0; 1]
        self.strength = strength or uniform(0, 1)
        # Владелец иммунитета
        self.owner = owner

    def downgrade_bacterias(self):
        # Просчёт действия иммунитета
        # На каждое из заболеваний
        for bacteria in self.owner.bacterias:
            alpha = self.strength ** 2
            level_dgrad = alpha / 2
            bacteria.downgrade(level_dgrad)
            delta_dgrad = alpha / 4
            bacteria.slow_down(delta_dgrad)

    def delete_dead_bacterias(self):
        # Удаление мёртвых болезней
        delete_indices = [
            i for i, b in enumerate(
                self.owner.bacterias
            ) if not b.alive
        ]

        for i in delete_indices[::-1]:
            self.owner.bacterias.pop(i)

    def heal_owner(self):
        # Автоматическое лечение человека
        delta_hp = self.strength * 0.9
        self.owner.heal(delta_hp)

    def tick(self):
        # Обновление иммунитета
        if not self.owner.alive:
            return

        self.downgrade_bacterias()
        self.delete_dead_bacterias()
        self.heal_owner()


