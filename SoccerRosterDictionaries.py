def get_roster():
    roster = {}
    for i in range(1, 6):
        jersey_num = int(input(f"Enter player {i}'s jersey number:\n"))
        rating = int(input(f"Enter player {i}'s rating:\n"))
        print()
        roster[jersey_num] = rating
    return sort_roster(roster)

def sort_roster(roster):
    roster = {k: v for k, v in sorted(roster.items())}
    return roster

def print_roster(roster):
    print("ROSTER")
    for jersey, rating in roster.items():
        print(f"Jersey number: {jersey}, Rating: {rating}")
    print()


def print_menu():
    print("MENU")
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - quit')
    print()


def user_choice(roster):
    options = ['a', 'd', 'u', 'r', 'o', 'q']
    choice = input('Choose an option:\n')

    while choice != 'q':
        if choice not in options:
            choice = input('Choose an option:\n')
            continue
        execute_menu(choice, roster)
        print_menu()
        choice = input('Choose an option:\n')


def add_player(roster):
    jersey_num = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    roster[jersey_num] = rating

def remove_player(roster):
    jersey_num = int(input("Enter a jersey number:\n"))
    del roster[jersey_num]


def update_player(roster):
    jersey_num = int(input("Enter a jersey number:\n"))
    new_rating = int(input("Enter a new rating for player:\n"))
    roster[jersey_num] = new_rating

def output_above(roster):
    check_val = int(input("Enter a rating:\n"))
    print(f"ABOVE {check_val}")
    for jersey, rating in roster.items():
        if rating > check_val:
            print(f'Jersey number: {jersey}, Rating: {rating}')
def execute_menu(choice, roster):
    match choice:
        case 'a':
            add_player(roster)
        case 'd':
            remove_player(roster)
        case'u':
            update_player(roster)
        case'r':
            output_above(roster)
        case 'o':
            print_roster(team)


team = get_roster()

print_menu()
user_choice(team)
