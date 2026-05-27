# fix clicker scaling and add it to others buttons - DONE
# add more content - DONE
    # enemy progressions - DONE
    # more upgrades - DONE
        # -1 mobs needed  # 5 - DONE
        # - 5% cost of upgrades, 1 % per upgrade # 4 - DONE
        # + 50% DPS per upgrade, 5 upgrade max  # 1 - DONE
        #  + 10% gold per upgrade, 5 upgrades  # 3 - DONE
        # + 20 % DPC per upgrade, 5 upgrades # 2 - DONE
    # add Prestige - DONE
        # Prestige - DONE
        # prestige tokens give 1% dmg - DONE
        # prestige upgrade - DONE
            # 50% more money, 10 upgrades # 2 💎 - DONE
            # -1 mobs needed, 4 upgrades # 4 ⚡ - DONE
            # +2x dmg, 25 upgrades # 1 💥 - DONE
            # prestige token gain +0,2x, 5 upgrades # 3🔮 - DONE
    # achievements - NAH
# add sound effects - NAH
# improve ui - NAH
# add save - DONE
# animations - DONE
# screens ui ex. menu shop
# auto next wave - DONE
# auto clicker - DONE
# page 1 and 2 for upgrades - DONE
# fix the positions and add more emojis and the square sizes - DONE

# fix the prestige dmg multi - DONE
# Add dmg per click more smoothly over the enemy - DONE
# fix back - IDK For me works

# add a boss system
# add skill tree for the 4 gui - DONE
    # 3 paths - DONE
        # damage - DONE
            # brutal clicks, +10% click_damage_multi per level - DONE
            # Burning Core +15% damage_per_second_multi per level - DONE
            # Critical Surge 10% chance to deal 2x total damage - DONE
            # Combo System each click within short time = stacking damage bonus - DONE
            # final upgrade:
                # Executioner enemies under 30% HP take +50% damage
        # economy - DONE
            # Golden Touch +10% money_multiplier per level - DONE
            # Market Knowledge reduces discount (ALL upgrades cheaper) - DONE
            # bounty system every x enemy +2x gold a chance for double gold - DONE
            # clicking an enemy gives 1% of the gold gain for the wave - DONE
            # final upgrade:
                # Greed engine for every wave give a gold multi of 1% to gold gain - DONE
        # progression - DONE
            # auto click core unlocks auto click - DONE
            # overclocked clicker increase the speed of the auto click - DONE
            # smart targeting increase the dmg of the auto click +0,2x - DONE
            # unlocks auto next - DONE
            # final upgrade:
                # overdrive every 30s either 2x dmg or 1.5x click speed of the auto click for 10 s - DONE
# add lines, the rest of the skill tree, the prices, the description and everything else - DONE
# add all things from the skill tree to save and load - DONE

# fix the skill tree prog path 5 showing for 1 frame - DONE


import json
import os
import sys
import time

import pygame
import random


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath("")

    return os.path.join(base_path, relative_path)

save_dir = os.path.join(os.getenv("APPDATA"), "TwojaGra")
os.makedirs(save_dir, exist_ok=True)

save_path = os.path.join(save_dir, "save.json")

def notation(number):
    if 1000 <= number <= 999999:
        number_display_k = round(number / 1000,2)
        return f"{number_display_k}K"
    elif 1000000 <= number <= 999999999:
        number_display_m = round(number / 1000000,2)
        return f"{number_display_m}M"
    elif 1000000000 <= number <= 999999999999:
        number_display_b = round(number / 1000000000,2)
        return f"{number_display_b}B"
    elif 1000000000000 <= number <= 999999999999999:
        number_display_t = round(number / 1000000000000,2)
        return f"{number_display_t}T"
    elif 1000000000000000 <= number <= 999999999999999999:
        number_display_qa = round(number / 1000000000000000,2)
        return f"{number_display_qa}QA"
    elif 1000000000000000000 <= number <= 999999999999999999999:
        number_display_qi = round(number / 1000000000000000000,2)
        return f"{number_display_qi}QI"
    elif 1000000000000000000000 <= number <= 999999999999999999999999:
        number_display_se = round(number / 1000000000000000000000,2)
        return f"{number_display_se}SE"
    elif 1000000000000000000000000 <= number <= 999999999999999999999999999:
        number_display_sp = round(number / 1000000000000000000000000,2)
        return f"{number_display_sp}SP"
    elif 1000000000000000000000000000 <= number <= 999999999999999999999999999999:
        number_display_oc = round(number / 1000000000000000000000000000,2)
        return f"{number_display_oc}OC"
    elif 1000000000000000000000000000000 <= number <= 999999999999999999999999999999999:
        number_display_no = round(number / 1000000000000000000000000000000,2)
        return f"{number_display_no}NO"
    elif 1000000000000000000000000000000000 <= number <= 999999999999999999999999999999999999:
        number_display_de = round(number / 1000000000000000000000000000000000,2)
        return f"{number_display_de}DE"
    else:
        return round(number,2)
# black outline
def draw_text_with_outline(surface, text1, font, text_color, outline_color, pos):
    x1, y1 = pos

    # outline
    for dx in [-2, -1, 0, 1, 2]:
        for dy in [-2, -1, 0, 1, 2]:
            if dx != 0 or dy != 0:
                outline = font.render(text1, True, outline_color)
                surface.blit(outline, (x1 + dx, y1 + dy))

    # main text
    text_surface = font.render(text1, True, text_color)
    surface.blit(text_surface, (x1, y1))

def save_game():
    data = {
        "button_1_cost": button_1_cost,
        "button_2_cost": button_2_cost,
        "button_3_cost": button_3_cost,
        "button_4_cost": button_4_cost,
        "button_5_cost": button_5_cost,
        "button_6_cost": button_6_cost,
        "button_7_cost": button_7_cost,
        "button_8_cost": button_8_cost,
        "button_9_cost": button_9_cost,
        "button_10_cost": button_10_cost,

        "button_upgrade_1_cost": button_upgrade_1_cost,
        "button_upgrade_2_cost": button_upgrade_2_cost,
        "button_upgrade_3_cost": button_upgrade_3_cost,
        "button_upgrade_4_cost": button_upgrade_4_cost,
        "button_upgrade_5_cost": button_upgrade_5_cost,

        "button_prestige_upgrade_1_cost": button_prestige_upgrade_1_cost,
        "button_prestige_upgrade_2_cost": button_prestige_upgrade_2_cost,
        "button_prestige_upgrade_3_cost": button_prestige_upgrade_3_cost,
        "button_prestige_upgrade_4_cost": button_prestige_upgrade_4_cost,

        "max_health": max_health,

        "click_damage": click_damage,
        "click_damage_multi": click_damage_multi,
        "damage_per_second": damage_per_second,
        "damage_per_second_multi": damage_per_second_multi,

        "base_gain": base_gain,
        "gold": gold,
        "money_multiplier": money_multiplier,
        "discount": discount,

        "prestige_tokens": prestige_tokens,
        "prestige_tokens_gain": prestige_tokens_gain,
        "prestige_tokens_multiplier": prestige_tokens_multiplier,
        "prestige_dmg_multi": prestige_dmg_multi,
        "prestige_upgrade_dmg_multi": prestige_upgrade_dmg_multi,
        "prestige_upgrade_money_multi": prestige_upgrade_money_multi,

        "prestige_enemy_red": prestige_enemy_red,

        "next_clicker_is": next_clicker_is,
        "auto_next_is": auto_next_is,
        "auto_click_is": auto_click_is,

        "wave": wave,
        "best_wave": best_wave,
        "enemies_had": enemies_had,

        "button_1_limit_had": button_1_limit_had,
        "button_2_limit_had": button_2_limit_had,
        "button_3_limit_had": button_3_limit_had,
        "button_4_limit_had": button_4_limit_had,
        "button_5_limit_had": button_5_limit_had,
        "button_6_limit_had": button_6_limit_had,
        "button_7_limit_had": button_7_limit_had,
        "button_8_limit_had": button_8_limit_had,
        "button_9_limit_had": button_9_limit_had,
        "button_10_limit_had": button_10_limit_had,

        "button_upgrade_1_limit_had": button_upgrade_1_limit_had,
        "button_upgrade_2_limit_had": button_upgrade_2_limit_had,
        "button_upgrade_3_limit_had": button_upgrade_3_limit_had,
        "button_upgrade_4_limit_had": button_upgrade_4_limit_had,
        "button_upgrade_5_limit_had": button_upgrade_5_limit_had,

        "button_prestige_upgrade_1_limit_had": button_prestige_upgrade_1_limit_had,
        "button_prestige_upgrade_2_limit_had": button_prestige_upgrade_2_limit_had,
        "button_prestige_upgrade_3_limit_had": button_prestige_upgrade_3_limit_had,
        "button_prestige_upgrade_4_limit_had": button_prestige_upgrade_4_limit_had,

        # tu

        "skill_points": skill_points,
        "enemies_needed_skill_tree_had": enemies_needed_skill_tree_had,

        "skill_tree_dpc_multi":skill_tree_dpc_multi,
        "skill_tree_dps_multi": skill_tree_dps_multi,
        "skill_tree_money_multi": skill_tree_money_multi,
        "skill_tree_discount":skill_tree_discount,
        "skill_tree_wave_multi":skill_tree_wave_multi,
        "skill_tree_overdrive_dmg_multi":skill_tree_overdrive_dmg_multi,
        "skill_tree_overdrive_speed_multi": skill_tree_overdrive_speed_multi,

        "skill_tree_unlock_limit_had":skill_tree_unlock_limit_had,

        "skill_tree_dmg_path_1_limit_had": skill_tree_dmg_path_1_limit_had,
        "skill_tree_dmg_path_2_limit_had": skill_tree_dmg_path_2_limit_had,
        "skill_tree_dmg_path_3_limit_had": skill_tree_dmg_path_3_limit_had,
        "skill_tree_dmg_path_4_limit_had": skill_tree_dmg_path_4_limit_had,
        "skill_tree_dmg_path_5_limit_had": skill_tree_dmg_path_5_limit_had,

        "skill_tree_eco_path_1_limit_had": skill_tree_eco_path_1_limit_had,
        "skill_tree_eco_path_2_limit_had": skill_tree_eco_path_2_limit_had,
        "skill_tree_eco_path_3_limit_had": skill_tree_eco_path_3_limit_had,
        "skill_tree_eco_path_4_limit_had": skill_tree_eco_path_4_limit_had,
        "skill_tree_eco_path_5_limit_had": skill_tree_eco_path_5_limit_had,

        "skill_tree_prog_path_1_limit_had": skill_tree_prog_path_1_limit_had,
        "skill_tree_prog_path_2_limit_had": skill_tree_prog_path_2_limit_had,
        "skill_tree_prog_path_3_limit_had": skill_tree_prog_path_3_limit_had,
        "skill_tree_prog_path_4_limit_had": skill_tree_prog_path_4_limit_had,
        "skill_tree_prog_path_5_limit_had": skill_tree_prog_path_5_limit_had,

        "combo":combo,
        "last_click_time":last_click_time,
        "click_combo_multi":click_combo_multi,
        "combo_add":combo_add,

        "overdrive_active":overdrive_active,
        "overdrive_type":overdrive_type,

        "skill_tree_unlock_color":skill_tree_unlock_color,

        "skill_tree_eco_path_1_color":skill_tree_eco_path_1_color,
        "skill_tree_eco_path_2_color": skill_tree_eco_path_2_color,
        "skill_tree_eco_path_3_color": skill_tree_eco_path_3_color,
        "skill_tree_eco_path_4_color": skill_tree_eco_path_4_color,
        "skill_tree_eco_path_5_color": skill_tree_eco_path_5_color,

        "skill_tree_dmg_path_1_color": skill_tree_dmg_path_1_color,
        "skill_tree_dmg_path_2_color": skill_tree_dmg_path_2_color,
        "skill_tree_dmg_path_3_color": skill_tree_dmg_path_3_color,
        "skill_tree_dmg_path_4_color": skill_tree_dmg_path_4_color,
        "skill_tree_dmg_path_5_color": skill_tree_dmg_path_5_color,

        "skill_tree_prog_path_1_color": skill_tree_prog_path_1_color,
        "skill_tree_prog_path_2_color": skill_tree_prog_path_2_color,
        "skill_tree_prog_path_3_color": skill_tree_prog_path_3_color,
        "skill_tree_prog_path_4_color": skill_tree_prog_path_4_color,
        "skill_tree_prog_path_5_color": skill_tree_prog_path_5_color,

        "current_index":current_index,

    }
    with open("save.json", "w") as f:
        json.dump(data, f)

