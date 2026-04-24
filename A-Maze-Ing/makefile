# 1. Variáveis para facilitar a manutenção
NAME        = a_maze_ing.py
PYTHON      = python3
CONFIG      = config.txt
PIP         = $(PYTHON) -m pip

# 2. Phony Targets (diz ao Makefile que estes nomes não são ficheiros)
.PHONY: all install run debug lint clean

# Regra padrão (o que acontece se escreveres apenas 'make')
all: run

# 3. Instalação de dependências
install:
	$(PIP) install --upgrade pip
	$(PIP) install flake8 mypy

# 4. Execução normal
run:
	$(PYTHON) $(NAME) $(CONFIG)

# 5. Debugging com o PDB (Debugger do Python)
debug:
	$(PYTHON) -m pdb $(NAME) $(CONFIG)

# 6. Qualidade de Código (Linting) - REQUISITO DO PDF
# Usamos o backslash (\) para partir o comando em várias linhas e ficar legível
lint:
	flake8 .
	mypy --warn-return-any \
		 --warn-unused-ignores \
		 --ignore-missing-imports \
		 --disallow-untyped-defs \
		 --check-untyped-defs .

# 7. Limpeza de ficheiros temporários
clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
