import random

def parier_sur_couleur(points):
    mise = int(input("Combien voulez-vous parier ? "))
    couleur = input("Sur quelle couleur voulez-vous parier (r ou n) ? ")

    suits = ['coeur', 'carreau', 'pique', 'trèfle']
    couleur_tiree = random.choice(suits)

    if random.randint(1, 54) > 2:
        if couleur == 'r' and couleur_tiree in ['coeur', 'carreau']:
            points = mise * 2
            print(f"La carte pigee est un {random.randint(1, 13)} de {couleur_tiree} ! Vous avez gagné {points} points.")
            return points
        elif couleur == 'n' and couleur_tiree in ['pique', 'trèfle']:
            points = mise * 2
            print(f"La carte pigee est un {random.randint(1, 13)} de {couleur_tiree} ! Vous avez gagné {points} points.")
            return points
        else:
            points = mise
            print(f"La carte pigee est un {random.randint(1, 13)} de {couleur_tiree}. Vous avez perdu {points} points.")
            return points
    else:
        print(f"Aww, vous avez eu un joker, donc vous avez perdu {points} points.")
        return points
def parier_sur_suite(points):
    mise = float(input("Combien voulez-vous parier ? "))
    suite = input("Sur quelle suite voulez-vous parier (co, ca, pi, tre) ? ")

    suites_cartes = ['co', 'ca', 'pi', 'tre']
    suite_tiree = random.choice(suites_cartes)
    if random.randint(1, 54) > 2:
        if suite == suite_tiree:
            points = mise * 3
            print(f"La carte tiree est {random.randint(1, 13)} {suite_tiree} ! Vous avez gagné : {points} points.")
        else:
            points = mise
            print(f"La carte tiree est {random.randint(1, 13)} {suite_tiree}. Vous avez perdu : {points} points.")
    elif random.randint(1, 54) <= 2:
        points = mise
        print(f" Aw, Vous avez eu un joker! Vous avez perdu : {points} points.")
        return points

def parier_sur_joker(points):
    mise = int(input("Combien voulez-vous parier sur le joker ? "))

    if random.randint(1, 54) <= 2:
        points = (mise * 26)
        print(f"C'est un joker ! Vous avez gagné 26 fois votre mise ! Vous avez gagné {points} points!.")
    else:
        points = mise
        print(f"Vous avez pigez un {random.randint(1, 13)} de {random.choice(['coeur', 'carreaux', 'pique', 'trefles'])}. Vous avez perdu {points} points.")
    return points

points_joueur = 0  # Montant d'points initial

while True:
    print("\nMenu:")
    print("1. Parier sur une couleur")
    print("2. Parier sur une suite")
    print("3. Parier sur un joker")
    print("4. Quitter le jeu")

    choix = input("Choisissez une option : ")

    if choix == '1':
        points_joueur = parier_sur_couleur(points_joueur)
    elif choix == '2':
        points_joueur = parier_sur_suite(points_joueur)
    elif choix == '3':
        points_joueur = parier_sur_joker(points_joueur)
    elif choix == '4':
        break
    else:
        print("Option invalide. Veuillez choisir parmi les options disponibles.")