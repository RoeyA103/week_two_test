from core import player_io ,deck
# bonus
def add_1_or_11(val) -> int:
    if val + 11 < 22:
        return 11
    return 1


def calculate_hand_value(hand:list[dict]) -> int:
    val = 0
    for card in hand:
        rank = card['rank']
        if not rank.isdigit():
            match rank:
                case 'A':
                    val += add_1_or_11(val)
                case _ :
                    val += 10  
        else:
            val += int(rank)   
    return val         

def deal_two_each(deck:list[dict],player:dict,dealer:dict) -> None:
    for i in range(2):
        card = deck.pop()
        player['hand'].append(card)
        card2 = deck.pop()
        dealer['hand'].append(card2)
    p1hand = calculate_hand_value(player['hand'])    
    dhand = calculate_hand_value(dealer['hand'])
    print(f"player hand : {p1hand} , dealer hand : {dhand}")
        
def dealer_play(deck:list[dict],dealer:dict) -> bool:
    # if the dealer pass the 21 returns false
    while True:
        dhand = calculate_hand_value(dealer['hand'])
        if dhand >= 17 :
            break
        card = deck.pop()
        dealer['hand'].append(card)
    return dhand < 22

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    def inner(deck: list[dict], player: dict, dealer: dict) -> str:
        deal_two_each(deck,player,dealer)
        while True:
            player_io.print_player_hand(player)
            phand = calculate_hand_value(player['hand'])
            if phand > 21:
                break
            player_answer = player_io.ask_player_action()
            if player_answer == 'S':
                break
            card = deck.pop()
            player['hand'].append(card)

        if phand > 21:
            return "dealer"
        if dealer_play(deck,dealer):
            dhand = calculate_hand_value(dealer['hand'])
            if phand > dhand:
                return "player"
            elif phand < dhand:
                return "dealer"
            return "tie"
        else:
            return "player"
        
    resolt = inner(deck,player,dealer)
    player_io.print_game_summary(player,dealer)
    match resolt:
        case "player":
            print("player won!!")
        case "dealer":
            print("dealer won!!!")
        case _ :
            print("its a tie!!!!")      


    
    
        





   



# d1 = deck.build_standard()
# d1 = deck.shuffle_by_suit(d1)
# hand = d1[:4]
# print(hand)
# print(calculate_hand_value(hand))

