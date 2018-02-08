# NOTE: Change "written" to the name of your TeX file with no extension
#
# #https://reu.dimacs.rutgers.edu/Symbols.pdf 
TARGET=helloworld theorems theorems1 theorems2 theorems3


# bibtex_7
#生成 bibliography 的例子见 脚本  bibliography.sh

all: $(patsubst %, %.pdf, $(TARGET))

## Generalized rule: how to build a .pdf from each .tex
LATEXPDFS=$(patsubst %.tex,%.pdf,$(wildcard *.tex))
$(LATEXPDFS): %.pdf: %.tex
	xelatex $(patsubst %.pdf,%.tex,$@)

clean:
	rm *.aux *.log *.pdf *.toc *.nav *.snm *.def *.out *.lof *.lot *.bbl *.blg *blx.bib  *.xml -f || true

veryclean: clean
	rm $(TARGET).pdf

view: $(TARGET).pdf
	if [ "Darwin" = "$(shell uname)" ]; then open $(TARGET).pdf ; else evince $(TARGET).pdf ; fi

submit: $(TARGET).pdf
	cp $(TARGET).pdf ../

print: $(TARGET).pdf
	lpr $(TARGET).pdf

.PHONY: all clean veryclean view print
