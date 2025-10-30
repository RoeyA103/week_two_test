from random import randint

cards_rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
cards_suite =['S','H','C','D']
shuffle_Conditions = {'H':5,'C':3,'D':2,'S':7}

def create_card(rank:str, suite:str) -> dict:
    card = {'rank':rank,'suit':suite}
    return card

def build_standard() -> list[dict]:
    deck = []
    for rank in cards_rank:
        for suite in cards_suite:
            deck.append(create_card(rank,suite))

    return deck

def shuffle_by_suit(deck:list[dict],swaps:int=5000) -> list[dict]:
    for _ in range(swaps):
        while True:
            index1 , index2 = randint(0,51) , randint(0,51)
            index1s = deck[index1]['suit']
            shuffle_Condition = shuffle_Conditions[index1s]
            if index1 == index2:
                continue
            elif index2 % shuffle_Condition != 0:
                continue
            break
        deck[index1] , deck[index2] = deck[index2] , deck[index1]

    return deck


