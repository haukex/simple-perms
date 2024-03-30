
.PHONY: all installdeps clean

all: output/markdown/index.md

# Regarding "WARNING: unknown node type: desc_returns", see:
# https://github.com/liran-funaro/sphinx-markdown-builder/issues/19
output/markdown/index.md: index.rst ../simple_perms/__init__.py
	PYTHONPATH=..:_ext sphinx-build -M markdown . output

installdeps:
	python -m pip install --upgrade --upgrade-strategy=eager --no-warn-script-location -r requirements.txt

clean:
	rm -rf output