def load_game():
    global button_1_cost, button_2_cost, button_3_cost, button_4_cost,button_5_cost, button_6_cost, button_7_cost, button_8_cost, button_9_cost, button_10_cost
    global button_upgrade_1_cost, button_upgrade_2_cost, button_upgrade_3_cost, button_upgrade_4_cost, button_upgrade_5_cost
    global button_prestige_upgrade_1_cost, button_prestige_upgrade_2_cost, button_prestige_upgrade_3_cost, button_prestige_upgrade_4_cost
    global max_health, click_damage, click_damage_multi, damage_per_second, damage_per_second_multi, base_gain, gold, money_multiplier, discount
    global prestige_tokens, prestige_tokens_gain, prestige_tokens_multiplier, prestige_dmg_multi, prestige_upgrade_dmg_multi, prestige_upgrade_money_multi
    global prestige_enemy_red, next_clicker_is, auto_next_is, auto_click_is, wave, best_wave, enemies_had
    global button_1_limit_had, button_2_limit_had, button_3_limit_had, button_4_limit_had, button_5_limit_had, button_6_limit_had, button_7_limit_had
    global button_8_limit_had, button_9_limit_had, button_10_limit_had, button_upgrade_1_limit_had, button_upgrade_2_limit_had, button_upgrade_3_limit_had
    global button_upgrade_4_limit_had, button_upgrade_5_limit_had, button_prestige_upgrade_1_limit_had, button_prestige_upgrade_2_limit_had
    global button_prestige_upgrade_3_limit_had, button_prestige_upgrade_4_limit_had

    global skill_points,enemies_needed_skill_tree_had,skill_tree_dpc_multi,skill_tree_dps_multi,skill_tree_money_multi,skill_tree_discount,skill_tree_wave_multi
    global skill_tree_overdrive_dmg_multi,skill_tree_overdrive_speed_multi,skill_tree_unlock_limit_had,skill_tree_dmg_path_1_limit_had,skill_tree_dmg_path_2_limit_had,skill_tree_dmg_path_3_limit_had
    global skill_tree_dmg_path_4_limit_had,skill_tree_dmg_path_5_limit_had,skill_tree_eco_path_1_limit_had,skill_tree_eco_path_2_limit_had,skill_tree_eco_path_3_limit_had
    global skill_tree_eco_path_4_limit_had,skill_tree_eco_path_5_limit_had,skill_tree_prog_path_1_limit_had,skill_tree_prog_path_2_limit_had,skill_tree_prog_path_3_limit_had
    global skill_tree_prog_path_4_limit_had,skill_tree_prog_path_5_limit_had,combo,last_click_time,click_combo_multi,combo_add,overdrive_active,overdrive_type
    global skill_tree_unlock_color,skill_tree_eco_path_1_color,skill_tree_eco_path_2_color,skill_tree_eco_path_3_color,skill_tree_eco_path_4_color,skill_tree_eco_path_5_color
    global skill_tree_dmg_path_1_color,skill_tree_dmg_path_2_color,skill_tree_dmg_path_3_color,skill_tree_dmg_path_4_color,skill_tree_dmg_path_5_color
    global skill_tree_prog_path_1_color,skill_tree_prog_path_2_color,skill_tree_prog_path_3_color,skill_tree_prog_path_4_color,skill_tree_prog_path_5_color,current_index

    if os.path.exists("save.json"):
        with open("save.json", "r") as f:
            data = json.load(f)

            button_1_cost = data["button_1_cost"]
            button_2_cost = data["button_2_cost"]
            button_3_cost = data["button_3_cost"]
            button_4_cost = data["button_4_cost"]
            button_5_cost = data["button_5_cost"]
            button_6_cost = data["button_6_cost"]
            button_7_cost = data["button_7_cost"]
            button_8_cost = data["button_8_cost"]
            button_9_cost = data["button_9_cost"]
            button_10_cost = data["button_10_cost"]

            button_upgrade_1_cost = data["button_upgrade_1_cost"]
            button_upgrade_2_cost = data["button_upgrade_2_cost"]
            button_upgrade_3_cost = data["button_upgrade_3_cost"]
            button_upgrade_4_cost = data["button_upgrade_4_cost"]
            button_upgrade_5_cost = data["button_upgrade_5_cost"]

            button_prestige_upgrade_1_cost = data["button_prestige_upgrade_1_cost"]
            button_prestige_upgrade_2_cost = data["button_prestige_upgrade_2_cost"]
            button_prestige_upgrade_3_cost = data["button_prestige_upgrade_3_cost"]
            button_prestige_upgrade_4_cost = data["button_prestige_upgrade_4_cost"]

            max_health = data["max_health"]

            click_damage = data["click_damage"]
            click_damage_multi = data["click_damage_multi"]
            damage_per_second = data["damage_per_second"]
            damage_per_second_multi = data["damage_per_second_multi"]

            base_gain = data["base_gain"]
            gold = data["gold"]
            money_multiplier = data["money_multiplier"]
            discount = data["discount"]

            prestige_tokens = data["prestige_tokens"]
            prestige_tokens_gain = data["prestige_tokens_gain"]
            prestige_tokens_multiplier = data["prestige_tokens_multiplier"]
            prestige_dmg_multi = data["prestige_dmg_multi"]
            prestige_upgrade_dmg_multi = data["prestige_upgrade_dmg_multi"]
            prestige_upgrade_money_multi = data["prestige_upgrade_money_multi"]

            prestige_enemy_red = data["prestige_enemy_red"]

            next_clicker_is = data["next_clicker_is"]
            auto_next_is = data["auto_next_is"]
            auto_click_is = data["auto_click_is"]

            wave = data["wave"]
            best_wave = data["best_wave"]
            enemies_had = data["enemies_had"]

            button_1_limit_had = data["button_1_limit_had"]
            button_2_limit_had = data["button_2_limit_had"]
            button_3_limit_had = data["button_3_limit_had"]
            button_4_limit_had = data["button_4_limit_had"]
            button_5_limit_had = data["button_5_limit_had"]
            button_6_limit_had = data["button_6_limit_had"]
            button_7_limit_had = data["button_7_limit_had"]
            button_8_limit_had = data["button_8_limit_had"]
            button_9_limit_had = data["button_9_limit_had"]
            button_10_limit_had = data["button_10_limit_had"]

            button_upgrade_1_limit_had = data["button_upgrade_1_limit_had"]
            button_upgrade_2_limit_had = data["button_upgrade_2_limit_had"]
            button_upgrade_3_limit_had = data["button_upgrade_3_limit_had"]
            button_upgrade_4_limit_had = data["button_upgrade_4_limit_had"]
            button_upgrade_5_limit_had = data["button_upgrade_5_limit_had"]

            button_prestige_upgrade_1_limit_had = data["button_prestige_upgrade_1_limit_had"]
            button_prestige_upgrade_2_limit_had = data["button_prestige_upgrade_2_limit_had"]
            button_prestige_upgrade_3_limit_had = data["button_prestige_upgrade_3_limit_had"]
            button_prestige_upgrade_4_limit_had = data["button_prestige_upgrade_4_limit_had"]

            skill_points = data["skill_points"]
            enemies_needed_skill_tree_had = data["enemies_needed_skill_tree_had"]

            skill_tree_dpc_multi = data["skill_tree_dpc_multi"]
            skill_tree_dps_multi = data["skill_tree_dps_multi"]
            skill_tree_money_multi = data["skill_tree_money_multi"]
            skill_tree_discount = data["skill_tree_discount"]
            skill_tree_wave_multi = data["skill_tree_wave_multi"]
            skill_tree_dps_multi = data["skill_tree_dps_multi"]

            skill_tree_overdrive_dmg_multi = data["skill_tree_overdrive_dmg_multi"]
            skill_tree_overdrive_speed_multi = data["skill_tree_overdrive_speed_multi"]

            skill_tree_unlock_limit_had = data["skill_tree_unlock_limit_had"]

            skill_tree_dmg_path_1_limit_had = data["skill_tree_dmg_path_1_limit_had"]
            skill_tree_dmg_path_2_limit_had = data["skill_tree_dmg_path_2_limit_had"]
            skill_tree_dmg_path_3_limit_had = data["skill_tree_dmg_path_3_limit_had"]
            skill_tree_dmg_path_4_limit_had = data["skill_tree_dmg_path_4_limit_had"]
            skill_tree_dmg_path_5_limit_had = data["skill_tree_dmg_path_5_limit_had"]

            skill_tree_eco_path_1_limit_had = data["skill_tree_eco_path_1_limit_had"]
            skill_tree_eco_path_2_limit_had = data["skill_tree_eco_path_2_limit_had"]
            skill_tree_eco_path_3_limit_had = data["skill_tree_eco_path_3_limit_had"]
            skill_tree_eco_path_4_limit_had = data["skill_tree_eco_path_4_limit_had"]
            skill_tree_eco_path_5_limit_had = data["skill_tree_eco_path_5_limit_had"]

            skill_tree_prog_path_1_limit_had = data["skill_tree_prog_path_1_limit_had"]
            skill_tree_prog_path_2_limit_had = data["skill_tree_prog_path_2_limit_had"]
            skill_tree_prog_path_3_limit_had = data["skill_tree_prog_path_3_limit_had"]
            skill_tree_prog_path_4_limit_had = data["skill_tree_prog_path_4_limit_had"]
            skill_tree_prog_path_5_limit_had = data["skill_tree_prog_path_5_limit_had"]

            combo = data["combo"]
            last_click_time = data["last_click_time"]
            click_combo_multi = data["click_combo_multi"]
            combo_add = data["combo_add"]
            overdrive_active = data["overdrive_active"]
            overdrive_type = data["overdrive_type"]

            skill_tree_unlock_color = data["skill_tree_unlock_color"]

            skill_tree_eco_path_1_color = data["skill_tree_eco_path_1_color"]
            skill_tree_eco_path_2_color = data["skill_tree_eco_path_2_color"]
            skill_tree_eco_path_3_color = data["skill_tree_eco_path_3_color"]
            skill_tree_eco_path_4_color = data["skill_tree_eco_path_4_color"]
            skill_tree_eco_path_5_color = data["skill_tree_eco_path_5_color"]

            skill_tree_dmg_path_1_color = data["skill_tree_dmg_path_1_color"]
            skill_tree_dmg_path_2_color = data["skill_tree_dmg_path_2_color"]
            skill_tree_dmg_path_3_color = data["skill_tree_dmg_path_3_color"]
            skill_tree_dmg_path_4_color = data["skill_tree_dmg_path_4_color"]
            skill_tree_dmg_path_5_color = data["skill_tree_dmg_path_5_color"]

            skill_tree_prog_path_1_color = data["skill_tree_prog_path_1_color"]
            skill_tree_prog_path_2_color = data["skill_tree_prog_path_2_color"]
            skill_tree_prog_path_3_color = data["skill_tree_prog_path_3_color"]
            skill_tree_prog_path_4_color = data["skill_tree_prog_path_4_color"]
            skill_tree_prog_path_5_color = data["skill_tree_prog_path_5_color"]

            current_index = data["current_index"]


pygame.init()

# main stuff
screen = pygame.display.set_mode((1200, 900))
running = True
clock = pygame.time.Clock()
pygame.display.set_caption("clicker-heroes")
width = screen.get_width()
height = screen.get_height()

# centers
clicker_center = (int(width / 1.597) + 20, int(height / 2.5))

button_1_center = (int(width / 9.3), int(height / 5.8))
button_2_center = (int(width / 9.3), int(button_1_center[1] + 120))
button_3_center = (int(width / 9.3), int(button_2_center[1] + 120))
button_4_center = (int(width / 9.3), int(button_3_center[1] + 120))
button_5_center = (int(width / 9.3), int(button_4_center[1] + 120))
button_6_center = (int(width / 3.6), int(height / 5.8))
button_7_center = (int(width / 3.6), int(button_6_center[1] + 120))
button_8_center = (int(width / 3.6), int(button_7_center[1] + 120))
button_9_center = (int(width / 3.6), int(button_8_center[1] + 120))
button_10_center = (int(width / 3.6), int(button_9_center[1] + 120))

button_upgrade_1_center = (int(width / 4), int(height / 5.8))
button_upgrade_2_center = (int(width / 4), int(button_upgrade_1_center[1]) + 120)
button_upgrade_3_center = (int(width / 4), int(button_upgrade_2_center[1]) + 120)
button_upgrade_4_center = (int(width / 4), int(button_upgrade_3_center[1]) + 120)
button_upgrade_5_center = (int(width / 4), int(button_upgrade_4_center[1]) + 120)

button_next_center = (int(width / 1.5), int(height / 6))
button_back_center = (int(width / 1.7), int(height / 6))

button_auto_next_center = (int(width / 1.15), int(height / 6))
button_auto_click_center = (int(width / 1.15), int(height / 3.5))

button_gui_1_center = (int(width / 10), int(height / 1.09))
button_gui_2_center = (int(width / 10) + 250, int(height / 1.09))
button_gui_3_center = (int(width / 10) + 500, int(height / 1.09))
button_gui_4_center = (int(width / 10) + 750, int(height / 1.09))
button_gui_5_center = (int(width / 10) + 1000, int(height / 1.09))

button_prestige_center = int(width / 6) , int(height / 2.8)
button_prestige_upgrade_1_center = int(width / 4) , int(height / 2.2)
button_prestige_upgrade_2_center = int(width / 4) , int(height / 2.2) + 80
button_prestige_upgrade_3_center = int(width / 4) , int(height / 2.2) + 160
button_prestige_upgrade_4_center = int(width / 4) , int(height / 2.2) + 240

button_save_center = int(width / 1.15), int(height / 20)

skill_tree_unlock_center = int(width / 6) , int(height / 3)

skill_tree_dmg_path_1_center = skill_tree_unlock_center[0], skill_tree_unlock_center[1] + 100
skill_tree_dmg_path_2_center = skill_tree_unlock_center[0], skill_tree_unlock_center[1] + 170
skill_tree_dmg_path_3_center = skill_tree_unlock_center[0], skill_tree_unlock_center[1] + 240
skill_tree_dmg_path_4_center = skill_tree_unlock_center[0], skill_tree_unlock_center[1] + 310
skill_tree_dmg_path_5_center = skill_tree_unlock_center[0], skill_tree_unlock_center[1] + 380

skill_tree_eco_path_1_center = skill_tree_unlock_center[0] + 100, skill_tree_unlock_center[1] + 100
skill_tree_eco_path_2_center = skill_tree_unlock_center[0] + 100, skill_tree_unlock_center[1] + 170
skill_tree_eco_path_3_center = skill_tree_unlock_center[0] + 100, skill_tree_unlock_center[1] + 240
skill_tree_eco_path_4_center = skill_tree_unlock_center[0] + 100, skill_tree_unlock_center[1] + 310
skill_tree_eco_path_5_center = skill_tree_unlock_center[0] + 100, skill_tree_unlock_center[1] + 380

skill_tree_prog_path_1_center = skill_tree_unlock_center[0] - 100, skill_tree_unlock_center[1] + 100
skill_tree_prog_path_2_center = skill_tree_unlock_center[0] - 100, skill_tree_unlock_center[1] + 170
skill_tree_prog_path_3_center = skill_tree_unlock_center[0] - 100, skill_tree_unlock_center[1] + 240
skill_tree_prog_path_4_center = skill_tree_unlock_center[0] - 100, skill_tree_unlock_center[1] + 310
skill_tree_prog_path_5_center = skill_tree_unlock_center[0] - 100, skill_tree_unlock_center[1] + 380

# gui
gui = 1

# base sizes
clicker_base = 230
button_next_size = 50
button_base1,button_base2 = 90,40
gui_buttons_size = 190,90
gui_exit = 120,90
upgrade_buttons_size = 120,80
prestige_upgrade_buttons_size = 100,60
button_save_size = 80
skill_tree_size = 70,50
skill_tree_display = 180,120

# scales
clicker_scale = 1

button_scale_1 = 1
button_scale_2 = 1
button_scale_3 = 1
button_scale_4 = 1
button_scale_5 = 1
button_scale_6 = 1
button_scale_7 = 1
button_scale_8 = 1
button_scale_9 = 1
button_scale_10 = 1

button_scale_upgrade_1 = 1
button_scale_upgrade_2 = 1
button_scale_upgrade_3 = 1
button_scale_upgrade_4 = 1
button_scale_upgrade_5 = 1

button_scale_next = 1
button_scale_back = 1

button_scale_auto_next = 1
button_scale_auto_click = 1

button_scale_gui_1 = 1
button_scale_gui_2 = 1
button_scale_gui_3 = 1
button_scale_gui_4 = 1
button_scale_gui_5 = 1

button_scale_prestige = 1
button_scale_prestige_upgrade_1 = 1
button_scale_prestige_upgrade_2 = 1
button_scale_prestige_upgrade_3 = 1
button_scale_prestige_upgrade_4 = 1

skill_tree_unlock_scale = 1

skill_tree_dmg_path_1_scale = 1
skill_tree_dmg_path_2_scale = 1
skill_tree_dmg_path_3_scale = 1
skill_tree_dmg_path_4_scale = 1
skill_tree_dmg_path_5_scale = 1

skill_tree_eco_path_1_scale = 1
skill_tree_eco_path_2_scale = 1
skill_tree_eco_path_3_scale = 1
skill_tree_eco_path_4_scale = 1
skill_tree_eco_path_5_scale = 1

skill_tree_prog_path_1_scale = 1
skill_tree_prog_path_2_scale = 1
skill_tree_prog_path_3_scale = 1
skill_tree_prog_path_4_scale = 1
skill_tree_prog_path_5_scale = 1

button_scale_save = 1

# button
button_increase_price = 1.1

button_1_cost = 10
button_2_cost = 10
button_3_cost = 50
button_4_cost = 200
button_5_cost = 1000
button_6_cost = 5000
button_7_cost = 10000
button_8_cost = 50000
button_9_cost = 100000
button_10_cost = 500000

button_upgrade_1_cost = 10000
button_upgrade_2_cost = 10000
button_upgrade_3_cost = 100000
button_upgrade_4_cost = 10000000
button_upgrade_5_cost = 1000000000

button_prestige_upgrade_1_cost = 100
button_prestige_upgrade_2_cost = 1000
button_prestige_upgrade_3_cost = 10000
button_prestige_upgrade_4_cost = 1000000

skill_tree_unlock_cost = 1

skill_tree_dmg_path_1_cost = 3
skill_tree_dmg_path_2_cost = 5
skill_tree_dmg_path_3_cost = 10
skill_tree_dmg_path_4_cost = 15
skill_tree_dmg_path_5_cost = 30

skill_tree_eco_path_1_cost = 3
skill_tree_eco_path_2_cost = 5
skill_tree_eco_path_3_cost = 10
skill_tree_eco_path_4_cost = 15
skill_tree_eco_path_5_cost = 30

skill_tree_prog_path_1_cost = 3
skill_tree_prog_path_2_cost = 5
skill_tree_prog_path_3_cost = 10
skill_tree_prog_path_4_cost = 15
skill_tree_prog_path_5_cost = 30

# enemy health
max_health = 10
health = max_health

# damage
click_damage = 1
click_damage_multi = 1
damage_per_second = 0
damage_per_second_multi = 1

# gold
base_gain = 5
gold = 0
money_multiplier = 1
discount = 1

# prestige
prestige_tokens = 0
prestige_tokens_gain = 0
prestige_tokens_multiplier = 1
prestige_dmg_multi = 1
prestige_upgrade_dmg_multi = 1
prestige_upgrade_money_multi = 1
prestige_enemy_red = 0

# Skill Tree
skill_points = 0
enemies_needed_skill_tree = 100
enemies_needed_skill_tree_had = 0

skill_tree_dpc_multi = 1
skill_tree_dps_multi = 1
skill_tree_money_multi = 1
skill_tree_discount = 0
skill_tree_wave_multi = 1
skill_tree_overdrive_dmg_multi = 1
skill_tree_overdrive_speed_multi = 1

# time
time_passed = 0
time_passed_2 = 0
time_passed_3 = 0
time_passed_4 = 0

save_time = 0
save_time_2 = 0

next_clicker_is = False
auto_next_is = False
auto_click_is = False

base_auto_click_time = 0.2

# wave
wave = 1
best_wave = wave
wave_health_multi = 1.2
enemies_had = 0
enemies_need = 10

# limits
button_1_limit_had = 0
button_2_limit_had = 0
button_3_limit_had = 0
button_4_limit_had = 0
button_5_limit_had = 0
button_6_limit_had = 0
button_7_limit_had = 0
button_8_limit_had = 0
button_9_limit_had = 0
button_10_limit_had = 0

button_1_limit = 10
button_2_limit = 10
button_3_limit = 25
button_4_limit = 25
button_5_limit = 50
button_6_limit = 50
button_7_limit = 50
button_8_limit = 75
button_9_limit = 75
button_10_limit = 100

button_upgrade_1_limit_had = 0
button_upgrade_2_limit_had = 0
button_upgrade_3_limit_had = 0
button_upgrade_4_limit_had = 0
button_upgrade_5_limit_had = 0

button_upgrade_1_limit = 5
button_upgrade_2_limit = 5
button_upgrade_3_limit = 5
button_upgrade_4_limit = 5
button_upgrade_5_limit = 5

button_prestige_upgrade_1_limit_had = 0
button_prestige_upgrade_2_limit_had = 0
button_prestige_upgrade_3_limit_had = 0
button_prestige_upgrade_4_limit_had = 0

button_prestige_upgrade_1_limit = 25
button_prestige_upgrade_2_limit = 10
button_prestige_upgrade_3_limit = 5
button_prestige_upgrade_4_limit = 4

skill_tree_unlock_limit = 1
skill_tree_unlock_limit_had = 0

skill_tree_dmg_path_1_limit = 1
skill_tree_dmg_path_2_limit = 1
skill_tree_dmg_path_3_limit = 1
skill_tree_dmg_path_4_limit = 1
skill_tree_dmg_path_5_limit = 1

skill_tree_dmg_path_1_limit_had = 0
skill_tree_dmg_path_2_limit_had = 0
skill_tree_dmg_path_3_limit_had = 0
skill_tree_dmg_path_4_limit_had = 0
skill_tree_dmg_path_5_limit_had = 0

skill_tree_eco_path_1_limit = 1
skill_tree_eco_path_2_limit = 1
skill_tree_eco_path_3_limit = 1
skill_tree_eco_path_4_limit = 1
skill_tree_eco_path_5_limit = 1

skill_tree_eco_path_1_limit_had = 0
skill_tree_eco_path_2_limit_had = 0
skill_tree_eco_path_3_limit_had = 0
skill_tree_eco_path_4_limit_had = 0
skill_tree_eco_path_5_limit_had = 0

skill_tree_prog_path_1_limit = 1
skill_tree_prog_path_2_limit = 1
skill_tree_prog_path_3_limit = 1
skill_tree_prog_path_4_limit = 1
skill_tree_prog_path_5_limit = 1

skill_tree_prog_path_1_limit_had = 0
skill_tree_prog_path_2_limit_had = 0
skill_tree_prog_path_3_limit_had = 0
skill_tree_prog_path_4_limit_had = 0
skill_tree_prog_path_5_limit_had = 0

