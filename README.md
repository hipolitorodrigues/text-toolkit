# Text Toolkit v3.3

**Text Toolkit** é uma aplicação desktop simples e intuitiva, desenvolvida em Python com Tkinter, para manipulação de textos de maneira rápida e eficiente. Este projeto tem como objetivo principal converter textos para diferentes formatos de capitalização, sendo útil para escritores, programadores e estudantes.

![alt text](https://github.com/hipolitorodrigues/text-toolkit/blob/9894f127fd6e586bf979e6ec06b45ac1d2423d6f/assets/images/sampling.png)

## Descrição

O **Text Toolkit** oferece uma interface minimalista e moderna, com botões para realizar conversões de texto diretamente na aplicação. Ainda há funcionalidades planejadas para futuras atualizações, como contadores de palavras e caracteres, e um corretor ortográfico.

### Funcionalidades Atuais

- **MAIÚSCULO**: Converte todo o texto para letras maiúsculas.
- **minúsculo**: Converte todo o texto para letras minúsculas.
- **Primeiras letras - frases**: Converte a primeira letra de cada frase para maiúscula.
- **Primeiras Letras - Palavras**: Converte a primeira letra de cada palavra para maiúscula.

### Funcionalidades Planejadas

- Contador de palavras.
- Contador de caracteres.
- Gerador de Lorem Ipsum.
- Corretor ortográfico.

## Tecnologias Utilizadas

- **Python 3.13.1**: Lógica e backend.
- **Tkinter**: Interface gráfica simples e responsiva.

## Pré-requisitos

Certifique-se de ter o Python instalado na versão **3.6 ou superior**.  
Você pode baixar o Python em: [https://www.python.org/](https://www.python.org/).

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/text-toolkit.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd text-toolkit/src
   ```

3. Execute o script Python:
   ```bash
   python TextToolkit-v3.3.py
   ```

4. A aplicação será aberta em uma janela gráfica.

- Uma versão .exe (Portátil) encontra-se em dist/TextToolkit-v3.3.exe

## Estrutura do Projeto

```plaintext
text-toolkit/
├── TextToolkit-v3.3.py    # Arquivo principal da aplicação
```

## Como Usar

1. Insira ou cole o texto desejado na área de texto.
2. Clique em um dos botões para aplicar o formato desejado.
3. O texto formatado será exibido na área de texto.

## Exemplos

### Entrada
```
isto É UM Exemplo. outro exemplo.
```

### Saída com "Primeiras letras - frases"
```
Isto é um exemplo. Outro exemplo.
```

### Saída com "Primeiras Letras - Palavras"
```
Isto É Um Exemplo. Outro Exemplo.
```

## Autor

- **Desenvolvedor**: Hipolito Rodrigues
- **Data de Criação**: 09/11/2024
- **Última Atualização**: 16/01/2025
- **Versão Atual**: 3.3  

---

## Licença

Este projeto está sob a licença [CC0 1.0 Universal (Domínio Público)](https://creativecommons.org/publicdomain/zero/1.0/). Isso significa que você pode copiar, modificar, distribuir e executar o trabalho, mesmo para fins comerciais, tudo sem pedir permissão.
