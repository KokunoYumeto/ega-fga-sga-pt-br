from audit import *
f='08_expose_viii/components/07_seccion_5.tex'
block(f,15,'% Tradução brasileira revista','\\SGARefTarget{sga3:viii:section:5}', '% SGA 3, Exposé VIII, tradução brasileira: §5.\n% Autoridade: LNM 152 (1970), pp. 15--19.\n\n','structure','Autoridade do componente fixada em LNM 152, pp. 15–19.')
block(f,15,'\\noindent\\footnote{Nota do editor:', '\\medskip\n\\noindent\\SGARefTarget{sga3:viii:theorem:5:1}', '', 're-edition removed','P. 15 passa do título diretamente a 5.1; não há nota nem parágrafo preliminar sobre M e topologia fpqc.')
change(f,15,r'''\(\mathcal M\)-efetiva (cf. IV,
\SGARefLink{sga3:iv:subsection:3:4}{3.4}); isto é, existe o quociente''',r'''\(\mathcal M\)-efetiva, onde \(\mathcal M\) é o conjunto dos morfismos
fielmente planos quase-compactos (cf. IV), isto é, existe o quociente''','1970 restored','P. 15, 5.1 define M dentro do enunciado e remete somente a IV, sem número 3.4.')
