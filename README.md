Cada aluno deve criar sua própria .venv

Essa parte é importante. A .venv não vem do GitHub. Cada aluno cria a sua.

Windows:

python -m venv .venv

Ativa:

.\.venv\Scripts\Activate.ps1

E instala:

python -m pip install -r requirements.txt

Ubuntu/Linux:

python3 -m venv .venv

Ativa:

source .venv/bin/activate

E instala:

python3 -m pip install -r requirements.txt