# text
font_font_smaller = pygame.font.SysFont("Arial", 15)
font_font = pygame.font.SysFont("Arial", 22)
font_font_medium = pygame.font.SysFont("Arial", 26)
font_font_bigger = pygame.font.SysFont("Arial", 30)
font_font_biggest = pygame.font.SysFont("Arial", 40)
font_emoji_small = pygame.font.SysFont("Segoe UI Emoji", 30)
font_emoji_medium = pygame.font.SysFont("Segoe UI Emoji", 54)
font_emoji = pygame.font.SysFont("Segoe UI Emoji", 70)
font_emoji_bigger = pygame.font.SysFont("Segoe UI Emoji", 88)

# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0,0,0)
white = (255, 255, 255)
brown = (150, 75, 0)
light_Brown = (196, 164, 132)

# damage pop-up
damage_popup = []

# crit multi
crit_multi = 1
crit_multi_auto = 1

# click combo
combo = 1
last_click_time = 0
combo_timeout = 5
click_combo_multi = 1
combo_multi = 1
combo_add = 0

# 30 s events
OVERDRIVE_INTERVAL = 30000
OVERDRIVE_DURATION = 10000

last_overdrive_time = pygame.time.get_ticks()
overdrive_active = False
overdrive_type = None
overdrive_start_time = 0

# bought skill tree upgr
skill_tree_unlock_color = red

skill_tree_eco_path_1_color = red
skill_tree_eco_path_2_color = red
skill_tree_eco_path_3_color = red
skill_tree_eco_path_4_color = red
skill_tree_eco_path_5_color = red

skill_tree_dmg_path_1_color = red
skill_tree_dmg_path_2_color = red
skill_tree_dmg_path_3_color = red
skill_tree_dmg_path_4_color = red
skill_tree_dmg_path_5_color = red

skill_tree_prog_path_1_color = red
skill_tree_prog_path_2_color = red
skill_tree_prog_path_3_color = red
skill_tree_prog_path_4_color = red
skill_tree_prog_path_5_color = red

# images
images = [
    pygame.image.load(resource_path("dragon.png")).convert_alpha(),
    pygame.image.load(resource_path("goblin.png")).convert_alpha(),
    pygame.image.load(resource_path("mage.png")).convert_alpha(),
    pygame.image.load(resource_path("skeleton.png")).convert_alpha(),
    pygame.image.load(resource_path("slime.png")).convert_alpha()
]
current_index = 0

scale = 1
def scale_image():
    img = images[current_index]
    new_size = (
        int(330 * scale),
        int(300 * scale)
    )
    return pygame.transform.smoothscale(img, new_size)
scaled_image = scale_image()
image = scaled_image.get_rect(center=(int(width / 1.597) + 25, int(height / 2.5)))

