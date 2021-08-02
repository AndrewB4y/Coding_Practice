
"""

Calculations for espaditas critos combats

"""

traits_rel = {'fire': 'earth',
              'earth': 'lightning',
              'lightning': 'water',
              'water': 'fire'}

# COMBAT VARIABLES

bonus_power = 0  # Coming soon
# Hero Character variables

hero_power = 3660
hero_trait = 'water'

# *Character power is calculated depending if i align or not
# Unaligned character power (UCP): Calculated using the character's current level,
#  and the selected weapon without considering any elemental matching.
# Aligned character power (ACP): is calculated the same as UCP, except it takes
#  into account if any attributes match the character's element, or if the attribute is PWR

# weapon variables

# weapon_bonus_pwr = 0
weapon_trait = 'water'

# weapons could have up to three stats of different trait
weapon_power_stat1 = 239
weapon_trait_stat1 = 'earth'
weapon_power_stat2 = 0
weapon_trait_stat2 = 'traits[0]'
weapon_power_stat3 = 0
weapon_trait_stat3 = 'traits[0]'

# Enemy1 Character variables

enemy_power1 = 5349
enemy_trait1 = 'earth'

# Enemy2 Character variables

enemy_power2 = 5321
enemy_trait2 = 'lightning'

# Enemy3 Character variables

enemy_power3 = 5451
enemy_trait3 = 'lightning'

# Enemy4 Character variables

enemy_power4 = 5996
enemy_trait4 = 'earth'


if hero_trait != weapon_trait:
    # unaligned
    attribute_total = weapon_power_stat1 + weapon_power_stat2 + weapon_power_stat3
    power = (((attribute_total * 0.0025) + 1) * hero_power) + bonus_power
else:
    # aligned

    # weapon stat1 attribute calc
    if weapon_trait_stat1 != hero_trait:
        att1 = weapon_power_stat1 * 0.0025
    elif weapon_trait_stat1 == 'pwr':
        # equal to pwr
        att1 = weapon_power_stat1 * 0.002575
    elif weapon_trait_stat1 == hero_trait:
        att1 = weapon_power_stat1 * 0.002675

    # weapon stat2 attribute calc
    if weapon_trait_stat2 != hero_trait:
        att2 = weapon_power_stat2 * 0.0025
    elif weapon_trait_stat2 == 'pwr':
        # equal to pwr
        att2 = weapon_power_stat2 * 0.002575
    elif weapon_trait_stat2 == hero_trait:
        att2 = weapon_power_stat2 * 0.002675

    # weapon stat3 attribute calc
    if weapon_trait_stat3 != hero_trait:
        att3 = weapon_power_stat3 * 0.0025
    elif weapon_trait_stat3 == 'pwr':
        # equal to pwr
        att3 = weapon_power_stat3 * 0.002575
    elif weapon_trait_stat3 == hero_trait:
        att3 = weapon_power_stat3 * 0.002675

    # aligned power calc
    attribute_total = att1 + att2 + att3
    power = ((attribute_total + 1) * hero_power) + bonus_power
    orig_power = power

    aligned = 1

# ======================== Enemy 1 ========================
if aligned:
    # Trait bonus calc

    trait_bonus = 1
    if hero_trait == weapon_trait:
        trait_bonus += 0.075
    if traits_rel[hero_trait] == enemy_trait1:
        trait_bonus += 0.075
    if traits_rel[enemy_trait1] == hero_trait:
        trait_bonus -= 0.075
    power = orig_power * trait_bonus
    print(power)

min_power = int(power * 0.9)
max_power = int(power * 1.1)

min_enemy1 = int(enemy_power1 * 0.9)
max_enemy1 = int(enemy_power1 * 1.1)

if max_enemy1 > max_power:
    print("Aborte viejo, por debajo del 50%")

prob_enemy1 = (1 - (((max_enemy1 - min_power) / (max_power - min_power)) * ((max_enemy1 - min_power) / (max_enemy1 - min_enemy1)))) * 100

print(prob_enemy1)

# ======================== Enemy 2 ========================

if aligned:
    # Trait bonus calc

    trait_bonus = 1
    if hero_trait == weapon_trait:
        trait_bonus += 0.075
    if traits_rel[hero_trait] == enemy_trait2:
        trait_bonus += 0.075
    if traits_rel[enemy_trait2] == hero_trait:
        trait_bonus -= 0.075
    power = orig_power * trait_bonus
    print(power)

min_power = int(power * 0.9)
max_power = int(power * 1.1)

min_enemy2 = int(enemy_power2 * 0.9)
max_enemy2 = int(enemy_power2 * 1.1)

if max_enemy2 > max_power:
    print("Aborte viejo, por debajo del 50%")

prob_enemy2 = (1 - (((max_enemy2 - min_power) / (max_power - min_power)) * ((max_enemy2 - min_power) / (max_enemy2 - min_enemy2)))) * 100

print(prob_enemy2)


# ======================== Enemy 3 ========================

if aligned:
    # Trait bonus calc

    trait_bonus = 1
    if hero_trait == weapon_trait:
        trait_bonus += 0.075
    if traits_rel[hero_trait] == enemy_trait3:
        trait_bonus += 0.075
    if traits_rel[enemy_trait3] == hero_trait:
        trait_bonus -= 0.075
    power = orig_power * trait_bonus
    print(power)

min_power = int(power * 0.9)
max_power = int(power * 1.1)

min_enemy3 = int(enemy_power3 * 0.9)
max_enemy3 = int(enemy_power3 * 1.1)

if max_enemy3 > max_power:
    print("Aborte viejo, por debajo del 50%")

prob_enemy3 = (1 - (((max_enemy3 - min_power) / (max_power - min_power)) * ((max_enemy3 - min_power) / (max_enemy3 - min_enemy3)))) * 100

print(prob_enemy3)



# ======================== Enemy 4 ========================
if aligned:
    # Trait bonus calc

    trait_bonus = 1
    if hero_trait == weapon_trait:
        trait_bonus += 0.075
    if traits_rel[hero_trait] == enemy_trait4:
        trait_bonus += 0.075
    if traits_rel[enemy_trait4] == hero_trait:
        trait_bonus -= 0.075
    power = orig_power * trait_bonus
    print(power)

min_power = int(power * 0.9)
max_power = int(power * 1.1)

min_enemy4 = int(enemy_power4 * 0.9)
max_enemy4 = int(enemy_power4 * 1.1)

if max_enemy4 > max_power:
    print("Aborte viejo, por debajo del 50%")

prob_enemy4 = (1 - (((max_enemy4 - min_power) / (max_power - min_power)) * ((max_enemy4 - min_power) / (max_enemy4 - min_enemy4)))) * 100

print(prob_enemy4)
