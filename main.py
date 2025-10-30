from core import deck , game_logic ,player_io


if __name__ == "__main__":
    player = {'hand':[]}
    dealer = {'hand':[]}

    deck1 = deck.build_standard()
    deck1 = deck.shuffle_by_suit(deck1)

    game_logic.run_full_game(deck1,player,dealer)

