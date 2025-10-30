from core import game_logic , deck
def ask_player_action() -> str:
    while True:
        Player_answer = input("chose\n'h' to hit\n's' stand\n:").upper()
        print(Player_answer)
        if Player_answer != 'S' and Player_answer != 'H':
            print('not valid!!')
            continue
        break
    return Player_answer    

def print_player_hand(player:dict) -> None:
    print(f"hand: {player['hand']}")
    print(f"total value: {game_logic.calculate_hand_value(player['hand'])}")

def print_game_summary(player: dict, dealer: dict):
    print("game summary")
    print("-----------------------------\n")
    print(f"player hand:")
    print_player_hand(player)
    print("-----------------------------\n")
    print(f"dealer hand:")
    print_player_hand(dealer)

