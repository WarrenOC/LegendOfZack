import pygame
import socket
import pickle

class GameManager:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 400, 300
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # Player setup
        self.player = {"x": 50, "y": 50, "speed": 2}

        # Multiplayer setup
        self.multiplayer = False
        self.client = None

    def connect_to_server(self, ip="127.0.0.1", port=5555):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((ip, port))
            self.multiplayer = True
            print("Connected to server!")
        except:
            print("Failed to connect. Playing offline.")

    def disconnect_from_server(self):
        if self.client:
            self.client.close()
        self.client = None
        self.multiplayer = False
        print("Disconnected from server.")

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.player["x"] -= self.player["speed"]
        if keys[pygame.K_RIGHT]: self.player["x"] += self.player["speed"]
        if keys[pygame.K_UP]: self.player["y"] -= self.player["speed"]
        if keys[pygame.K_DOWN]: self.player["y"] += self.player["speed"]

    def update_multiplayer(self):
        if not self.multiplayer:
            return

        try:
            self.client.sendall(pickle.dumps(self.player))
            data = self.client.recv(1024)
            players = pickle.loads(data)
            for p in players.values():
                pygame.draw.rect(self.screen, (0, 255, 0), (p["x"], p["y"], 20, 20))
        except:
            print("Lost connection to server.")
            self.disconnect_from_server()

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()
            pygame.draw.rect(self.screen, (0, 0, 255), (self.player["x"], self.player["y"], 20, 20))
            self.update_multiplayer()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()


# 🛠 Prevent the script from running automatically when imported
if __name__ == "__main__":
    game = GameManager()
    game.run()
