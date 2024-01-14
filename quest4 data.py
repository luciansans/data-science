# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:13:32 2023

@author: Lucian
"""

# a. Probability of drawing a face card
total_cards = 52
face_cards = 3
pattern = 4
face_cards_total = face_cards * pattern
probability_face_card = face_cards_total / total_cards
print(f"a. Probability of drawing a face card: {probability_face_card:.4f}")

# b. Probability of getting a '9' of red color
nines_per_pattern = 1
red_pattern = 2
nines_total = nines_per_pattern * red_pattern
probability_9_red = nines_total / total_cards
print(f"b. Probability of getting a '9' of red color: {probability_9_red:.4f}")

# c. Probability that both cards are red without replacement
probability_first_red = red_pattern / total_cards
probability_second_red_given_first_red = (red_pattern - 1) / (total_cards - 1)
probability_both_red = probability_first_red * probability_second_red_given_first_red
print(f"c. Probability that both cards are red: {probability_both_red:.4f}")

# d. Probability of neither an ace nor a king of red color
aces_kings_per_pattern = 2
aces_kings_total = aces_kings_per_pattern * red_pattern
probability_ace_king_red = aces_kings_total / total_cards
probability_neither_ace_nor_king_red = 1 - probability_ace_king_red
print(f"d. Probability of neither an ace nor a king of red color: {probability_neither_ace_nor_king_red:.4f}")
