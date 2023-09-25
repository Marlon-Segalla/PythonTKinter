import tkinter as tk
from tkinter import font, messagebox

class JogoVelhaOO(tk.Frame):
    def __init__(self):
        super().__init__()
        self.ultimaJogada = "O"
        self.desenharTela()

    def desenharTela(self):
        self.master.title("Jogo da Velha OO")
        self.master.geometry("600x620")
        formato = 70

        self.teclaVet = []
        for i in range(1, 10):
            button = tk.Button(self.master, text="", border=1, relief=tk.RAISED, padx=20, pady=20,
                               command=lambda i=i: self.processarBotao(self.teclaVet[i - 1]))
            self.teclaVet.append(button)

        indice = 0
        for i in range(3):
            for j in range(3):
                self.teclaVet[indice].grid(row=i, column=j, ipadx=formato, ipady=formato)
                indice += 1

    def processarBotao(self, btnCli):
        myFont = font.Font(size=15, weight="bold")
        texto = btnCli['text']
        if texto == "":
            btnCli.configure(text=self.ultimaJogada, bg='#0052cc' if self.ultimaJogada == "O" else '#222222', fg='#ffffff')
            btnCli['font'] = myFont
            btnCli["state"] = "disabled"
            self.ultimaJogada = "X" if self.ultimaJogada == "O" else "O"
            vencedor = self.validarVencedor()
            if vencedor:
                messagebox.showinfo("Jogo da Velha", f"O jogador {vencedor} venceu!")
                self.reiniciarJogo()

    def validarVencedor(self):
        # Lógica para verificar o vencedor nas linhas, colunas e diagonais
        tabuleiro = [btn['text'] for btn in self.teclaVet]
        sequencias = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for seq in sequencias:
            if tabuleiro[seq[0]] == tabuleiro[seq[1]] == tabuleiro[seq[2]] != "":
                return tabuleiro[seq[0]]
        return None

    def reiniciarJogo(self):
        for btn in self.teclaVet:
            btn.configure(text="", state="normal")

if __name__ == "__main__":
    obj = JogoVelhaOO()
    obj.mainloop()