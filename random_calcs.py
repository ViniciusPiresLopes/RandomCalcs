import random


class App:
    def __init__(self):
        self.running = False
        self.symbols = "+", "-",
        
        self.x = 0
        self.y = 0
        self.symbol = ""
        self.user_result = 0
        self.result = 0
    
    def sepl(self):
        print("-" * 30)

    def generate(self):
        self.x = random.randint(1, 20)
        self.y = random.randint(1, 20)
        self.symbol = random.choice(self.symbols)
        
        if self.symbol == "+":
            self.result = self.x + self.y
        elif self.symbol == "-":
            self.result = self.x - self.y
        else:
           print("Símbolo não reconhecido!") 
           quit()
    
    def show(self):
        self.sepl()
        
        print(f"{self.x} {self.symbol} {self.y} = ?")
    
    def input(self):
        self.user_result = int(input("Resultado: "))
    
    def logic(self):
        self.sepl()
        
        if self.user_result == self.result:
            print("Você acertou!")
        else:
            print("Você errou!") 
        
        print(f"O resultado era: {self.result}.")

    def run(self):
        self.running = True
        
        while self.running:
            self.generate()
            self.show()
            self.input()
            self.logic()


if __name__ == "__main__":
    app = App()
    app.run()
