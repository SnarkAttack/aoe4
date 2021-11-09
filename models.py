from os import SCHED_OTHER
from posix import ST_NOEXEC
from django.db import models
from django.db.models.fields.related import ForeignObject

class Player(models.Model):
    username = models.CharField(max_length=32)

class MatchPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    team = models.IntegerField()
    
class AoEMatchStats(models.Model):
    pass

class PlayerMatchStats(models.Model):
    match_player = models.ForeignKey(MatchPlayer, on_delete=models.CASCADE)
    match = models.ForeignKey(AoEMatchStats, on_delete=models.CASCADE)

class PlayerCategoryStats(models.Model):
    match_stats = models.ForeignKey(PlayerMatchStats, on_delete=models.CASCADE)

class PlayerMatchMilitaryStats(PlayerCategoryStats):
    score = models.IntegerField()
    units_killed = models.IntegerField()
    units_lost = models.IntegerField()
    buildings_razed = models.IntegerField()
    buildings_lost = models.IntegerField()
    largest_army = models.IntegerField()

class PlayerMatchEconomyStats(PlayerCategoryStats):
    score = models.IntegerField()
    food = models.IntegerField()
    wood = models.IntegerField()
    stone = models.IntegerField()
    gold = models.IntegerField()
    max_food_per_min = models.IntegerField()
    max_wood_per_min = models.IntegerField()

class PlayerMatchTechnologyStats(PlayerCategoryStats):
    score = models.IntegerField()
    time_to_age_2 = models.TimeField()
    time_to_age_3 = models.TimeField()
    time_to_age_4 = models.TimeField()
    map_explored = models.IntegerField()
    research_count = models.IntegerField()

class PlayerMatchSocietyStats(PlayerCategoryStats):
    score = models.IntegerField()
    relics_captured = models.IntegerField()
    villager_high = models.IntegerField()
    avg_villager_idle = models.TimeField()
    avg_unit_lifespan = models.TimeField()