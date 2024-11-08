# Variabili per i percorsi
SPHINXBUILD = sphinx-build
SPHINXAPIDOC = sphinx-apidoc
SOURCEDIR = docs/source
BUILDDIR = docs/build

# Mostra l'elenco dei comandi disponibili e le loro descrizioni
help:
	@echo "Comandi disponibili:"
	@echo ""
	@echo "  make help           - Mostra questo elenco di comandi e le loro descrizioni."
	@echo "  make init           - Inizializza il progetto: crea l'ambiente virtuale e installa le dipendenze."
	@echo "  make activate       - Mostra il comando per attivare l'ambiente virtuale."
	@echo "  make deactivate     - Mostra il comando per disattivare l'ambiente virtuale."
	@echo "  make update-reqs    - Aggiorna il file requirements.txt con le librerie attualmente installate."
	@echo "  make clean          - Rimuove file temporanei, cache e build di Sphinx (soft clean)."
	@echo "  make clean-forced   - Rimuove tutto, incluso l'ambiente virtuale (hard clean)."
	@echo "  make test           - Esegue i test definiti nella directory tests/ usando pytest."
	@echo "  make apidoc         - Genera automaticamente file .rst per la documentazione dei moduli Python."
	@echo "  make docs           - Genera la documentazione in formato HTML nella directory docs/build/html."
	@echo "  make open-docs      - Apre la documentazione HTML generata nel browser (solo su macOS)."
	@echo "  make run            - Esegue il file principale src/main.py."
	@echo ""

# Inizializza l'ambiente virtuale e installa dipendenze
init:
	python3 -m venv .venv
	source .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Attiva l'ambiente virtuale
activate:
	@echo "source .venv/bin/activate"

# Disattiva l'ambiente virtuale
deactivate:
	@echo "Per disattivare l'ambiente, esegui 'deactivate' (direttamente nel terminale)."

# Esegui i test
test:
	pytest tests/

# Aggiorna il file requirements.txt
update-reqs:
	pip freeze > requirements.txt

# Pulisci file temporanei (soft clean)
clean:
	rm -rf __pycache__ *.pyc *.pyo .ipynb_checkpoints $(BUILDDIR)

# Rimuove tutto, incluso l'ambiente virtuale (hard clean)
clean-forced:
	rm -rf .venv __pycache__ *.pyc *.pyo .ipynb_checkpoints build dist *.egg-info $(BUILDDIR)

# Genera la documentazione API con sphinx-apidoc
apidoc:
	$(SPHINXAPIDOC) -o $(SOURCEDIR) ./src

# Genera documentazione con Sphinx
docs:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html

# Apri la documentazione HTML nel browser
open-docs:
	cd $(BUILDDIR)/html && open index.html

# Esegui l'applicazione principale
run:
	python src/main.py
