from game_manager import GameManager

if __name__ == "__main__":
    game = GameManager()

    # Uncomment this if you want to test multiplayer:
    game.connect_to_server("127.0.0.1", 5555)

    game.run()