# load save
load_game()
while running:
    delta_time = clock.tick(60) / 1000
    screen.fill((50, 150, 100))
    mouse_pos = pygame.mouse.get_pos()

    now = pygame.time.get_ticks()

    # background
    background_left = pygame.Rect(0, 80, 425, 640)
    pygame.draw.rect(screen,(40,32,230), background_left, border_top_right_radius= 10, border_bottom_right_radius=10)

    background_bottom = pygame.Rect(0, 750, 1200, 640)
    pygame.draw.rect(screen,light_Brown, background_bottom, border_radius=15)

    # scaling clicker
    clicker_size = clicker_base * clicker_scale
    clicker = pygame.Rect(0, 0, clicker_size, clicker_size)
    clicker.center = clicker_center

    # scaling button 1
    size_1_button = button_base1 * button_scale_1, button_base2 * button_scale_1
    button_1 = pygame.Rect(0, 0, size_1_button[0], size_1_button[1])
    button_1.center = button_1_center

    # scaling button 2
    size_2_button = button_base1 * button_scale_2,button_base2 * button_scale_2
    button_2 = pygame.Rect(0, 0, size_2_button[0], size_2_button[1])
    button_2.center = button_2_center

    # scaling button 3
    size_3_button = button_base1 * button_scale_3,button_base2 * button_scale_3
    button_3 = pygame.Rect(0, 0, size_3_button[0], size_3_button[1])
    button_3.center = button_3_center

    # scaling button 4
    size_4_button = button_base1 * button_scale_4,button_base2 * button_scale_4
    button_4 = pygame.Rect(0, 0, size_4_button[0], size_4_button[1])
    button_4.center = button_4_center

    # scaling button 5
    size_5_button = button_base1 * button_scale_5,button_base2 * button_scale_5
    button_5 = pygame.Rect(0, 0, size_5_button[0], size_5_button[1])
    button_5.center = button_5_center

    # scaling button 6
    size_6_button = button_base1 * button_scale_6, button_base2 * button_scale_6
    button_6 = pygame.Rect(0, 0, size_6_button[0], size_6_button[1])
    button_6.center = button_6_center

    # scaling button 7
    size_7_button = button_base1 * button_scale_7, button_base2 * button_scale_7
    button_7 = pygame.Rect(0, 0, size_7_button[0], size_7_button[1])
    button_7.center = button_7_center

    # scaling button 8
    size_8_button = button_base1 * button_scale_8, button_base2 * button_scale_8
    button_8 = pygame.Rect(0, 0, size_8_button[0], size_8_button[1])
    button_8.center = button_8_center

    # scaling button 9
    size_9_button = button_base1 * button_scale_9, button_base2 * button_scale_9
    button_9 = pygame.Rect(0, 0, size_9_button[0], size_9_button[1])
    button_9.center = button_9_center

    # scaling button 10
    size_10_button = button_base1 * button_scale_10, button_base2 * button_scale_10
    button_10 = pygame.Rect(0, 0, size_10_button[0], size_10_button[1])
    button_10.center = button_10_center

    # scaling upgrade button 1
    size_1_button_upgrade = upgrade_buttons_size[0] * button_scale_upgrade_1, upgrade_buttons_size[1] * button_scale_upgrade_1
    button_upgrade_1 = pygame.Rect(0, 0, size_1_button_upgrade[0], size_1_button_upgrade[1])
    button_upgrade_1.center = button_upgrade_1_center

    # scaling upgrade button 2
    size_2_button_upgrade = upgrade_buttons_size[0] * button_scale_upgrade_2, upgrade_buttons_size[1] * button_scale_upgrade_2
    button_upgrade_2 = pygame.Rect(0, 0, size_2_button_upgrade[0], size_2_button_upgrade[1])
    button_upgrade_2.center = button_upgrade_2_center

    # scaling upgrade button 3
    size_3_button_upgrade = upgrade_buttons_size[0] * button_scale_upgrade_3, upgrade_buttons_size[1] * button_scale_upgrade_3
    button_upgrade_3 = pygame.Rect(0, 0, size_3_button_upgrade[0], size_3_button_upgrade[1])
    button_upgrade_3.center = button_upgrade_3_center

    # scaling upgrade button 4
    size_4_button_upgrade = upgrade_buttons_size[0] * button_scale_upgrade_4, upgrade_buttons_size[1] * button_scale_upgrade_4
    button_upgrade_4 = pygame.Rect(0, 0, size_4_button_upgrade[0], size_4_button_upgrade[1])
    button_upgrade_4.center = button_upgrade_4_center

    # scaling upgrade button 5
    size_5_button_upgrade = upgrade_buttons_size[0] * button_scale_upgrade_5, upgrade_buttons_size[1] * button_scale_upgrade_5
    button_upgrade_5 = pygame.Rect(0, 0, size_5_button_upgrade[0], size_5_button_upgrade[1])
    button_upgrade_5.center = button_upgrade_5_center

    # scaling prestige upgrade button 1
    size_1_button_prestige_upgrade = prestige_upgrade_buttons_size[0] * button_scale_prestige_upgrade_1, prestige_upgrade_buttons_size[1] * button_scale_prestige_upgrade_1
    button_prestige_upgrade_1 = pygame.Rect(0, 0, size_1_button_prestige_upgrade[0], size_1_button_prestige_upgrade[1])
    button_prestige_upgrade_1.center = button_prestige_upgrade_1_center

    # scaling prestige upgrade button 2
    size_2_button_prestige_upgrade = prestige_upgrade_buttons_size[0] * button_scale_prestige_upgrade_2, prestige_upgrade_buttons_size[1] * button_scale_prestige_upgrade_2
    button_prestige_upgrade_2 = pygame.Rect(0, 0, size_2_button_prestige_upgrade[0], size_2_button_prestige_upgrade[1])
    button_prestige_upgrade_2.center = button_prestige_upgrade_2_center

    # scaling prestige upgrade button 3
    size_3_button_prestige_upgrade = prestige_upgrade_buttons_size[0] * button_scale_prestige_upgrade_3,prestige_upgrade_buttons_size[1] * button_scale_prestige_upgrade_3
    button_prestige_upgrade_3 = pygame.Rect(0, 0, size_3_button_prestige_upgrade[0], size_3_button_prestige_upgrade[1])
    button_prestige_upgrade_3.center = button_prestige_upgrade_3_center

    # scaling prestige upgrade button 4
    size_4_button_prestige_upgrade = prestige_upgrade_buttons_size[0] * button_scale_prestige_upgrade_4,prestige_upgrade_buttons_size[1] * button_scale_prestige_upgrade_4
    button_prestige_upgrade_4 = pygame.Rect(0, 0, size_4_button_prestige_upgrade[0], size_4_button_prestige_upgrade[1])
    button_prestige_upgrade_4.center = button_prestige_upgrade_4_center

    # scaling skill tree unlock
    size_unlock_skill_tree = skill_tree_size[0] * skill_tree_unlock_scale, skill_tree_size[1] * skill_tree_unlock_scale
    skill_tree_unlock = pygame.Rect(0, 0, size_unlock_skill_tree[0], size_unlock_skill_tree[1])
    skill_tree_unlock.center = skill_tree_unlock_center

    # scaling skill tree dmg path 1
    size_dmg_path_1_skill_tree = skill_tree_size[0] * skill_tree_dmg_path_1_scale, skill_tree_size[1] * skill_tree_dmg_path_1_scale
    skill_tree_dmg_path_1 = pygame.Rect(0, 0, size_dmg_path_1_skill_tree[0], size_dmg_path_1_skill_tree[1])
    skill_tree_dmg_path_1.center = skill_tree_dmg_path_1_center

    # scaling skill tree dmg path 2
    size_dmg_path_2_skill_tree = skill_tree_size[0] * skill_tree_dmg_path_2_scale, skill_tree_size[1] * skill_tree_dmg_path_2_scale
    skill_tree_dmg_path_2 = pygame.Rect(0, 0, size_dmg_path_2_skill_tree[0], size_dmg_path_2_skill_tree[1])
    skill_tree_dmg_path_2.center = skill_tree_dmg_path_2_center

    # scaling skill tree dmg path 3
    size_dmg_path_3_skill_tree = skill_tree_size[0] * skill_tree_dmg_path_3_scale, skill_tree_size[1] * skill_tree_dmg_path_3_scale
    skill_tree_dmg_path_3 = pygame.Rect(0, 0, size_dmg_path_3_skill_tree[0], size_dmg_path_3_skill_tree[1])
    skill_tree_dmg_path_3.center = skill_tree_dmg_path_3_center

    # scaling skill tree dmg path 4
    size_dmg_path_4_skill_tree = skill_tree_size[0] * skill_tree_dmg_path_4_scale, skill_tree_size[1] * skill_tree_dmg_path_4_scale
    skill_tree_dmg_path_4 = pygame.Rect(0, 0, size_dmg_path_4_skill_tree[0], size_dmg_path_4_skill_tree[1])
    skill_tree_dmg_path_4.center = skill_tree_dmg_path_4_center

    # scaling skill tree dmg path 5
    size_dmg_path_5_skill_tree = skill_tree_size[0] * skill_tree_dmg_path_5_scale, skill_tree_size[1] * skill_tree_dmg_path_5_scale
    skill_tree_dmg_path_5 = pygame.Rect(0, 0, size_dmg_path_5_skill_tree[0], size_dmg_path_5_skill_tree[1])
    skill_tree_dmg_path_5.center = skill_tree_dmg_path_5_center

    # scaling skill tree eco path 1
    size_eco_path_1_skill_tree = skill_tree_size[0] * skill_tree_eco_path_1_scale, skill_tree_size[1] * skill_tree_eco_path_1_scale
    skill_tree_eco_path_1 = pygame.Rect(0, 0, size_eco_path_1_skill_tree[0], size_eco_path_1_skill_tree[1])
    skill_tree_eco_path_1.center = skill_tree_eco_path_1_center

    # scaling skill tree eco path 2
    size_eco_path_2_skill_tree = skill_tree_size[0] * skill_tree_eco_path_2_scale, skill_tree_size[1] * skill_tree_eco_path_2_scale
    skill_tree_eco_path_2 = pygame.Rect(0, 0, size_eco_path_2_skill_tree[0], size_eco_path_2_skill_tree[1])
    skill_tree_eco_path_2.center = skill_tree_eco_path_2_center

    # scaling skill tree eco path 3
    size_eco_path_3_skill_tree = skill_tree_size[0] * skill_tree_eco_path_3_scale, skill_tree_size[1] * skill_tree_eco_path_3_scale
    skill_tree_eco_path_3 = pygame.Rect(0, 0, size_eco_path_3_skill_tree[0], size_eco_path_3_skill_tree[1])
    skill_tree_eco_path_3.center = skill_tree_eco_path_3_center

    # scaling skill tree eco path 4
    size_eco_path_4_skill_tree = skill_tree_size[0] * skill_tree_eco_path_4_scale, skill_tree_size[1] * skill_tree_eco_path_4_scale
    skill_tree_eco_path_4 = pygame.Rect(0, 0, size_eco_path_4_skill_tree[0], size_eco_path_4_skill_tree[1])
    skill_tree_eco_path_4.center = skill_tree_eco_path_4_center

    # scaling skill tree eco path 5
    size_eco_path_5_skill_tree = skill_tree_size[0] * skill_tree_eco_path_5_scale, skill_tree_size[1] * skill_tree_eco_path_5_scale
    skill_tree_eco_path_5 = pygame.Rect(0, 0, size_eco_path_5_skill_tree[0], size_eco_path_5_skill_tree[1])
    skill_tree_eco_path_5.center = skill_tree_eco_path_5_center

    # scaling skill tree prog path 1
    size_prog_path_1_skill_tree = skill_tree_size[0] * skill_tree_prog_path_1_scale, skill_tree_size[1] * skill_tree_prog_path_1_scale
    skill_tree_prog_path_1 = pygame.Rect(0, 0, size_prog_path_1_skill_tree[0], size_prog_path_1_skill_tree[1])
    skill_tree_prog_path_1.center = skill_tree_prog_path_1_center

    # scaling skill tree prog path 2
    size_prog_path_2_skill_tree = skill_tree_size[0] * skill_tree_prog_path_2_scale, skill_tree_size[1] * skill_tree_prog_path_2_scale
    skill_tree_prog_path_2 = pygame.Rect(0, 0, size_prog_path_2_skill_tree[0], size_prog_path_2_skill_tree[1])
    skill_tree_prog_path_2.center = skill_tree_prog_path_2_center

    # scaling skill tree prog path 3
    size_prog_path_3_skill_tree = skill_tree_size[0] * skill_tree_prog_path_3_scale, skill_tree_size[1] * skill_tree_prog_path_3_scale
    skill_tree_prog_path_3 = pygame.Rect(0, 0, size_prog_path_3_skill_tree[0], size_prog_path_3_skill_tree[1])
    skill_tree_prog_path_3.center = skill_tree_prog_path_3_center

    # scaling skill tree prog path 4
    size_prog_path_4_skill_tree = skill_tree_size[0] * skill_tree_prog_path_4_scale, skill_tree_size[1] * skill_tree_prog_path_4_scale
    skill_tree_prog_path_4 = pygame.Rect(0, 0, size_prog_path_4_skill_tree[0], size_prog_path_4_skill_tree[1])
    skill_tree_prog_path_4.center = skill_tree_prog_path_4_center

    # scaling skill tree prog path 5
    size_prog_path_5_skill_tree = skill_tree_size[0] * skill_tree_prog_path_5_scale, skill_tree_size[1] * skill_tree_prog_path_5_scale
    skill_tree_prog_path_5 = pygame.Rect(0, 0, size_prog_path_5_skill_tree[0], size_prog_path_5_skill_tree[1])
    skill_tree_prog_path_5.center = skill_tree_prog_path_5_center

    # scaling next button
    size_next_button = button_next_size * button_scale_next
    button_next = pygame.Rect(0, 0, size_next_button, size_next_button)
    button_next.center = button_next_center

    # scaling back button
    size_back_button = button_next_size * button_scale_back
    button_back = pygame.Rect(0, 0, size_back_button, size_back_button)
    button_back.center = button_back_center

    # scaling auto next button
    size_auto_next = button_base1 * button_scale_auto_next, button_base2 * button_scale_auto_next
    button_auto_next = pygame.Rect(0, 0, size_auto_next[0], size_auto_next[1])
    button_auto_next.center = button_auto_next_center

    # scaling auto click button
    size_auto_click = button_base1 * button_scale_auto_click, button_base2 * button_scale_auto_click
    button_auto_click = pygame.Rect(0, 0, size_auto_click[0], size_auto_click[1])
    button_auto_click.center = button_auto_click_center

    # scaling button gui 1
    size_button_gui_1 = gui_buttons_size[0] * button_scale_gui_1, gui_buttons_size[1] * button_scale_gui_1
    button_gui_1 = pygame.Rect(0, 0, size_button_gui_1[0], size_button_gui_1[1])
    button_gui_1.center = button_gui_1_center

    # scaling button gui 2
    size_button_gui_2 = gui_buttons_size[0] * button_scale_gui_2, gui_buttons_size[1] * button_scale_gui_2
    button_gui_2 = pygame.Rect(0, 0, size_button_gui_2[0], size_button_gui_2[1])
    button_gui_2.center = button_gui_2_center

    # scaling button gui 3
    size_button_gui_3 = gui_buttons_size[0] * button_scale_gui_3, gui_buttons_size[1] * button_scale_gui_3
    button_gui_3 = pygame.Rect(0, 0, size_button_gui_3[0], size_button_gui_3[1])
    button_gui_3.center = button_gui_3_center

    # scaling button gui 4
    size_button_gui_4 = gui_buttons_size[0] * button_scale_gui_4, gui_buttons_size[1] * button_scale_gui_4
    button_gui_4 = pygame.Rect(0, 0, size_button_gui_4[0], size_button_gui_4[1])
    button_gui_4.center = button_gui_4_center

    # scaling button gui 5
    size_button_gui_5 = gui_exit[0] * button_scale_gui_5, gui_exit[1] * button_scale_gui_5
    button_gui_5 = pygame.Rect(0, 0, size_button_gui_5[0], size_button_gui_5[1])
    button_gui_5.center = button_gui_5_center

    # scaling button prestige
    size_button_prestige = gui_buttons_size[0] * button_scale_prestige, gui_buttons_size[1] * button_scale_prestige
    button_prestige = pygame.Rect(0, 0, size_button_prestige[0], size_button_prestige[1])
    button_prestige.center = button_prestige_center

    # scaling save button
    size_button_save = button_save_size * button_scale_save
    button_save = pygame.Rect(0, 0, size_button_save, size_button_save)
    button_save.center = button_save_center

    # scalling img
    scaled_image = scale_image()
    image = scaled_image.get_rect(center=image.center)

    # Damage Overall
    DPC_overall = round(click_damage * click_damage_multi * prestige_dmg_multi * prestige_upgrade_dmg_multi * skill_tree_dpc_multi * round(combo_multi,2) * skill_tree_overdrive_dmg_multi,2)
    DPS_overall = round(damage_per_second * damage_per_second_multi * prestige_dmg_multi * prestige_upgrade_dmg_multi * skill_tree_dps_multi * skill_tree_overdrive_dmg_multi,2)

    # Money Overall
    money_overall = base_gain * money_multiplier * prestige_upgrade_money_multi * skill_tree_money_multi * skill_tree_wave_multi

    # time
    current_time = time.time()

    # main event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # clicker
                if clicker.collidepoint(event.pos):
                    if health > 0:
                        if random.randint(1,10) == 1 and skill_tree_dmg_path_3_limit_had == 1:
                            crit_multi = 2
                        if skill_tree_dmg_path_5_limit_had >= skill_tree_dmg_path_5_limit:
                            if health <= max_health * 0.3:
                                health -= DPC_overall * 1.5 * crit_multi
                            else:
                                health -= DPC_overall * crit_multi
                        else:
                            health -= DPC_overall * crit_multi
                        x,y = event.pos
                        damage_popup.append([x,y,notation(DPC_overall * crit_multi),1.0])
                        crit_multi = 1
                        save_time_2 = time_passed_4
                        if skill_tree_dmg_path_4_limit_had == 1:
                            if current_time - last_click_time <= combo_timeout:
                                combo += 1
                                combo_multi += 0.001
                            else:
                                combo = 1
                            last_click_time = current_time
                        if skill_tree_eco_path_4_limit_had >= skill_tree_eco_path_4_limit:
                            gold += money_overall / 100
                    scale = 0.9
                    scaled_image = scale_image()
                    clicker_scale = 0.9
                    image = scaled_image.get_rect(center=image.center)

                # button 1
                if button_1.collidepoint(event.pos) and gui == 1:
                    if button_1_limit_had + 1 <= button_1_limit:
                        if gold >= button_1_cost / discount:
                            gold -= button_1_cost / discount
                            button_1_cost = int(button_1_cost * button_increase_price)
                            click_damage += 1
                            button_1_limit_had += 1
                        button_scale_1 = 0.9
                    else:
                        button_scale_1 = 0.9

                # button 2
                if button_2.collidepoint(event.pos) and gui == 1:
                    if button_2_limit_had + 1 <= button_2_limit:
                        if gold >= button_2_cost / discount:
                            gold -= button_2_cost / discount
                            button_2_cost = int(button_2_cost * button_increase_price)
                            damage_per_second += 2
                            button_2_limit_had += 1
                        button_scale_2 = 0.9
                    else:
                        button_scale_2 = 0.9

                # button 3
                if button_3.collidepoint(event.pos) and gui == 1:
                    if button_3_limit_had + 1 <= button_3_limit:
                        if gold >= button_3_cost / discount:
                            gold -= button_3_cost / discount
                            button_3_cost = int(button_3_cost * button_increase_price)
                            damage_per_second += 8
                            button_3_limit_had += 1
                        button_scale_3 = 0.9
                    else:
                        button_scale_3 = 0.9

                # button 4
                if button_4.collidepoint(event.pos) and gui == 1:
                    if button_4_limit_had + 1 <= button_4_limit:
                        if gold >= button_4_cost / discount:
                            gold -= button_4_cost / discount
                            button_4_cost = int(button_4_cost * button_increase_price)
                            click_damage += 20
                            button_4_limit_had += 1
                        button_scale_4 = 0.9
                    else:
                        button_scale_4 = 0.9

                # button 5
                if button_5.collidepoint(event.pos) and gui == 1:
                    if button_5_limit_had + 1 <= button_5_limit:
                        if gold >= button_5_cost / discount:
                            gold -= button_5_cost / discount
                            button_5_cost = int(button_5_cost * button_increase_price)
                            damage_per_second += 100
                            button_5_limit_had += 1
                        button_scale_5 = 0.9
                    else:
                        button_scale_5 = 0.9

                # button 6
                if button_6.collidepoint(event.pos) and gui == 1:
                    if button_6_limit_had + 1 <= button_6_limit:
                        if gold >= button_6_cost / discount:
                            gold -= button_6_cost / discount
                            button_6_cost = int(button_6_cost * button_increase_price)
                            click_damage += 500
                            button_6_limit_had += 1
                        button_scale_6 = 0.9
                    else:
                        button_scale_6 = 0.9

                # button 7
                if button_7.collidepoint(event.pos) and gui == 1:
                    if button_7_limit_had + 1 <= button_7_limit:
                        if gold >= button_7_cost / discount:
                            gold -= button_7_cost / discount
                            button_7_cost = int(button_7_cost * button_increase_price)
                            damage_per_second += 2500
                            button_7_limit_had += 1
                        button_scale_7 = 0.9
                    else:
                        button_scale_7 = 0.9

                # button 8
                if button_8.collidepoint(event.pos) and gui == 1:
                    if button_8_limit_had + 1 <= button_8_limit:
                        if gold >= button_8_cost / discount:
                            gold -= button_8_cost / discount
                            button_8_cost = int(button_8_cost * button_increase_price)
                            damage_per_second += 10000
                            button_8_limit_had += 1
                        button_scale_8 = 0.9
                    else:
                        button_scale_8 = 0.9

                # button 9
                if button_9.collidepoint(event.pos) and gui == 1:
                    if button_9_limit_had + 1 <= button_9_limit:
                        if gold >= button_9_cost / discount:
                            gold -= button_9_cost / discount
                            button_9_cost = int(button_9_cost * button_increase_price)
                            click_damage += 40000
                            button_9_limit_had += 1
                        button_scale_9 = 0.9
                    else:
                        button_scale_9 = 0.9

                # button 10
                if button_10.collidepoint(event.pos) and gui == 1:
                    if button_10_limit_had + 1 <= button_10_limit:
                        if gold >= button_10_cost / discount:
                            gold -= button_10_cost / discount
                            button_10_cost = int(button_10_cost * button_increase_price)
                            damage_per_second += 150000
                            button_10_limit_had += 1
                        button_scale_10 = 0.9
                    else:
                        button_scale_10 = 0.9

                # button upgrade 1
                if button_upgrade_1.collidepoint(event.pos) and gui == 2:
                    if button_upgrade_1_limit_had + 1 <= button_upgrade_1_limit:
                        if gold >= button_upgrade_1_cost / discount:
                            gold -= button_upgrade_1_cost / discount
                            button_upgrade_1_cost = int(button_upgrade_1_cost * 10)
                            damage_per_second_multi = damage_per_second_multi + 0.5
                            button_upgrade_1_limit_had += 1
                        button_scale_upgrade_1= 0.9
                    else:
                        button_scale_upgrade_1= 0.9

                # button upgrade 2
                if button_upgrade_2.collidepoint(event.pos) and gui == 2:
                    if button_upgrade_2_limit_had + 1 <= button_upgrade_2_limit:
                        if gold >= button_upgrade_2_cost / discount:
                            gold -= button_upgrade_2_cost / discount
                            button_upgrade_2_cost = int(button_upgrade_2_cost * 10)
                            click_damage_multi = click_damage_multi + 0.2
                            button_upgrade_2_limit_had += 1
                        button_scale_upgrade_2 = 0.9
                    else:
                        button_scale_upgrade_2 = 0.9

                # button upgrade 3
                if button_upgrade_3.collidepoint(event.pos) and gui == 2:
                    if button_upgrade_3_limit_had + 1 <= button_upgrade_3_limit:
                        if gold >= button_upgrade_3_cost / discount:
                            gold -= button_upgrade_3_cost / discount
                            button_upgrade_3_cost = int(button_upgrade_3_cost * 10)
                            money_multiplier = money_multiplier + 0.1
                            button_upgrade_3_limit_had += 1
                        button_scale_upgrade_3 = 0.9
                    else:
                        button_scale_upgrade_3 = 0.9

                # button upgrade 4
                if button_upgrade_4.collidepoint(event.pos) and gui == 2:
                    if button_upgrade_4_limit_had + 1 <= button_upgrade_4_limit:
                        if gold >= button_upgrade_4_cost / discount:
                            gold -= button_upgrade_4_cost / discount
                            button_upgrade_4_cost = int(button_upgrade_4_cost * 5)
                            discount = discount + 0.01
                            button_upgrade_4_limit_had += 1
                        button_scale_upgrade_4 = 0.9
                    else:
                        button_scale_upgrade_4 = 0.9

                # button upgrade 5
                if button_upgrade_5.collidepoint(event.pos) and gui == 2:
                    if button_upgrade_5_limit_had + 1 <= button_upgrade_5_limit:
                        if gold >= button_upgrade_5_cost / discount:
                            gold -= button_upgrade_5_cost / discount
                            enemies_need = enemies_need - 1
                            button_upgrade_5_limit_had += 1
                            button_upgrade_5_cost = int(button_upgrade_5_cost * 4)
                        button_scale_upgrade_5 = 0.9
                    else:
                        button_scale_upgrade_5 = 0.9

                # button prestige upgrade 1
                if button_prestige_upgrade_1.collidepoint(event.pos) and gui == 3:
                    if button_prestige_upgrade_1_limit_had + 1 <= button_prestige_upgrade_1_limit:
                        if prestige_tokens >= button_prestige_upgrade_1_cost:
                            prestige_tokens -= button_prestige_upgrade_1_cost
                            prestige_upgrade_dmg_multi = prestige_upgrade_dmg_multi + 2
                            button_prestige_upgrade_1_limit_had += 1
                            button_prestige_upgrade_1_cost = int(button_prestige_upgrade_1_cost * 3)
                        button_scale_prestige_upgrade_1 = 0.9
                    else:
                        button_scale_prestige_upgrade_1 = 0.9

                # button prestige upgrade 2
                if button_prestige_upgrade_2.collidepoint(event.pos) and gui == 3:
                    if button_prestige_upgrade_2_limit_had + 1 <= button_prestige_upgrade_2_limit:
                        if prestige_tokens >= button_prestige_upgrade_2_cost:
                            prestige_tokens -= button_prestige_upgrade_2_cost
                            prestige_upgrade_money_multi = prestige_upgrade_money_multi + 0.5
                            button_prestige_upgrade_2_limit_had += 1
                            button_prestige_upgrade_2_cost = int(button_prestige_upgrade_2_cost * 5)
                        button_scale_prestige_upgrade_2 = 0.9
                    else:
                        button_scale_prestige_upgrade_2 = 0.9

                # button prestige upgrade 3
                if button_prestige_upgrade_3.collidepoint(event.pos) and gui == 3:
                    if button_prestige_upgrade_3_limit_had + 1 <= button_prestige_upgrade_3_limit:
                        if prestige_tokens >= button_prestige_upgrade_3_cost:
                            prestige_tokens -= button_prestige_upgrade_3_cost
                            prestige_tokens_multiplier = prestige_tokens_multiplier + 0.2
                            button_prestige_upgrade_3_limit_had += 1
                            button_prestige_upgrade_3_cost = int(button_prestige_upgrade_3_cost * 10)
                        button_scale_prestige_upgrade_3 = 0.9
                    else:
                        button_scale_prestige_upgrade_3 = 0.9

                # button prestige upgrade 4
                if button_prestige_upgrade_4.collidepoint(event.pos) and gui == 3:
                    if button_prestige_upgrade_4_limit_had + 1 <= button_prestige_upgrade_4_limit:
                        if prestige_tokens >= button_prestige_upgrade_4_cost:
                            prestige_tokens -= button_prestige_upgrade_4_cost
                            enemies_need = enemies_need - 1
                            prestige_enemy_red += 1
                            button_prestige_upgrade_4_limit_had += 1
                            button_prestige_upgrade_4_cost = int(button_prestige_upgrade_4_cost * 12)
                        button_scale_prestige_upgrade_4 = 0.9
                    else:
                        button_scale_prestige_upgrade_4 = 0.9

                # skill tree unlock
                if skill_tree_unlock.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had + 1 <= skill_tree_unlock_limit:
                        if skill_points >= skill_tree_unlock_cost:
                            skill_tree_unlock_limit_had += 1
                            skill_tree_unlock_scale = 0.9
                            skill_points -= skill_tree_unlock_cost
                            skill_tree_unlock_color = green
                    skill_tree_unlock_scale = 0.9

                # skill tree dmg path 1
                if skill_tree_dmg_path_1.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit:
                        if skill_tree_dmg_path_1_limit_had + 1 <= skill_tree_dmg_path_1_limit:
                            if skill_points >= skill_tree_dmg_path_1_cost:
                                skill_tree_dmg_path_1_limit_had += 1
                                skill_tree_dmg_path_1_scale = 0.9
                                skill_tree_dpc_multi += 0.1
                                skill_points -= skill_tree_dmg_path_1_cost
                                skill_tree_dmg_path_1_color = green
                    skill_tree_dmg_path_1_scale = 0.9

                # skill tree dmg path 2
                if skill_tree_dmg_path_2.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_dmg_path_1_limit_had >= skill_tree_dmg_path_1_limit:
                        if skill_tree_dmg_path_2_limit_had + 1 <= skill_tree_dmg_path_2_limit:
                            if skill_points >= skill_tree_dmg_path_2_cost:
                                skill_tree_dmg_path_2_limit_had += 1
                                skill_tree_dmg_path_2_scale = 0.9
                                skill_tree_dps_multi += 0.15
                                skill_points -= skill_tree_dmg_path_2_cost
                                skill_tree_dmg_path_2_color = green
                    skill_tree_dmg_path_2_scale = 0.9

                # skill tree dmg path 3
                if skill_tree_dmg_path_3.collidepoint(event.pos) and gui == 4:
                    if (skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_dmg_path_1_limit_had >= skill_tree_dmg_path_1_limit
                    and skill_tree_dmg_path_2_limit_had >= skill_tree_dmg_path_2_limit):
                        if skill_tree_dmg_path_3_limit_had + 1 <= skill_tree_dmg_path_3_limit:
                            if skill_points >= skill_tree_dmg_path_3_cost:
                                skill_tree_dmg_path_3_limit_had += 1
                                skill_tree_dmg_path_3_scale = 0.9
                                skill_points -= skill_tree_dmg_path_3_cost
                                skill_tree_dmg_path_3_color = green
                    skill_tree_dmg_path_3_scale = 0.9

                # skill tree dmg path 4
                if skill_tree_dmg_path_4.collidepoint(event.pos) and gui == 4:
                    if (skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_dmg_path_1_limit_had >= skill_tree_dmg_path_1_limit
                    and skill_tree_dmg_path_2_limit_had >= skill_tree_dmg_path_2_limit and skill_tree_dmg_path_3_limit_had >= skill_tree_dmg_path_3_limit):
                        if skill_tree_dmg_path_4_limit_had + 1 <= skill_tree_dmg_path_4_limit:
                            if skill_points >= skill_tree_dmg_path_4_cost:
                                skill_tree_dmg_path_4_limit_had += 1
                                skill_tree_dmg_path_4_scale = 0.9
                                skill_points -= skill_tree_dmg_path_4_cost
                                skill_tree_dmg_path_4_color = green
                    skill_tree_dmg_path_4_scale = 0.9

                # skill tree dmg path 5
                if skill_tree_dmg_path_5.collidepoint(event.pos) and gui == 4:
                    if (skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_dmg_path_1_limit_had >= skill_tree_dmg_path_1_limit
                    and skill_tree_dmg_path_2_limit_had >= skill_tree_dmg_path_2_limit and skill_tree_dmg_path_3_limit_had >= skill_tree_dmg_path_3_limit
                    and skill_tree_dmg_path_4_limit_had >= skill_tree_dmg_path_4_limit):
                        if skill_tree_dmg_path_5_limit_had + 1 <= skill_tree_dmg_path_5_limit:
                            if skill_points >= skill_tree_dmg_path_5_cost:
                                skill_tree_dmg_path_5_limit_had += 1
                                skill_tree_dmg_path_5_scale = 0.9
                                skill_points -= skill_tree_dmg_path_5_cost
                                skill_tree_dmg_path_5_color = green
                    skill_tree_dmg_path_5_scale = 0.9

                # skill tree eco path 1
                if skill_tree_eco_path_1.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit:
                        if skill_tree_eco_path_1_limit_had + 1 <= skill_tree_eco_path_1_limit:
                            if skill_points >= skill_tree_eco_path_1_cost:
                                skill_tree_eco_path_1_limit_had += 1
                                skill_tree_money_multi += 0.1
                                skill_tree_eco_path_1_scale = 0.9
                                skill_points -= skill_tree_eco_path_1_cost
                                skill_tree_eco_path_1_color = green
                    skill_tree_eco_path_1_scale = 0.9

                # skill tree eco path 2
                if skill_tree_eco_path_2.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_eco_path_1_limit_had >= skill_tree_eco_path_1_limit:
                        if skill_tree_eco_path_2_limit_had + 1 <= skill_tree_eco_path_2_limit:
                            if skill_points >= skill_tree_eco_path_2_cost:
                                skill_tree_eco_path_2_limit_had += 1
                                skill_tree_discount += 0.1
                                discount += skill_tree_discount
                                skill_tree_eco_path_2_scale = 0.9
                                skill_points -= skill_tree_eco_path_2_cost
                                skill_tree_eco_path_2_color = green
                    skill_tree_eco_path_2_scale = 0.9

                # skill tree eco path 3
                if skill_tree_eco_path_3.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_eco_path_1_limit_had >= skill_tree_eco_path_1_limit\
                    and skill_tree_eco_path_2_limit_had >= skill_tree_eco_path_2_limit:
                        if skill_tree_eco_path_3_limit_had + 1 <= skill_tree_eco_path_3_limit:
                            if skill_points >= skill_tree_eco_path_3_cost:
                                skill_tree_eco_path_3_limit_had += 1
                                skill_tree_eco_path_3_scale = 0.9
                                skill_points -= skill_tree_eco_path_3_cost
                                skill_tree_eco_path_3_color = green
                    skill_tree_eco_path_3_scale = 0.9

                # skill tree eco path 4
                if skill_tree_eco_path_4.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_eco_path_1_limit_had >= skill_tree_eco_path_1_limit\
                    and skill_tree_eco_path_2_limit_had >= skill_tree_eco_path_2_limit and skill_tree_eco_path_3_limit_had >= skill_tree_eco_path_3_limit:
                        if skill_tree_eco_path_4_limit_had + 1 <= skill_tree_eco_path_4_limit:
                            if skill_points >= skill_tree_eco_path_4_cost:
                                skill_tree_eco_path_4_limit_had += 1
                                skill_tree_eco_path_4_scale = 0.9
                                skill_points -= skill_tree_eco_path_4_cost
                                skill_tree_eco_path_4_color = green
                    skill_tree_eco_path_4_scale = 0.9

                # skill tree eco path 5
                if skill_tree_eco_path_5.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_eco_path_1_limit_had >= skill_tree_eco_path_1_limit\
                    and skill_tree_eco_path_2_limit_had >= skill_tree_eco_path_2_limit and skill_tree_eco_path_3_limit_had >= skill_tree_eco_path_3_limit\
                    and skill_tree_eco_path_4_limit_had >= skill_tree_eco_path_4_limit:
                        if skill_tree_eco_path_5_limit_had + 1 <= skill_tree_eco_path_5_limit:
                            if skill_points >= skill_tree_eco_path_5_cost:
                                skill_tree_eco_path_5_limit_had += 1
                                skill_tree_eco_path_5_scale = 0.9
                                skill_points -= skill_tree_eco_path_5_cost
                                skill_tree_eco_path_5_color = green
                    skill_tree_eco_path_5_scale = 0.9

                # skill tree prog path 1
                if skill_tree_prog_path_1.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit:
                        if skill_tree_prog_path_1_limit_had + 1 <= skill_tree_prog_path_1_limit:
                            if skill_points >= skill_tree_prog_path_1_cost:
                                skill_tree_prog_path_1_limit_had += 1
                                skill_tree_prog_path_1_scale = 0.9
                                skill_points -= skill_tree_prog_path_1_cost
                                skill_tree_prog_path_1_color = green
                    skill_tree_prog_path_1_scale = 0.9

                # skill tree prog path 2
                if skill_tree_prog_path_2.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_prog_path_1_limit_had >= skill_tree_prog_path_1_limit:
                        if skill_tree_prog_path_2_limit_had + 1 <= skill_tree_prog_path_2_limit:
                            if skill_points >= skill_tree_prog_path_2_cost:
                                skill_tree_prog_path_2_limit_had += 1
                                base_auto_click_time = base_auto_click_time / 2
                                skill_tree_prog_path_2_scale = 0.9
                                skill_points -= skill_tree_prog_path_2_cost
                                skill_tree_prog_path_2_color = green
                    skill_tree_prog_path_2_scale = 0.9

                # skill tree prog path 3
                if skill_tree_prog_path_3.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_prog_path_1_limit_had >= skill_tree_prog_path_1_limit\
                    and skill_tree_prog_path_2_limit_had >= skill_tree_prog_path_2_limit:
                        if skill_tree_prog_path_3_limit_had + 1 <= skill_tree_prog_path_3_limit:
                            if skill_points >= skill_tree_prog_path_3_cost:
                                skill_tree_prog_path_3_limit_had += 1
                                skill_tree_prog_path_3_scale = 0.9
                                skill_points -= skill_tree_prog_path_3_cost
                                skill_tree_prog_path_3_color = green
                    skill_tree_prog_path_3_scale = 0.9

                # skill tree prog path 4
                if skill_tree_prog_path_4.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_prog_path_1_limit_had >= skill_tree_prog_path_1_limit\
                    and skill_tree_prog_path_2_limit_had >= skill_tree_prog_path_2_limit and skill_tree_prog_path_3_limit_had >= skill_tree_prog_path_3_limit:
                        if skill_tree_prog_path_4_limit_had + 1 <= skill_tree_prog_path_4_limit:
                            if skill_points >= skill_tree_prog_path_4_cost:
                                skill_tree_prog_path_4_limit_had += 1
                                skill_tree_prog_path_4_scale = 0.9
                                skill_points -= skill_tree_prog_path_4_cost
                                skill_tree_prog_path_4_color = green
                    skill_tree_prog_path_4_scale = 0.9

                # skill tree prog path 5
                if skill_tree_prog_path_5.collidepoint(event.pos) and gui == 4:
                    if skill_tree_unlock_limit_had >= skill_tree_unlock_limit and skill_tree_prog_path_1_limit_had >= skill_tree_prog_path_1_limit\
                    and skill_tree_prog_path_2_limit_had >= skill_tree_prog_path_2_limit and skill_tree_prog_path_3_limit_had >= skill_tree_prog_path_3_limit\
                    and skill_tree_prog_path_4_limit_had >= skill_tree_prog_path_4_limit:
                        if skill_tree_prog_path_5_limit_had + 1 <= skill_tree_prog_path_5_limit:
                            if skill_points >= skill_tree_prog_path_5_cost:
                                skill_tree_prog_path_5_limit_had += 1
                                skill_tree_prog_path_5_scale = 0.9
                                skill_points -= skill_tree_prog_path_5_cost
                                skill_tree_prog_path_5_color = green
                    skill_tree_prog_path_5_scale = 0.9

                # button next
                if button_next.collidepoint(event.pos):
                    if enemies_had >= enemies_need:
                        current_index = (current_index + 1) % len(images)
                        scaled_image = scale_image()
                        image = scaled_image.get_rect(center=(int(width / 1.597) + 25, int(height / 2.5)))
                        wave += 1
                        if wave >= best_wave:
                            enemies_had = 0
                            best_wave = wave
                        if wave + 1 < best_wave:
                            enemies_had = enemies_need
                        max_health = max_health * wave_health_multi
                        health = max_health
                        button_scale_next = 0.9
                        base_gain = base_gain * 1.2
                    else:
                        next_clicker_is = True
                        save_time = time_passed_2
                    button_scale_next = 0.9

                # button back
                if button_back.collidepoint(event.pos):
                    if wave > 1:
                        current_index = (current_index - 1) % len(images)
                        scaled_image = scale_image()
                        image = scaled_image.get_rect(center=(int(width / 1.597) + 25, int(height / 2.5)))
                        wave -= 1
                        enemies_had = enemies_need
                        if wave == 1:
                            max_health = 10
                        else:
                            max_health = max_health / wave_health_multi
                        health = max_health
                        base_gain = base_gain / 1.2
                    button_scale_back = 0.9

                # button auto next
                if button_auto_next.collidepoint(event.pos):
                    if auto_next_is:
                        auto_next_is = False
                    else:
                        auto_next_is = True
                    button_scale_auto_next = 0.9

                # button auto click
                if button_auto_click.collidepoint(event.pos):
                    if auto_click_is:
                        auto_click_is = False
                    else:
                        auto_click_is = True
                    button_scale_auto_click = 0.9

                # button gui 1
                if button_gui_1.collidepoint(event.pos):
                    gui = 1
                    button_scale_gui_1 = 0.9

                # button gui 2
                if button_gui_2.collidepoint(event.pos):
                    gui = 2
                    button_scale_gui_2 = 0.9

                # button gui 3
                if button_gui_3.collidepoint(event.pos):
                    gui = 3
                    button_scale_gui_3 = 0.9

                # button gui 4
                if button_gui_4.collidepoint(event.pos):
                    gui = 4
                    button_scale_gui_4 = 0.9

                # button gui 5
                if button_gui_5.collidepoint(event.pos):
                    gui = 5
                    button_scale_gui_5 = 0.9

                # button save
                if button_save.collidepoint(event.pos):
                    button_scale_save = 0.9
                    save_game()

                # button prestige
                if button_prestige.collidepoint(event.pos) and gui == 3:
                    if prestige_tokens_gain > 0:
                        prestige_tokens += prestige_tokens_gain
                        enemies_need = 10 - prestige_enemy_red
                        discount = 1 + skill_tree_discount

                        damage_per_second_multi = 1
                        click_damage_multi = 1

                        wave = 1
                        best_wave = wave

                        button_1_limit_had = 0
                        button_2_limit_had = 0
                        button_3_limit_had = 0
                        button_4_limit_had = 0
                        button_5_limit_had = 0
                        button_6_limit_had = 0
                        button_7_limit_had = 0
                        button_8_limit_had = 0
                        button_9_limit_had = 0
                        button_10_limit_had = 0

                        button_upgrade_1_limit_had = 0
                        button_upgrade_2_limit_had = 0
                        button_upgrade_3_limit_had = 0
                        button_upgrade_4_limit_had = 0
                        button_upgrade_5_limit_had = 0

                        button_1_cost = 10
                        button_2_cost = 10
                        button_3_cost = 50
                        button_4_cost = 200
                        button_5_cost = 1000
                        button_6_cost = 5000
                        button_7_cost = 10000
                        button_8_cost = 50000
                        button_9_cost = 100000
                        button_10_cost = 500000

                        button_upgrade_1_cost = 10000
                        button_upgrade_2_cost = 10000
                        button_upgrade_3_cost = 100000
                        button_upgrade_4_cost = 10000000
                        button_upgrade_5_cost = 1000000000

                        base_gain = 5

                        gold = 0
                        money_multiplier = 1

                        damage_per_second = 0
                        click_damage = 1

                        health = 10
                        max_health = 10
                    button_scale_prestige = 0.9

    # hover
    target_clicker = 1.1 if clicker.collidepoint(mouse_pos) else 1

    target_button_1 = 1.1 if button_1.collidepoint(mouse_pos) else 1
    target_button_2 = 1.1 if button_2.collidepoint(mouse_pos) else 1
    target_button_3 = 1.1 if button_3.collidepoint(mouse_pos) else 1
    target_button_4 = 1.1 if button_4.collidepoint(mouse_pos) else 1
    target_button_5 = 1.1 if button_5.collidepoint(mouse_pos) else 1
    target_button_6 = 1.1 if button_6.collidepoint(mouse_pos) else 1
    target_button_7 = 1.1 if button_7.collidepoint(mouse_pos) else 1
    target_button_8 = 1.1 if button_8.collidepoint(mouse_pos) else 1
    target_button_9 = 1.1 if button_9.collidepoint(mouse_pos) else 1
    target_button_10 = 1.1 if button_10.collidepoint(mouse_pos) else 1

    target_button_upgrade_1 = 1.1 if button_upgrade_1.collidepoint(mouse_pos) else 1
    target_button_upgrade_2 = 1.1 if button_upgrade_2.collidepoint(mouse_pos) else 1
    target_button_upgrade_3 = 1.1 if button_upgrade_3.collidepoint(mouse_pos) else 1
    target_button_upgrade_4 = 1.1 if button_upgrade_4.collidepoint(mouse_pos) else 1
    target_button_upgrade_5 = 1.1 if button_upgrade_5.collidepoint(mouse_pos) else 1

    target_button_prestige_upgrade_1 = 1.1 if button_prestige_upgrade_1.collidepoint(mouse_pos) else 1
    target_button_prestige_upgrade_2 = 1.1 if button_prestige_upgrade_2.collidepoint(mouse_pos) else 1
    target_button_prestige_upgrade_3 = 1.1 if button_prestige_upgrade_3.collidepoint(mouse_pos) else 1
    target_button_prestige_upgrade_4 = 1.1 if button_prestige_upgrade_4.collidepoint(mouse_pos) else 1

    target_button_next = 1.1 if button_next.collidepoint(mouse_pos) else 1
    target_button_back = 1.1 if button_back.collidepoint(mouse_pos) else 1

    target_button_auto_next = 1.1 if button_auto_next.collidepoint(mouse_pos) else 1
    target_button_auto_click = 1.1 if button_auto_click.collidepoint(mouse_pos) else 1

    target_button_gui_1 = 1.1 if button_gui_1.collidepoint(mouse_pos) else 1
    target_button_gui_2 = 1.1 if button_gui_2.collidepoint(mouse_pos) else 1
    target_button_gui_3 = 1.1 if button_gui_3.collidepoint(mouse_pos) else 1
    target_button_gui_4 = 1.1 if button_gui_4.collidepoint(mouse_pos) else 1
    target_button_gui_5 = 1.1 if button_gui_5.collidepoint(mouse_pos) else 1

    target_skill_tree_unlock = 1.1 if skill_tree_unlock.collidepoint(mouse_pos) else 1
    target_skill_tree_dmg_path_1 = 1.1 if skill_tree_dmg_path_1.collidepoint(mouse_pos) else 1
    target_skill_tree_dmg_path_2 = 1.1 if skill_tree_dmg_path_2.collidepoint(mouse_pos) else 1
    target_skill_tree_dmg_path_3 = 1.1 if skill_tree_dmg_path_3.collidepoint(mouse_pos) else 1
    target_skill_tree_dmg_path_4 = 1.1 if skill_tree_dmg_path_4.collidepoint(mouse_pos) else 1
    target_skill_tree_dmg_path_5 = 1.1 if skill_tree_dmg_path_5.collidepoint(mouse_pos) else 1

    target_skill_tree_eco_path_1 = 1.1 if skill_tree_eco_path_1.collidepoint(mouse_pos) else 1
    target_skill_tree_eco_path_2 = 1.1 if skill_tree_eco_path_2.collidepoint(mouse_pos) else 1
    target_skill_tree_eco_path_3 = 1.1 if skill_tree_eco_path_3.collidepoint(mouse_pos) else 1
    target_skill_tree_eco_path_4 = 1.1 if skill_tree_eco_path_4.collidepoint(mouse_pos) else 1
    target_skill_tree_eco_path_5 = 1.1 if skill_tree_eco_path_5.collidepoint(mouse_pos) else 1

    target_skill_tree_prog_path_1 = 1.1 if skill_tree_prog_path_1.collidepoint(mouse_pos) else 1
    target_skill_tree_prog_path_2 = 1.1 if skill_tree_prog_path_2.collidepoint(mouse_pos) else 1
    target_skill_tree_prog_path_3 = 1.1 if skill_tree_prog_path_3.collidepoint(mouse_pos) else 1
    target_skill_tree_prog_path_4 = 1.1 if skill_tree_prog_path_4.collidepoint(mouse_pos) else 1
    target_skill_tree_prog_path_5 = 1.1 if skill_tree_prog_path_5.collidepoint(mouse_pos) else 1

    target_button_prestige = 1.1 if button_prestige.collidepoint(mouse_pos) else 1

    target_button_save = 1.1 if button_save.collidepoint(mouse_pos) else 1

    target_image = 1.1 if clicker.collidepoint(mouse_pos) else 1

    # scaling
    clicker_scale += (target_clicker - clicker_scale) * 0.1

    button_scale_1 += (target_button_1 - button_scale_1) * 0.1
    button_scale_2 += (target_button_2 - button_scale_2) * 0.1
    button_scale_3 += (target_button_3 - button_scale_3) * 0.1
    button_scale_4 += (target_button_4 - button_scale_4) * 0.1
    button_scale_5 += (target_button_5 - button_scale_5) * 0.1
    button_scale_6 += (target_button_6 - button_scale_6) * 0.1
    button_scale_7 += (target_button_7 - button_scale_7) * 0.1
    button_scale_8 += (target_button_8 - button_scale_8) * 0.1
    button_scale_9 += (target_button_9 - button_scale_9) * 0.1
    button_scale_10 += (target_button_10 - button_scale_10) * 0.1

    button_scale_upgrade_1 += (target_button_upgrade_1 - button_scale_upgrade_1) * 0.1
    button_scale_upgrade_2 += (target_button_upgrade_2 - button_scale_upgrade_2) * 0.1
    button_scale_upgrade_3 += (target_button_upgrade_3 - button_scale_upgrade_3) * 0.1
    button_scale_upgrade_4 += (target_button_upgrade_4 - button_scale_upgrade_4) * 0.1
    button_scale_upgrade_5 += (target_button_upgrade_5 - button_scale_upgrade_5) * 0.1

    button_scale_prestige_upgrade_1 += (target_button_prestige_upgrade_1 - button_scale_prestige_upgrade_1) * 0.1
    button_scale_prestige_upgrade_2 += (target_button_prestige_upgrade_2 - button_scale_prestige_upgrade_2) * 0.1
    button_scale_prestige_upgrade_3 += (target_button_prestige_upgrade_3 - button_scale_prestige_upgrade_3) * 0.1
    button_scale_prestige_upgrade_4 += (target_button_prestige_upgrade_4 - button_scale_prestige_upgrade_4) * 0.1

    skill_tree_unlock_scale += (target_skill_tree_unlock - skill_tree_unlock_scale) * 0.1
    skill_tree_dmg_path_1_scale += (target_skill_tree_dmg_path_1 - skill_tree_dmg_path_1_scale) * 0.1
    skill_tree_dmg_path_2_scale += (target_skill_tree_dmg_path_2 - skill_tree_dmg_path_2_scale) * 0.1
    skill_tree_dmg_path_3_scale += (target_skill_tree_dmg_path_3 - skill_tree_dmg_path_3_scale) * 0.1
    skill_tree_dmg_path_4_scale += (target_skill_tree_dmg_path_4 - skill_tree_dmg_path_4_scale) * 0.1
    skill_tree_dmg_path_5_scale += (target_skill_tree_dmg_path_5 - skill_tree_dmg_path_5_scale) * 0.1

    skill_tree_eco_path_1_scale += (target_skill_tree_eco_path_1 - skill_tree_eco_path_1_scale) * 0.1
    skill_tree_eco_path_2_scale += (target_skill_tree_eco_path_2 - skill_tree_eco_path_2_scale) * 0.1
    skill_tree_eco_path_3_scale += (target_skill_tree_eco_path_3 - skill_tree_eco_path_3_scale) * 0.1
    skill_tree_eco_path_4_scale += (target_skill_tree_eco_path_4 - skill_tree_eco_path_4_scale) * 0.1
    skill_tree_eco_path_5_scale += (target_skill_tree_eco_path_5 - skill_tree_eco_path_5_scale) * 0.1

    skill_tree_prog_path_1_scale += (target_skill_tree_prog_path_1 - skill_tree_prog_path_1_scale) * 0.1
    skill_tree_prog_path_2_scale += (target_skill_tree_prog_path_2 - skill_tree_prog_path_2_scale) * 0.1
    skill_tree_prog_path_3_scale += (target_skill_tree_prog_path_3 - skill_tree_prog_path_3_scale) * 0.1
    skill_tree_prog_path_4_scale += (target_skill_tree_prog_path_4 - skill_tree_prog_path_4_scale) * 0.1
    skill_tree_prog_path_5_scale += (target_skill_tree_prog_path_5 - skill_tree_prog_path_5_scale) * 0.1

    button_scale_next += (target_button_next - button_scale_next) * 0.1
    button_scale_back += (target_button_back - button_scale_back) * 0.1

    button_scale_auto_next += (target_button_auto_next - button_scale_auto_next) * 0.1
    button_scale_auto_click += (target_button_auto_click - button_scale_auto_click) * 0.1

    button_scale_gui_1 += (target_button_gui_1 - button_scale_gui_1) * 0.1
    button_scale_gui_2 += (target_button_gui_2 - button_scale_gui_2) * 0.1
    button_scale_gui_3 += (target_button_gui_3 - button_scale_gui_3) * 0.1
    button_scale_gui_4 += (target_button_gui_4 - button_scale_gui_4) * 0.1
    button_scale_gui_5 += (target_button_gui_5 - button_scale_gui_5) * 0.1

    button_scale_prestige += (target_button_prestige - button_scale_prestige) * 0.1

    button_scale_save += (target_button_save - button_scale_save) * 0.1

    scale += (target_image - scale) * 0.1

    # combo
    if current_time - last_click_time > combo_timeout:
        combo = 1
        combo_multi = 1

    # warning for next
    time_passed_2 += delta_time
    if save_time > 0:
        next_text_position = (int(width / 1.93), int(height / 4))
        draw_text_with_outline(screen, "You Can't Go Next Yet", font_font_bigger, (255, 0, 0), (0, 0, 0),(next_text_position[0], next_text_position[1]))
        if time_passed_2 >= save_time + 3:
            save_time = 0
            next_clicker_is = False

    # Skill Tree
    if enemies_needed_skill_tree_had >= enemies_needed_skill_tree:
        skill_points += 1
        enemies_needed_skill_tree_had = 0

    # health
    if health <= 0:
        health = max_health
        if skill_tree_eco_path_3_limit_had >= skill_tree_eco_path_3_limit:
            gold_random = random.randint(1, 5)
            if gold_random == 1:
                gold += money_overall * 2
            else:
                gold += money_overall
        else:
            gold += money_overall
        enemies_needed_skill_tree_had += 1
        if enemies_had + 1 > enemies_need:
            enemies_had = enemies_need
        else:
            enemies_had += 1

    # dmg/s
    time_passed += delta_time
    if time_passed >= 1:
        if skill_tree_dmg_path_5_limit_had >= skill_tree_dmg_path_5_limit:
            if health <= max_health * 0.3:
                health -= DPS_overall * 1.5
            else:
                health -= DPS_overall
        else:
            health -= DPS_overall
        time_passed -= 1

    # auto next
    if skill_tree_prog_path_4_limit_had >= skill_tree_prog_path_4_limit:
        if auto_next_is:
            if enemies_had >= enemies_need:
                current_index = (current_index + 1) % len(images)
                scaled_image = scale_image()
                image = scaled_image.get_rect(center=(int(width / 1.597) + 25, int(height / 2.5)))
                enemies_had = 0
                wave += 1
                max_health = max_health * wave_health_multi
                health = max_health
                button_scale_next = 0.9
                base_gain = base_gain * 1.2

    # auto click
    time_passed_3 += delta_time
    if skill_tree_prog_path_1_limit_had >= skill_tree_prog_path_1_limit:
        while auto_click_is and time_passed_3 >= base_auto_click_time / skill_tree_overdrive_speed_multi:
            random_position_1 = random.randint(700, 850)
            random_position_2 = random.randint(300, 400)
            save_time_2 = time_passed_4
            if random.randint(1, 10) == 1 and skill_tree_dmg_path_3_limit_had == 1:
                crit_multi_auto = 2
            if skill_tree_prog_path_3_limit_had >= skill_tree_prog_path_3_limit:
                if skill_tree_dmg_path_5_limit_had >= skill_tree_dmg_path_5_limit:
                    if health <= max_health * 0.3:
                        health -= DPC_overall * crit_multi_auto * 1.2 * 1.5
                        damage_popup.append([random_position_1, random_position_2, notation(DPC_overall * crit_multi_auto * 1.2 * 1.5), 1.0])
                    else:
                        health -= DPC_overall * crit_multi_auto * 1.2
                        damage_popup.append([random_position_1, random_position_2, notation(DPC_overall * crit_multi_auto * 1.2), 1.0])
                else:
                    health -= DPC_overall * crit_multi_auto * 1.2
                    damage_popup.append([random_position_1, random_position_2, notation(DPC_overall * crit_multi_auto * 1.2), 1.0])
            else:
                health -= DPC_overall * crit_multi_auto
                damage_popup.append([random_position_1, random_position_2, notation(DPC_overall * crit_multi_auto), 1.0])
            crit_multi_auto = 1
            time_passed_3 -= base_auto_click_time
            if skill_tree_dmg_path_4_limit_had == 1:
                if current_time - last_click_time <= combo_timeout:
                    combo += 1
                    combo_multi += 0.001
                else:
                    combo = 1
                last_click_time = current_time
            if skill_tree_eco_path_4_limit_had >= skill_tree_eco_path_4_limit:
                gold += money_overall / 100
            clicker_scale = 0.9

    # prestige
    if gold >= 1000000:
        prestige_tokens_gain = int(gold / 1000000) * prestige_tokens_multiplier
    else:
        prestige_tokens_gain = 0

    # prestige dmg
    if prestige_tokens > 0:
        prestige_dmg_multi = prestige_tokens / 100
    else:
        prestige_dmg_multi = 1

    # wave multi
    if skill_tree_eco_path_5_limit_had >= skill_tree_eco_path_5_limit:
        skill_tree_wave_multi = 1 + (wave / 100)
    else:
        skill_tree_wave_multi = 1

    # random choices skill prog path 5
    if skill_tree_prog_path_5_limit_had >= skill_tree_prog_path_5_limit:
        if not overdrive_active and now - last_overdrive_time >= OVERDRIVE_INTERVAL:
            overdrive_active = True
            overdrive_start_time = now
            last_overdrive_time = now

            # pick random buff
            overdrive_type = random.choice(["DAMAGE", "SPEED"])
            if overdrive_type == "DAMAGE":
                skill_tree_overdrive_dmg_multi = skill_tree_overdrive_dmg_multi * 2
            else:
                skill_tree_overdrive_speed_multi = skill_tree_overdrive_speed_multi * 1.5

    if overdrive_active and now - overdrive_start_time >= OVERDRIVE_DURATION:
        overdrive_active = False
        skill_tree_overdrive_dmg_multi = 1
        skill_tree_overdrive_speed_multi = 1
        overdrive_type = None

    # overdrive text draw
    if overdrive_active:
        draw_text_with_outline(screen, f"OVERDRIVE: {overdrive_type}  ACTIVE", font_font, (255, 255, 255), (0, 0, 0),(int(width / 1.8), int(height / 1.8)))

    # text button draw:
    if gui == 1:
        # button 1
        button_1_positon = (int(width / 11) - 2, int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_1_cost / discount)}", font_font,(255,255,255),(0,0,0), (button_1_positon[0], button_1_positon[1] - 15))
        # text
        draw_text_with_outline(screen, "+1 DPC", font_font,(255,255,255),(0,0,0), (button_1_positon[0] - 25, button_1_positon[1] - 85))
        # emoji
        draw_text_with_outline(screen, "🗡️", font_emoji,(255,255,255),(0,0,0), (button_1_positon[0] - 115, button_1_positon[1] - 90))
        # limit
        draw_text_with_outline(screen, f"{button_1_limit_had} / {button_1_limit}", font_font,(255,255,255),(0,0,0), (button_1_positon[0] - 93, button_1_positon[1] - 10))

        # button 2
        button_2_positon = (int(width / 11) - 2, int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_2_cost / discount)}", font_font,(255,255,255),(0,0,0), (button_2_positon[0], button_2_positon[1] + 105))
        # text
        draw_text_with_outline(screen, "+2 DPS", font_font,(255,255,255),(0,0,0), (button_2_positon[0] - 25, button_2_positon[1] + 35))
        # emoji
        draw_text_with_outline(screen, "🔥", font_emoji,(255,255,255),(0,0,0), (button_1_positon[0] - 115, button_1_positon[1] + 28))
        # limit
        draw_text_with_outline(screen, f"{button_2_limit_had} / {button_2_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] - 93, button_1_positon[1] + 110))

        # button 3
        button_3_positon = (int(width / 11) - 2, int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_3_cost / discount)}", font_font,(255,255,255),(0,0,0), (button_3_positon[0], button_3_positon[1] + 225))
        # text
        draw_text_with_outline(screen, "+8 DPS", font_font,(255,255,255),(0,0,0), (button_3_positon[0] - 25, button_3_positon[1] + 155))
        # emoji
        draw_text_with_outline(screen, "⚡", font_emoji, (255, 255, 255), (0, 0, 0),(button_1_positon[0] - 115, button_1_positon[1] + 146))
        # limit
        draw_text_with_outline(screen, f"{button_3_limit_had} / {button_3_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] - 93, button_1_positon[1] + 230))

        # button 4
        button_4_positon = (int(width / 11) - 2, int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_4_cost / discount)}", font_font,(255,255,255),(0,0,0), (button_4_positon[0] - 5, button_4_positon[1] + 345))
        # text
        draw_text_with_outline(screen, "+20 DPC", font_font,(255,255,255),(0,0,0), (button_4_positon[0] - 25, button_4_positon[1] + 275))
        # emoji
        draw_text_with_outline(screen, "🪓", font_emoji, (255, 255, 255), (0, 0, 0),(button_1_positon[0] - 115, button_1_positon[1] + 264))
        # limit
        draw_text_with_outline(screen, f"{button_4_limit_had} / {button_4_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] - 93, button_1_positon[1] + 350))

        # button 5
        button_5_positon = (int(width / 11) - 2, int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_5_cost / discount)}", font_font,(255,255,255),(0,0,0), (button_5_positon[0] - 12, button_5_positon[1] + 465))
        # text
        draw_text_with_outline(screen, "+100 DPS", font_font,(255,255,255),(0,0,0), (button_5_positon[0] - 25, button_5_positon[1] + 395))
        # emoji
        draw_text_with_outline(screen, "☠️", font_emoji, (255, 255, 255), (0, 0, 0),(button_1_positon[0] - 115, button_1_positon[1] + 382))
        # limit
        draw_text_with_outline(screen, f"{button_5_limit_had} / {button_5_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] - 93, button_1_positon[1] + 470))

        # button 6
        button_6_positon = (int(width / 3.6), int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_6_cost / discount)}", font_font, (255, 255, 255), (0, 0, 0),(button_6_positon[0] - 30, button_6_positon[1] - 17))
        # text
        draw_text_with_outline(screen, "+500 DPC", font_font, (255, 255, 255), (0, 0, 0),(button_6_positon[0] - 45, button_6_positon[1] - 85))
        # emoji
        draw_text_with_outline(screen, "🖱️", font_emoji, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 90, button_1_positon[1] - 90))
        # limit
        draw_text_with_outline(screen, f"{button_6_limit_had} / {button_6_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 110, button_1_positon[1] - 10))

        # button 7
        button_7_positon = (int(width / 3.6), int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_7_cost / discount)}", font_font, (255, 255, 255), (0, 0, 0),(button_7_positon[0] - 30, button_7_positon[1] + 103))
        # text
        draw_text_with_outline(screen, "+2500 DPS", font_font, (255, 255, 255), (0, 0, 0),(button_7_positon[0] - 45, button_7_positon[1] + 35))
        # emoji
        draw_text_with_outline(screen, "💀", font_emoji, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 90, button_1_positon[1] + 20))
        # limit
        draw_text_with_outline(screen, f"{button_7_limit_had} / {button_7_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 110, button_1_positon[1] + 110))

        # button 8
        button_8_positon = (int(width / 3.6), int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_8_cost / discount)}", font_font, (255, 255, 255), (0, 0, 0),(button_8_positon[0] - 30, button_8_positon[1] + 223))
        # text
        draw_text_with_outline(screen, "+10K DPS", font_font, (255, 255, 255), (0, 0, 0),(button_8_positon[0] - 45, button_8_positon[1] + 155))
        # emoji
        draw_text_with_outline(screen, "🌪️", font_emoji, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 90, button_1_positon[1] + 140))
        # limit
        draw_text_with_outline(screen, f"{button_8_limit_had} / {button_8_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 110, button_1_positon[1] + 230))

        # button 9
        button_9_positon = (int(width / 3.6), int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_9_cost / discount)}", font_font, (255, 255, 255), (0, 0, 0),(button_9_positon[0] - 30, button_9_positon[1] + 343))
        # text
        draw_text_with_outline(screen, "+40K DPC", font_font, (255, 255, 255), (0, 0, 0),(button_9_positon[0] - 45, button_9_positon[1] + 275))
        # emoji
        draw_text_with_outline(screen, "👊", font_emoji, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 90, button_1_positon[1] + 260))
        # limit
        draw_text_with_outline(screen, f"{button_9_limit_had} / {button_9_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 110, button_1_positon[1] + 350))

        # button 10
        button_10_positon = (int(width / 3.6), int(height / 4.3) - 15)
        # cost
        draw_text_with_outline(screen, f"{notation(button_10_cost / discount)}", font_font, (255, 255, 255), (0, 0, 0),(button_10_positon[0] - 30, button_10_positon[1] + 463))
        # text
        draw_text_with_outline(screen, "+150K DPS", font_font, (255, 255, 255), (0, 0, 0),(button_10_positon[0] - 45, button_10_positon[1] + 395))
        # emoji
        draw_text_with_outline(screen, "🧪", font_emoji, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 90, button_1_positon[1] + 380))
        # limit
        draw_text_with_outline(screen, f"{button_10_limit_had} / {button_10_limit}", font_font, (255, 255, 255), (0, 0, 0),(button_1_positon[0] + 110, button_1_positon[1] + 470))

        # draw upgrade buttons
        pygame.draw.rect(screen, (255, 0, 0), button_1, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_2, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_3, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_4, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_5, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_6, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_7, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_8, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_9, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_10, border_radius=15)
        pygame.draw.rect(screen, black, button_1,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_2,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_3,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_4,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_5,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_6,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_7,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_8,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_9,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_10,width=6, border_radius=15)

        # buy text
        buy_text_position_1 = (int(width / 9.3) - 22, int(height / 5.8) - 12)
        buy_text_position_2 = (int(width / 9.3) - 22, int(height / 5.8) + 108)
        buy_text_position_3 = (int(width / 9.3) - 22, int(height / 5.8) + 228)
        buy_text_position_4 = (int(width / 9.3) - 22, int(height / 5.8) + 348)
        buy_text_position_5 = (int(width / 9.3) - 22, int(height / 5.8) + 468)

        buy_text_position_6 = (int(width / 3.6) - 22, int(height / 5.8) - 12)
        buy_text_position_7 = (int(width / 3.6) - 22, int(height / 5.8) + 108)
        buy_text_position_8 = (int(width / 3.6) - 22, int(height / 5.8) + 228)
        buy_text_position_9 = (int(width / 3.6) - 22, int(height / 5.8) + 348)
        buy_text_position_10 = (int(width / 3.6) - 22, int(height / 5.8) + 468)

        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_1[0], buy_text_position_1[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_2[0], buy_text_position_2[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_3[0], buy_text_position_3[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_4[0], buy_text_position_4[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_5[0], buy_text_position_5[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_6[0], buy_text_position_6[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_7[0], buy_text_position_7[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_8[0], buy_text_position_8[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_9[0], buy_text_position_9[1]))
        draw_text_with_outline(screen, "BUY", font_font, black, white, (buy_text_position_10[0], buy_text_position_10[1]))
    elif gui == 2:
        # button upgrade 1
        button_upgrade_1_position = (int(width / 4), int(height / 5.8))
        # cost
        draw_text_with_outline(screen, f"{notation(button_upgrade_1_cost / discount)}", font_font_medium, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 200, button_upgrade_1_position[1]))
        # text
        draw_text_with_outline(screen, "+50% DPS", font_font_medium, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] - 35))
        # emoji
        draw_text_with_outline(screen, "🔥", font_emoji_bigger, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 310, button_upgrade_1_position[1] - 50))
        # limit
        draw_text_with_outline(screen, f"{button_upgrade_1_limit_had} / {button_upgrade_1_limit}", font_font_medium, (255, 255, 255),(0, 0, 0), (button_upgrade_1_position[0] - 25, button_upgrade_1_position[1] + 50))

        # button upgrade 2
        button_upgrade_2_position = button_upgrade_1_position[0], button_upgrade_1_position[1] + 160
        # cost
        draw_text_with_outline(screen, f"{notation(button_upgrade_2_cost / discount)}", font_font_medium, (255, 255, 255),(0, 0, 0), (button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] + 120))
        # text
        draw_text_with_outline(screen, "+20% DPC", font_font_medium, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] + 85))
        # emoji
        draw_text_with_outline(screen, "⚔️", font_emoji_bigger, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 310, button_upgrade_1_position[1] + 70))
        # limit
        draw_text_with_outline(screen, f"{button_upgrade_2_limit_had} / {button_upgrade_2_limit}", font_font_medium,(255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 25, button_upgrade_1_position[1] + 170))

        # button upgrade 3
        button_upgrade_3_position = button_upgrade_2_position[0], button_upgrade_2_position[1] + 160
        # cost
        draw_text_with_outline(screen, f"{notation(button_upgrade_3_cost / discount)}", font_font_medium, (255, 255, 255),(0, 0, 0), (button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] + 240))
        # text
        draw_text_with_outline(screen, "+10% gold", font_font_medium, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] + 205))
        # emoji
        draw_text_with_outline(screen, "💰", font_emoji_bigger, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 310, button_upgrade_1_position[1] + 190))
        # limit
        draw_text_with_outline(screen, f"{button_upgrade_3_limit_had} / {button_upgrade_3_limit}", font_font_medium,(255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 25, button_upgrade_1_position[1] + 290))

        # button upgrade 4
        button_upgrade_4_position = button_upgrade_3_position[0], button_upgrade_3_position[1] + 160
        # cost
        draw_text_with_outline(screen, f"{notation(button_upgrade_4_cost / discount)}", font_font_medium, (255, 255, 255),(0, 0, 0), (button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] + 360))
        # text
        draw_text_with_outline(screen, "-1% cost", font_font_medium, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] + 325))
        # emoji
        draw_text_with_outline(screen, "💸", font_emoji_bigger, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 310, button_upgrade_1_position[1] + 310))
        # limit
        draw_text_with_outline(screen, f"{button_upgrade_4_limit_had} / {button_upgrade_4_limit}", font_font_medium,(255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 25, button_upgrade_1_position[1] + 410))

        # button upgrade 5
        button_upgrade_5_position = button_upgrade_4_position[0], button_upgrade_4_position[1] + 160
        # cost
        draw_text_with_outline(screen, f"{notation(button_upgrade_5_cost / discount)}", font_font_medium, (255, 255, 255),(0, 0, 0), (button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] + 480))
        # text
        draw_text_with_outline(screen, "-1 mob", font_font_medium, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 200, button_upgrade_1_position[1] + 445))
        # emoji
        draw_text_with_outline(screen, "🎯", font_emoji_bigger, (255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 310, button_upgrade_1_position[1] + 430))
        # limit
        draw_text_with_outline(screen, f"{button_upgrade_5_limit_had} / {button_upgrade_5_limit}", font_font_medium,(255, 255, 255), (0, 0, 0),(button_upgrade_1_position[0] - 25, button_upgrade_1_position[1] + 530))

        pygame.draw.rect(screen, (255, 0, 0), button_upgrade_1, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_upgrade_2, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_upgrade_3, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_upgrade_4, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_upgrade_5, border_radius=15)
        pygame.draw.rect(screen, black, button_upgrade_1,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_upgrade_2,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_upgrade_3,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_upgrade_4,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_upgrade_5,width=6, border_radius=15)

        # buy upgrades
        buy_upgrade_position_1 = int(width / 4) - 30, int(height / 6.4)
        buy_upgrade_position_2 = int(width / 4) - 30, int(height / 6.4) + 120
        buy_upgrade_position_3 = int(width / 4) - 30, int(height / 6.4) + 240
        buy_upgrade_position_4 = int(width / 4) - 30, int(height / 6.4) + 360
        buy_upgrade_position_5 = int(width / 4) - 30, int(height / 6.4) + 480


        draw_text_with_outline(screen, "BUY", font_font_bigger, black, white, (buy_upgrade_position_1[0], buy_upgrade_position_1[1]))
        draw_text_with_outline(screen, "BUY", font_font_bigger, black, white, (buy_upgrade_position_2[0], buy_upgrade_position_2[1]))
        draw_text_with_outline(screen, "BUY", font_font_bigger, black, white, (buy_upgrade_position_3[0], buy_upgrade_position_3[1]))
        draw_text_with_outline(screen, "BUY", font_font_bigger, black, white, (buy_upgrade_position_4[0], buy_upgrade_position_4[1]))
        draw_text_with_outline(screen, "BUY", font_font_bigger, black, white, (buy_upgrade_position_5[0], buy_upgrade_position_5[1]))
    elif gui == 3:
        # text Prestige
        draw_text_with_outline(screen,"Prestige", font_font_biggest, white, black, ((int(width / 10) +5) , int(height / 10)))
        draw_text_with_outline(screen,"For every 1M gold, you get 1 token", font_font_medium, white, black, (6 , int(height / 6)))
        draw_text_with_outline(screen,"Every 1 token gives 1% more damage", font_font, white, black, (20 , int(height / 6) + 40))
        draw_text_with_outline(screen,f"+{notation(prestige_tokens_gain)} Tokens", font_font_bigger, white, black, ((int(width / 10) - 5) , int(height / 4)))

        # prestige upgrade 1
        prestige_upgrade_1_position = int(width / 3.5) , int(height / 2.2)
        # cost
        draw_text_with_outline(screen,f"{notation(button_prestige_upgrade_1_cost)}", font_font_medium, white, black, (prestige_upgrade_1_position[0] - 200, prestige_upgrade_1_position[1] - 5))
        # text
        draw_text_with_outline(screen,"+200% DMG", font_font_medium, white, black, (prestige_upgrade_1_position[0] - 250, prestige_upgrade_1_position[1] - 30))
        # emoji
        draw_text_with_outline(screen, "💥", font_emoji, (255, 255, 255), (0, 0, 0),(prestige_upgrade_1_position[0] - 340, prestige_upgrade_1_position[1] - 40))
        # limit
        draw_text_with_outline(screen, f"{button_prestige_upgrade_1_limit_had} / {button_prestige_upgrade_1_limit}", font_font,(255, 255, 255), (0, 0, 0),(prestige_upgrade_1_position[0] + 12, prestige_upgrade_1_position[1] - 15))

        # prestige upgrade 2
        prestige_upgrade_2_position = int(width / 3.5), int(height / 2.2) + 80
        # cost
        draw_text_with_outline(screen, f"{notation(button_prestige_upgrade_2_cost)}", font_font_medium, white, black,(prestige_upgrade_2_position[0] - 200, prestige_upgrade_2_position[1] - 5))
        # text
        draw_text_with_outline(screen, "+50% GOLD", font_font_medium, white, black,(prestige_upgrade_2_position[0] - 250, prestige_upgrade_2_position[1] - 30))
        # emoji
        draw_text_with_outline(screen, "💎", font_emoji, (255, 255, 255), (0, 0, 0),(prestige_upgrade_2_position[0] - 340, prestige_upgrade_2_position[1] - 40))
        # limit
        draw_text_with_outline(screen, f"{button_prestige_upgrade_2_limit_had} / {button_prestige_upgrade_2_limit}",font_font, (255, 255, 255), (0, 0, 0),(prestige_upgrade_2_position[0] + 12, prestige_upgrade_2_position[1] - 15))

        # prestige upgrade 3
        prestige_upgrade_3_position = int(width / 3.5), int(height / 2.2) + 160
        # cost
        draw_text_with_outline(screen, f"{notation(button_prestige_upgrade_3_cost)}", font_font_medium, white, black,(prestige_upgrade_3_position[0] - 200, prestige_upgrade_3_position[1] - 5))
        # text
        draw_text_with_outline(screen, "PT Gain +20%", font_font, white, black,(prestige_upgrade_3_position[0] - 250, prestige_upgrade_3_position[1] - 30))
        # emoji
        draw_text_with_outline(screen, "🔮", font_emoji, (255, 255, 255), (0, 0, 0),(prestige_upgrade_3_position[0] - 340, prestige_upgrade_3_position[1] - 40))
        # limit
        draw_text_with_outline(screen, f"{button_prestige_upgrade_3_limit_had} / {button_prestige_upgrade_3_limit}",font_font, (255, 255, 255), (0, 0, 0),(prestige_upgrade_3_position[0] + 12, prestige_upgrade_3_position[1] - 15))

        # prestige upgrade 4
        prestige_upgrade_4_position = int(width / 3.5), int(height / 2.2) + 240
        # cost
        draw_text_with_outline(screen, f"{notation(button_prestige_upgrade_4_cost)}", font_font_medium, white, black,(prestige_upgrade_4_position[0] - 200, prestige_upgrade_4_position[1] - 5))
        # text
        draw_text_with_outline(screen, "-1 Mob", font_font_medium, white, black,(prestige_upgrade_4_position[0] - 250, prestige_upgrade_4_position[1] - 30))
        # emoji
        draw_text_with_outline(screen, "⚡", font_emoji, (255, 255, 255), (0, 0, 0),(prestige_upgrade_4_position[0] - 340, prestige_upgrade_4_position[1] - 40))
        # limit
        draw_text_with_outline(screen, f"{button_prestige_upgrade_4_limit_had} / {button_prestige_upgrade_4_limit}",font_font, (255, 255, 255), (0, 0, 0),(prestige_upgrade_4_position[0] + 12, prestige_upgrade_4_position[1] - 15))

        pygame.draw.rect(screen, (255, 0, 0), button_prestige_upgrade_1, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_prestige_upgrade_2, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_prestige_upgrade_3, border_radius=15)
        pygame.draw.rect(screen, (255, 0, 0), button_prestige_upgrade_4, border_radius=15)
        pygame.draw.rect(screen, black, button_prestige_upgrade_1,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_prestige_upgrade_2,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_prestige_upgrade_3,width=6, border_radius=15)
        pygame.draw.rect(screen, black, button_prestige_upgrade_4,width=6, border_radius=15)

        pygame.draw.rect(screen, (255, 0, 0), button_prestige, border_radius=15)
        pygame.draw.rect(screen, black, button_prestige,width=6, border_radius=15)
        draw_text_with_outline(screen,"Prestige", font_font_biggest, white, black, ((int(width / 10) +5) , int(height / 10) + 205))

        # buy
        buy_prestige_upgrade_position_1 = int(width / 3.5) - 67, int(height / 2.28)
        buy_prestige_upgrade_position_2 = int(width / 3.5) - 67, int(height / 2.28) + 80
        buy_prestige_upgrade_position_3 = int(width / 3.5) - 67, int(height / 2.28) + 160
        buy_prestige_upgrade_position_4 = int(width / 3.5) - 67, int(height / 2.28) + 240

        draw_text_with_outline(screen, "BUY", font_font_medium, black, white, (buy_prestige_upgrade_position_1[0], buy_prestige_upgrade_position_1[1]))
        draw_text_with_outline(screen, "BUY", font_font_medium, black, white, (buy_prestige_upgrade_position_2[0], buy_prestige_upgrade_position_2[1]))
        draw_text_with_outline(screen, "BUY", font_font_medium, black, white, (buy_prestige_upgrade_position_3[0], buy_prestige_upgrade_position_3[1]))
        draw_text_with_outline(screen, "BUY", font_font_medium, black, white, (buy_prestige_upgrade_position_4[0], buy_prestige_upgrade_position_4[1]))
    elif gui == 4:
        # text Skill tree
        draw_text_with_outline(screen, "Skill Tree", font_font_biggest, white, black,((int(width / 10) + 5), int(height / 10)))
        draw_text_with_outline(screen, "Every 100 kills you gain 1 skill point", font_font_medium, white, black,(25, int(height / 6)))
        draw_text_with_outline(screen, f"{skill_points} Skill Points", font_font_medium, white, black,(int(width / 9), int(height / 4.7) - 3))
        draw_text_with_outline(screen, f"{enemies_needed_skill_tree_had} / {enemies_needed_skill_tree} Enemies", font_font_bigger, white, black,(int(width / 10) - 20, int(height / 4)))

        # draw lines
        # middle
        pygame.draw.line(screen, black, (int(width / 6) , int(height / 3)), (int(width / 6) , int(height / 3) + 400), 10)
        # right
        pygame.draw.line(screen, black, (int(width / 6) , int(height / 3)), (int(width / 6) + 100 , int(height / 3) + 100), 10)
        pygame.draw.line(screen, black, (int(width / 6) + 100, int(height / 3) + 100), (int(width / 6) + 100, int(height / 3) + 400), 10)
        # left
        pygame.draw.line(screen, black, (int(width / 6), int(height / 3)),(int(width / 6) - 100, int(height / 3) + 100), 10)
        pygame.draw.line(screen, black, (int(width / 6) - 100, int(height / 3) + 100),(int(width / 6) - 100, int(height / 3) + 400), 10)



        # squares draw
        pygame.draw.rect(screen, skill_tree_unlock_color, skill_tree_unlock, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_unlock,width=6, border_radius=15)
        pygame.draw.rect(screen, skill_tree_dmg_path_1_color, skill_tree_dmg_path_1, border_radius=15)
        pygame.draw.rect(screen, skill_tree_dmg_path_2_color, skill_tree_dmg_path_2, border_radius=15)
        pygame.draw.rect(screen, skill_tree_dmg_path_3_color, skill_tree_dmg_path_3, border_radius=15)
        pygame.draw.rect(screen, skill_tree_dmg_path_4_color, skill_tree_dmg_path_4, border_radius=15)
        pygame.draw.rect(screen, skill_tree_dmg_path_5_color, skill_tree_dmg_path_5, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_dmg_path_1, width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_dmg_path_2, width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_dmg_path_3, width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_dmg_path_4, width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_dmg_path_5, width=6, border_radius=15)

        # skill tree unlock
        skill_tree_unlock_position = int(width / 6), int(height / 3)
        draw_text_with_outline(screen, "U1", font_font, white, black,(skill_tree_unlock_position[0] - 12, skill_tree_unlock_position[1] - 10))

        # skill tree dmg path 1
        skill_tree_dmg_path_1_position = skill_tree_unlock_position[0], skill_tree_unlock_position[1] + 100
        draw_text_with_outline(screen, "D1", font_font, white, black,(skill_tree_dmg_path_1_position[0] - 12, skill_tree_dmg_path_1_position[1] - 10))

        # skill tree dmg path 2
        skill_tree_dmg_path_2_position = skill_tree_unlock_position[0], skill_tree_unlock_position[1] + 170
        draw_text_with_outline(screen, "D2", font_font, white, black,(skill_tree_dmg_path_2_position[0] - 12, skill_tree_dmg_path_2_position[1] - 10))

        # skill tree dmg path 3
        skill_tree_dmg_path_3_position = skill_tree_unlock_position[0], skill_tree_unlock_position[1] + 240
        draw_text_with_outline(screen, "D3", font_font, white, black,(skill_tree_dmg_path_3_position[0] - 12, skill_tree_dmg_path_3_position[1] - 10))

        # skill tree dmg path 4
        skill_tree_dmg_path_4_position = skill_tree_unlock_position[0], skill_tree_unlock_position[1] + 310
        draw_text_with_outline(screen, "D4", font_font, white, black,(skill_tree_dmg_path_4_position[0] - 12, skill_tree_dmg_path_4_position[1] - 10))

        # skill tree dmg path 5
        skill_tree_dmg_path_5_position = skill_tree_unlock_position[0], skill_tree_unlock_position[1] + 380
        draw_text_with_outline(screen, "D5", font_font, white, black,(skill_tree_dmg_path_5_position[0] - 12, skill_tree_dmg_path_5_position[1] - 10))

        # draw eco path squares
        pygame.draw.rect(screen, skill_tree_eco_path_1_color, skill_tree_eco_path_1, border_radius=15)
        pygame.draw.rect(screen, skill_tree_eco_path_2_color, skill_tree_eco_path_2, border_radius=15)
        pygame.draw.rect(screen, skill_tree_eco_path_3_color, skill_tree_eco_path_3, border_radius=15)
        pygame.draw.rect(screen, skill_tree_eco_path_4_color, skill_tree_eco_path_4, border_radius=15)
        pygame.draw.rect(screen, skill_tree_eco_path_5_color, skill_tree_eco_path_5, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_eco_path_1, width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_eco_path_2, width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_eco_path_3, width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_eco_path_4, width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_eco_path_5, width=6, border_radius=15)

        # skill tree eco path 1
        skill_tree_eco_path_1_position = skill_tree_unlock_position[0] + 100, skill_tree_unlock_position[1] + 100
        draw_text_with_outline(screen, "E1", font_font, white, black,(skill_tree_eco_path_1_position[0] - 12, skill_tree_eco_path_1_position[1] - 10))

        # skill tree eco path 2
        skill_tree_eco_path_2_position = skill_tree_unlock_position[0] + 100, skill_tree_unlock_position[1] + 170
        draw_text_with_outline(screen, "E2", font_font, white, black,(skill_tree_eco_path_2_position[0] - 12, skill_tree_eco_path_2_position[1] - 10))

        # skill tree eco path 3
        skill_tree_eco_path_3_position = skill_tree_unlock_position[0] + 100, skill_tree_unlock_position[1] + 240
        draw_text_with_outline(screen, "E3", font_font, white, black,(skill_tree_eco_path_3_position[0] - 12, skill_tree_eco_path_3_position[1] - 10))

        # skill tree eco path 4
        skill_tree_eco_path_4_position = skill_tree_unlock_position[0] + 100, skill_tree_unlock_position[1] + 310
        draw_text_with_outline(screen, "E4", font_font, white, black,(skill_tree_eco_path_4_position[0] - 12, skill_tree_eco_path_4_position[1] - 10))

        # skill tree eco path 5
        skill_tree_eco_path_5_position = skill_tree_unlock_position[0] + 100, skill_tree_unlock_position[1] + 380
        draw_text_with_outline(screen, "E5", font_font, white, black,(skill_tree_eco_path_5_position[0] - 12, skill_tree_eco_path_5_position[1] - 10))

        # draw prog path squares
        pygame.draw.rect(screen, skill_tree_prog_path_1_color, skill_tree_prog_path_1, border_radius=15)
        pygame.draw.rect(screen, skill_tree_prog_path_2_color, skill_tree_prog_path_2, border_radius=15)
        pygame.draw.rect(screen, skill_tree_prog_path_3_color, skill_tree_prog_path_3, border_radius=15)
        pygame.draw.rect(screen, skill_tree_prog_path_4_color, skill_tree_prog_path_4, border_radius=15)
        pygame.draw.rect(screen, skill_tree_prog_path_5_color, skill_tree_prog_path_5, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_prog_path_1,width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_prog_path_2,width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_prog_path_3,width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_prog_path_4,width=6, border_radius=15)
        pygame.draw.rect(screen, black, skill_tree_prog_path_5,width=6, border_radius=15)

        # skill tree prog path 1
        skill_tree_prog_path_1_position = skill_tree_unlock_position[0] - 100, skill_tree_unlock_position[1] + 100
        draw_text_with_outline(screen, "P1", font_font, white, black,(skill_tree_prog_path_1_position[0] - 12, skill_tree_prog_path_1_position[1] - 10))

        # skill tree prog path 2
        skill_tree_prog_path_2_position = skill_tree_unlock_position[0] - 100, skill_tree_unlock_position[1] + 170
        draw_text_with_outline(screen, "P2", font_font, white, black,(skill_tree_prog_path_2_position[0] - 12, skill_tree_prog_path_2_position[1] - 10))

        # skill tree prog path 3
        skill_tree_prog_path_3_position = skill_tree_unlock_position[0] - 100, skill_tree_unlock_position[1] + 240
        draw_text_with_outline(screen, "P3", font_font, white, black,(skill_tree_prog_path_3_position[0] - 12, skill_tree_prog_path_3_position[1] - 10))

        # skill tree prog path 4
        skill_tree_prog_path_4_position = skill_tree_unlock_position[0] - 100, skill_tree_unlock_position[1] + 310
        draw_text_with_outline(screen, "P4", font_font, white, black,(skill_tree_prog_path_4_position[0] - 12, skill_tree_prog_path_4_position[1] - 10))

        # skill tree prog path 5
        skill_tree_prog_path_5_position = skill_tree_unlock_position[0] - 100, skill_tree_unlock_position[1] + 380
        draw_text_with_outline(screen, "P5", font_font, white, black,(skill_tree_prog_path_5_position[0] - 12, skill_tree_prog_path_5_position[1] - 10))

        # display the things
        if skill_tree_unlock.collidepoint(mouse_pos):
            skill_tree_unlock_display = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_unlock_display, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_unlock_display, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Unlock", font_font, white, black,(mouse_pos[0] + 55, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "Unlocks the Skill tree", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_unlock_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_dmg_path_1.collidepoint(mouse_pos):
            skill_tree_display_dmg_1 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_dmg_1, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_dmg_1, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Brutal Clicks", font_font, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "+10 % DPC", font_font, white, black,(mouse_pos[0] + 35, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_dmg_path_1_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_dmg_path_2.collidepoint(mouse_pos):
            skill_tree_display_dmg_2 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_dmg_2, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_dmg_2, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Burning Core", font_font, white, black,(mouse_pos[0] + 25, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "+15 % DPS", font_font, white, black,(mouse_pos[0] + 35, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_dmg_path_2_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_dmg_path_3.collidepoint(mouse_pos):
            skill_tree_display_dmg_3 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_dmg_3, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_dmg_3, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Unlock Crits", font_font, white, black,(mouse_pos[0] + 35, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "+10% to crit (2x dmg)", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_dmg_path_3_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_dmg_path_4.collidepoint(mouse_pos):
            skill_tree_display_dmg_4 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_dmg_4, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_dmg_4, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Unlock Combo", font_font, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "Every hit", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 40))
            draw_text_with_outline(screen, "gives +0.001x dmg", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 55))
            draw_text_with_outline(screen, f"{skill_tree_dmg_path_4_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_dmg_path_5.collidepoint(mouse_pos):
            skill_tree_display_dmg_5 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_dmg_5, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_dmg_5, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Executioner", font_font, white, black,(mouse_pos[0] + 35, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "under 30% hp", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 40))
            draw_text_with_outline(screen, "gives 1.5x damage", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 55))
            draw_text_with_outline(screen, f"{skill_tree_dmg_path_5_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_prog_path_1.collidepoint(mouse_pos):
            skill_tree_display_prog_1 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_prog_1, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_prog_1, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Auto click", font_font, white, black,(mouse_pos[0] + 40, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "Unlocks Auto click", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_prog_path_1_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_prog_path_2.collidepoint(mouse_pos):
            skill_tree_display_prog_2 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_prog_2, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_prog_2, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Auto click Speed", font_font, white, black,(mouse_pos[0] + 8, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "Divide the auto", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 40))
            draw_text_with_outline(screen, "click speed by 2", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 55))
            draw_text_with_outline(screen, f"{skill_tree_prog_path_2_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_prog_path_3.collidepoint(mouse_pos):
            skill_tree_display_prog_3 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_prog_3, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_prog_3, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Auto click Dmg", font_font, white, black,(mouse_pos[0] + 15, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "+20 % Auto Click", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 40))
            draw_text_with_outline(screen, "Damage", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 55))
            draw_text_with_outline(screen, f"{skill_tree_prog_path_3_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_prog_path_4.collidepoint(mouse_pos):
            skill_tree_display_prog_4 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_prog_4, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_prog_4, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Auto Next", font_font, white, black,(mouse_pos[0] + 40, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "Unlocks Auto Next", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_prog_path_4_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_prog_path_5.collidepoint(mouse_pos):
            skill_tree_display_prog_5 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_prog_5, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_prog_5, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Event", font_font, white, black,(mouse_pos[0] + 60, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "Every 30s u get", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 40))
            draw_text_with_outline(screen, "either 2x dmg or", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 55))
            draw_text_with_outline(screen, "-50% auto click speed", font_font_smaller, white, black,(mouse_pos[0] + 20, mouse_pos[1] + 70))
            draw_text_with_outline(screen, f"{skill_tree_prog_path_5_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_eco_path_1.collidepoint(mouse_pos):
            skill_tree_display_eco_1 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_eco_1, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_eco_1, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Golden Touch", font_font, white, black,(mouse_pos[0] + 25, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "+10% money mult", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_eco_path_1_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_eco_path_2.collidepoint(mouse_pos):
            skill_tree_display_eco_2 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_eco_2, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_eco_2, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Market", font_font, white, black,(mouse_pos[0] + 55, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "-10% upg cost", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_eco_path_2_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_eco_path_3.collidepoint(mouse_pos):
            skill_tree_display_eco_3 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_eco_3, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_eco_3, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Bounty", font_font, white, black,(mouse_pos[0] + 55, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "Chance for 2x gold", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_eco_path_3_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_eco_path_4.collidepoint(mouse_pos):
            skill_tree_display_eco_4 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_eco_4, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_eco_4, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Gold Click", font_font, white, black,(mouse_pos[0] + 40, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "Every click gives", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 40))
            draw_text_with_outline(screen, "1% of the gold gain", font_font_smaller, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 55))
            draw_text_with_outline(screen, f"{skill_tree_eco_path_4_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))

        if skill_tree_eco_path_5.collidepoint(mouse_pos):
            skill_tree_display_eco_5 = pygame.Rect(mouse_pos[0],mouse_pos[1], skill_tree_display[0], skill_tree_display[1])
            pygame.draw.rect(screen, brown, skill_tree_display_eco_5, border_radius=15)
            pygame.draw.rect(screen, black, skill_tree_display_eco_5, width=6, border_radius=15)

            # text
            draw_text_with_outline(screen, "Greed Engine", font_font, white, black,(mouse_pos[0] + 30, mouse_pos[1] + 10))
            draw_text_with_outline(screen, "1% more gold every wave", font_font_smaller, white, black,(mouse_pos[0] + 5, mouse_pos[1] + 40))
            draw_text_with_outline(screen, f"{skill_tree_eco_path_5_cost}", font_font, white, black,(mouse_pos[0] + 80, mouse_pos[1] + 90))
    elif gui == 5:
        save_game()
        sys.exit()

    # text draw
    # health
    draw_text_with_outline(screen, f"Health: {notation(health)} / {notation(max_health)}", font_font_bigger, red, black,((int(width / 1.7)) - 50, int(height / 2.1) + 60))

    # gold
    gold_text_position = (int(width / 7) - 50, int(height / 20) - 12)
    draw_text_with_outline(screen, f"Gold: {notation(gold)}", font_font_bigger, (255, 255, 255), (0, 0, 0),(gold_text_position[0], gold_text_position[1]))
    draw_text_with_outline(screen, "🪙", font_emoji, (255, 255, 255), (0, 0, 0),(gold_text_position[0] - 110, gold_text_position[1] - 30))

    # next
    next_positon = (int(width / 1.54), int(height / 10))
    draw_text_with_outline(screen, "Next", font_font, (255, 255, 255), (0, 0, 0), (next_positon[0], next_positon[1]))

    # back
    back_position = (int(width / 1.755), int(height / 10))
    draw_text_with_outline(screen, "Back", font_font, (255, 255, 255), (0, 0, 0), (back_position[0], back_position[1]))

    # wave
    wave_position = (gold_text_position[0] + 576, gold_text_position[1])
    draw_text_with_outline(screen, f"Wave: {wave}", font_font_bigger, (255, 255, 255), (0, 0, 0),(wave_position[0], wave_position[1]))

    # enemies
    enemies_position = ((int(width / 1.75)) - 7, int(height / 5))
    draw_text_with_outline(screen, f"Enemies: {enemies_had} / {enemies_need}", font_font, (255, 255, 255), (0, 0, 0),(enemies_position[0], enemies_position[1]))

    # DPS
    DPS_position = (int(width / 1.15) - 50, int(height / 6) + 150)
    draw_text_with_outline(screen, f"DPS: {notation(DPS_overall)}", font_font_bigger, (255, 255, 255), (0, 0, 0),(DPS_position[0], DPS_position[1]))

    # DPC
    DPC_position = (int(width / 1.15) - 50, int(height / 6) + 185)
    draw_text_with_outline(screen,f"DPC: {notation(DPC_overall)}",font_font_bigger, (255, 255, 255), (0, 0, 0), (DPC_position[0], DPC_position[1]))

    # Gold Gain
    Gold_Gain_position = (int(width / 1.15) - 50, int(height / 6) + 220)
    draw_text_with_outline(screen,f"Gain: {notation(money_overall)}",font_font_bigger, (255, 255, 255), (0, 0, 0), (Gold_Gain_position[0], Gold_Gain_position[1]))

    # prestige tokens
    prestige_tokens_position = (int(width / 2.5) - 50, int(height / 1.3))
    draw_text_with_outline(screen,f"Prestige tokens: {notation(prestige_tokens)}",font_font_bigger, (255, 255, 255), (0, 0, 0), (prestige_tokens_position[0], prestige_tokens_position[1]))


    # draw squares
    pygame.draw.rect(screen, (50, 150, 100), clicker)

    pygame.draw.rect(screen, (255, 0, 0), button_next)
    pygame.draw.rect(screen, (255, 0, 0), button_back)

    pygame.draw.rect(screen, red, button_auto_next,border_radius=15)
    pygame.draw.rect(screen, black, button_auto_next,width=6,border_radius=15)
    pygame.draw.rect(screen, red, button_auto_click,border_radius=15)
    pygame.draw.rect(screen, black, button_auto_click,width=6,border_radius=15)

    pygame.draw.rect(screen,red,button_gui_1, border_radius=20)
    pygame.draw.rect(screen,red,button_gui_2, border_radius=20)
    pygame.draw.rect(screen,red,button_gui_3, border_radius=20)
    pygame.draw.rect(screen,red,button_gui_4, border_radius=20)
    pygame.draw.rect(screen,red,button_gui_5, border_radius=20)
    pygame.draw.rect(screen, black, button_gui_1, width=6, border_radius=20)
    pygame.draw.rect(screen, black, button_gui_2, width=6, border_radius=20)
    pygame.draw.rect(screen, black, button_gui_3, width=6, border_radius=20)
    pygame.draw.rect(screen, black, button_gui_4, width=6, border_radius=20)
    pygame.draw.rect(screen, black, button_gui_5, width=6, border_radius=20)

    pygame.draw.rect(screen,red,button_save, border_radius=15)
    pygame.draw.rect(screen,black,button_save,width=6, border_radius=15)

    # image draw
    screen.blit(scaled_image, image)

    # emojis
    draw_text_with_outline(screen, "⬅️", font_emoji_medium, (255, 255, 255), (0, 0, 0), (back_position[0] - 12, back_position[1] + 31))
    draw_text_with_outline(screen, "➡️", font_emoji_medium, (255, 255, 255), (0, 0, 0), (next_positon[0] - 12, next_positon[1] + 31))

    # gui 1
    button_gui_1_text = (int(width / 12) - 65, int(height / 1.07) - 35)
    draw_text_with_outline(screen, "Improvements", font_font_bigger, (255, 255, 255), (0, 0, 0),(button_gui_1_text[0], button_gui_1_text[1]))

    # gui 2
    button_gui_2_text = (int(width / 12) - 65, int(height / 1.07) - 35)
    draw_text_with_outline(screen, "Upgrades", font_font_bigger, (255, 255, 255), (0, 0, 0),(button_gui_2_text[0] + 265, button_gui_2_text[1]))

    # gui 3
    button_gui_3_text = (int(width / 12) - 65, int(height / 1.07) - 35)
    draw_text_with_outline(screen, "Prestige", font_font_bigger, (255, 255, 255), (0, 0, 0),(button_gui_3_text[0] + 530, button_gui_3_text[1]))

    # gui 4
    button_gui_4_text = (int(width / 12) - 85, int(height / 1.07) - 35)
    draw_text_with_outline(screen, "Skill Tree", font_font_bigger, (255, 255, 255), (0, 0, 0),(button_gui_4_text[0] + 795, button_gui_4_text[1]))

    # gui 5
    button_gui_5_text = (int(width / 12) - 45, int(height / 1.07) - 35)
    draw_text_with_outline(screen, "Exit", font_font_bigger, (255, 255, 255), (0, 0, 0),(button_gui_5_text[0] + 1045, button_gui_5_text[1]))

    # save
    button_save_text = int(width / 1.15) - 32, int(height / 20) - 10
    draw_text_with_outline(screen, "SAVE", font_font_medium, (255, 255, 255), (0, 0, 0),(button_save_text[0], button_save_text[1]))

    # auto next
    auto_next_position = (int(width / 1.15) - 20, int(height / 6) - 10)
    if skill_tree_prog_path_4_limit_had >= skill_tree_prog_path_4_limit:
        if auto_next_is:
            draw_text_with_outline(screen, "ON", font_font, (255, 255, 255), (0, 0, 0),(auto_next_position[0], auto_next_position[1]))
        else:
            draw_text_with_outline(screen, "OFF", font_font, (255, 255, 255), (0, 0, 0),(auto_next_position[0], auto_next_position[1]))
    else:
        draw_text_with_outline(screen, "🔒", font_emoji_small, (255, 255, 255), (0, 0, 0),(auto_next_position[0], auto_next_position[1] - 8))
    draw_text_with_outline(screen, "Auto Next", font_font, white, black, (auto_next_position[0] - 25, auto_next_position[1] - 40))

    # auto click
    auto_click_position = (int(width / 1.15) - 20, int(height / 3.5) - 10)
    if skill_tree_prog_path_1_limit_had >= skill_tree_prog_path_1_limit:
        if auto_click_is:
            draw_text_with_outline(screen, "ON", font_font, (255, 255, 255), (0, 0, 0),(auto_click_position[0], auto_click_position[1]))
        else:
            draw_text_with_outline(screen, "OFF", font_font, (255, 255, 255), (0, 0, 0),(auto_click_position[0], auto_click_position[1]))
    else:
        draw_text_with_outline(screen, "🔒", font_emoji_small, (255, 255, 255), (0, 0, 0),(auto_click_position[0], auto_click_position[1] - 8))
    draw_text_with_outline(screen, "Auto Click", font_font, white, black, (auto_click_position[0] - 25, auto_click_position[1] - 40))

    for text in damage_popup[:]:
        text[1] -= 60 * delta_time
        text[3] -= delta_time

        draw_text_with_outline(screen, str(text[2]), font_font, (255, 255, 255), (0, 0, 0),(text[0], text[1]))
        if text[3] <= 0:
            damage_popup.remove(text)

    pygame.display.flip()

pygame.quit()