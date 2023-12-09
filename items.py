from abc import ABC, abstractmethod
from stats import Stats

class Stuff:
      
    def __init__(self, slot_1=None, slot_2=None, slot_3=None, slot_4=None, slot_5=None, slot_6=None):
        self.slot_1 = slot_1
        self.slot_2 = slot_2
        self.slot_3 = slot_3
        self.slot_4 = slot_4
        self.slot_5 = slot_5
        self.slot_6 = slot_6
    
    def compute_health(self):
        return self.slot_1.stat.health + self.slot_2.stat.health + self.slot_3.stat.health + self.slot_4.stat.health + self.slot_5.stat.health + self.slot_6.stat.health
    
    def compute_health_regeneration(self):
        pass
    
    def compute_mana(self):
        return self.slot_1.stat.mana + self.slot_2.stat.mana + self.slot_3.stat.mana + self.slot_4.stat.mana + self.slot_5.stat.mana + self.slot_6.stat.mana
    
    def compute_mana_regeneration(self):
        return self.slot_1.stat.mana_regeneration + self.slot_2.stat.mana_regeneration + self.slot_3.stat.mana_regeneration + self.slot_4.stat.mana_regeneration + self.slot_5.stat.mana_regeneration + self.slot_6.stat.mana_regeneration

    def compute_attack_damage(self):
        return self.slot_1.stat.attack_damage + self.slot_2.stat.attack_damage + self.slot_3.stat.attack_damage + self.slot_4.stat.attack_damage + self.slot_5.stat.attack_damage + self.slot_6.stat.attack_damage

    def compute_attack_speed(self):
        pass

    def compute_attack_range(self):
        pass

    def compute_critical_strike_chance(self):
        pass

    def compute_ability_power(self):
        pass

    def compute_magic_penetration(self):
        pass

    def compute_cooldown_reduction(self):
        pass

    def compute_armor(self):
        pass

    def compute_magic_resist(self):
        pass

    def compute_movement_speed(self):
        pass

    def compute_tenacity(self):
        pass

    def compute_life_steal(self):
        pass

    def compute_omnivamp(self):
        pass

    def compute_armor_penetration(self):
        pass

    def __repr__(self):
        return f"Stuff(slot_1={self.slot_1}, slot_2={self.slot_2}, slot_3={self.slot_3}, slot_4={self.slot_4}, slot_5={self.slot_5}, slot_6={self.slot_6})"     

class Item(ABC):

    def __init__(self, name : str, description : str, stat : Stats, **kwargs):
        self.name = name
        self.description = description
        self.stat = stat
        self.__dict__.update(kwargs)
    
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def stats(self):
        pass
    
class TankItem(Item, ABC):
    
        def __init__(self, name : str, description : str, stat : Stats, **kwargs):
            super().__init__(name, description, stat, **kwargs)
            
class SupportItem(Item, ABC):
    
        def __init__(self, name : str, description : str, stat : Stats, **kwargs):
            super().__init__(name, description, stat, **kwargs)

class FighterItem(Item, ABC):
    
        def __init__(self, name : str, description : str, stat : Stats, **kwargs):
            super().__init__(name, description, stat, **kwargs)

class MageItem(Item, ABC):
    
        def __init__(self, name : str, description : str, stat : Stats, **kwargs):
            super().__init__(name, description, stat, **kwargs)

class AssassinItem(Item, ABC):
    
        def __init__(self, name : str, description : str, stat : Stats, **kwargs):
            super().__init__(name, description, stat, **kwargs)   

class ShooterItem(Item, ABC):
    
        def __init__(self, name : str, description : str, stat : Stats, **kwargs):
            super().__init__(name, description, stat,  **kwargs)   
        
class BootsItem(Item, ABC):
        
        def __init__(self, name : str, description : str, stat : Stats, **kwargs):
            super().__init__(name, description, stat, **kwargs)

class ConsumableItem(Item, ABC):
            
        def __init__(self, name : str, description : str, stat : Stats, **kwargs):
            super().__init__(name, description, stat, **kwargs)