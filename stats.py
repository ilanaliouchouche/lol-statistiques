from typing import Any, Tuple
from items import Stuff

class Stats:

    def __init__(self, health : int, health_regeneration : int , mana : int, mana_regeneration : int,
                 attack_damage : int, attack_speed : float, attack_range : int, critical_strike_chance : int,
                 ability_power : int, magic_penetration : Tuple[int,int], cooldown_reduction : int, armor : int, magic_resist : int, movement_speed : int,
                 tenacity : int, life_steal : int, omnivamp : int, armor_penetration : Tuple[int, int], **kwargs):
        
        self.health = health
        self.health_regeneration = health_regeneration
        self.mana = mana
        self.mana_regeneration = mana_regeneration
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        self.critical_strike_chance = critical_strike_chance
        self.ability_power = ability_power
        self.magic_penetration = magic_penetration
        self.cooldown_reduction = cooldown_reduction
        self.armor = armor
        self.magic_resist = magic_resist
        self.movement_speed = movement_speed
        self.tenacity = tenacity
        self.life_steal = life_steal
        self.omnivamp = omnivamp
        self.armor_penetration = armor_penetration
        self.__dict__.update(kwargs)

class ChampionStats(Stats):

    def __init__(self, stuff : Stuff, **kwargs):
        pass
        
