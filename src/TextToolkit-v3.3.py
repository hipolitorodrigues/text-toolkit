"""
    Desenvolvedor: Hipolito Rodrigues
    Email: hipolitorodrigues@gmail.com
    Data de criação: 09/11/2024
    Última atualização: 16/01/2025
    Nome da aplicacação: Text Toolkit
    Versão: 3.3
    Tecnologias Utilizadas: Python 3.13.1 + Tkinter
    Descrição: Aplicação para converter textos em diferentes formatos de capitalização:
    - MAIÚSCULO
    - minúsculo
    - Primeira letra das frases
    - Primeira Letra Das Palavras
    - Contador de palavras (ainda não adicionado)
    - Contador de caracteres (ainda não adicionado)
    - Gerador de Lorem Ipsum (ainda não adicionado)
    - Corretor ortográfico (ainda não adicionado)
"""
import os

import tkinter as tk
from tkinter import ttk

class TextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Toolkit v3.3")
        self.root.geometry("800x275")
        self.root.resizable(False, False)
        
        # Configuração de estilo
        self.root.configure(bg='#e0e6ed')  # Fundo mais suave
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal com cor de fundo e padding mais moderno
        main_frame = tk.Frame(self.root, bg='#e0e6ed', padx=15, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Área de texto com borda arredondada simulada, e cores atualizadas
        self.text_area = tk.Text(
            main_frame,
            width=87,  # 87 caracteres
            height=10, # 10 linhas
            wrap=tk.WORD,
            font=('Arial', 11),
            relief='flat',
            borderwidth=1,
            bg='#ffffff',  # Fundo branco para contraste
            highlightbackground='#c0c7d1',  # Borda arredondada simulada
            highlightthickness=2  # Espessura da borda
        )
        self.text_area.pack(pady=(0, 15))
        
        # Frame para centralizar os botões com novo estilo de fundo
        center_frame = tk.Frame(main_frame, bg='#e0e6ed')
        center_frame.pack(fill=tk.X)
        
        # Frame para os botões (dentro do frame central)
        button_frame = tk.Frame(center_frame, bg='#e0e6ed')
        button_frame.pack(expand=True)
        
        # Configuração dos botões com novo estilo moderno
        buttons = [
            ("MAIÚSCULO", self.to_uppercase),
            ("minúsculo", self.to_lowercase),
            ("Primeiras letras - frases", self.to_sentence_case),
            ("Primeiras Letras - Palavras", self.to_proper_case)
        ]
        
        for text, command in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                width=20,
                relief='flat',  # Remove bordas
                font=('Arial', 10, 'bold'),  # Texto em negrito para modernizar
                bg='#4a90e2',  # Cor moderna de fundo
                fg='#ffffff',  # Texto branco para contraste
                activebackground='#357abd',  # Cor de fundo ao clicar
                activeforeground='#ffffff',  # Texto branco ao clicar
                padx=10, pady=5,  # Espaçamento interno
                borderwidth=0  # Remove borda para dar uma aparência mais limpa
            )
            btn.pack(side=tk.LEFT, padx=5, pady=10)  # Espaçamento entre os botões
    
    def get_text(self):
        """Obtém o texto da área de texto."""
        return self.text_area.get("1.0", tk.END).strip()
    
    def set_text(self, text):
        """Define o texto na área de texto."""
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", text)
    
    def to_uppercase(self):
        """Converte o texto para maiúsculo."""
        text = self.get_text()
        self.set_text(text.upper())
    
    def to_lowercase(self):
        """Converte o texto para minúsculo."""
        text = self.get_text()
        self.set_text(text.lower())
    
    def to_sentence_case(self):
        """Converte primeira letra de cada frase para maiúscula."""
        text = self.get_text()
        sentences = text.lower().split('. ')
        sentences = [s.capitalize() for s in sentences]
        self.set_text('. '.join(sentences))
    
    def to_proper_case(self):
        """Converte primeira letra de cada palavra para maiúscula."""
        text = self.get_text()
        self.set_text(text.title())

def main():
    root = tk.Tk()
    app = TextConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
