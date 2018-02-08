# NOTE: Change "written" to the name of your TeX file with no extension
#
# #https://reu.dimacs.rutgers.edu/Symbols.pdf 
TARGET= rsa_alg mathscr

all: $(patsubst %, %.pdf, $(TARGET))

## Generalized rule: how to build a .pdf from each .tex
LATEXPDFS=$(patsubst %.tex,%.pdf,$(wildcard *.tex))
$(LATEXPDFS): %.pdf: %.tex
	xelatex rsa_alg.tex
	bibtex rsa_alg.aux
	xelatex rsa_alg.tex
	xelatex rsa_alg.tex

clean:
	rm *.aux *.log *.pdf *.toc || true

veryclean: clean
	rm $(TARGET).pdf

view: $(TARGET).pdf
	if [ "Darwin" = "$(shell uname)" ]; then open $(TARGET).pdf ; else evince $(TARGET).pdf ; fi

submit: $(TARGET).pdf
	cp $(TARGET).pdf ../

print: $(TARGET).pdf
	lpr $(TARGET).pdf

.PHONY: all clean veryclean view print
