# Pygame Installer

## Descrição

Este script Python instala automaticamente o Pygame em um diretório específico (`Libs`) ao iniciar o script. Isso é útil quando você deseja garantir que o Pygame esteja disponível para o seu projeto sem precisar instalá-lo manualmente.

## Uso

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Execute o script:**

   ```bash
   python install_pygame.py
   ```

3. **Importe o Pygame em seu projeto:**

   ```python
   import pygame
   ```

## Como Funciona

O script verifica se o Pygame já está instalado no diretório `Libs`. Se não estiver, ele usa o `pip` para instalar o Pygame no diretório especificado. Em seguida, o diretório `Libs` é adicionado ao `sys.path` para que o Python possa encontrar e importar o Pygame.

## Requisitos

- Python 3.x
- Conexão com a Internet (para baixar o Pygame)

## Estrutura do Projeto

```
seu-repositorio/
├── install_pygame.py
├── Libs/
└── README.md
```

## Autor

- **Nome:** proxlu
- **Data:** Oct 30, 2024

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
