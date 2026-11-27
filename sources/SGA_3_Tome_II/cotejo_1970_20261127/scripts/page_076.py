from audit import block,change
from pathlib import Path
f='09_expose_ix/components/09_seccion_8_y_bibliografia.tex'
change(f,76,r'e toda extensão de \(K\) por \(H\) já é diagonalizável.',r'''que \(H^1(k_{\mathrm{fpqc}},L_k)
=\operatorname{Hom}(\operatorname{Gal}(\overline k/k),L)
\simeq0\), o que significa que toda extensão de \(K\)
por \(H\) já é diagonalizável.''','1970 restored','P. 76, first line: original inline H^1(k_fpqc,L_k)=Hom(Gal(kbar/k),L) is isomorphic to 0, followed by ce qui signifie que; enlarged at 5x. The reedition étale/Gamma/topological-Hom formula was removed on p. 75.')
block(f,76,r'\textbf{Observação 8.3.}',r'\SGARefTarget{sga3:ix:bibliography}',r'''\textbf{Observações 8.3.}
Como já se assinalou na demonstração de
\SGARefLink{sga3:ix:proposition:8:2}{8.2}, a primeira
asserção é enunciada e provada sobre uma base qualquer
em \SGARefLink{sga3:xvii:proposition:7:1:1}{XVII 7.1.1}.
Por outro lado, a segunda asserção se generaliza, com
essencialmente a mesma demonstração, ao caso de um
esquema de base íntegro normal (ou mais geralmente,
geometricamente unirramoso), utilizando
\SGARefLink{sga3:x:lemma:5-13}{X 5.13} mais adiante.
Por fim, pode-se também considerar
\SGARefLink{sga3:ix:proposition:8:1}{8.1} como um
corolário do resultado (claramente menos trivial)
\SGARefLink{sga3:ix:theorem:6:8}{6.8}, igualmente
válido sobre um esquema de base arbitrário.

''','1970 restored','P. 76, Remarques 8.3: plural heading, roman continuous paragraph, generalization with essentially the same proof (not added descent wording), parenthetical unibranch hypothesis, and parenthetical less trivial applied to result 6.8. Intègre follows supplied glossary: íntegro.')
s=(Path('work/sources')/f).read_text();old=s[s.index(r'\SGARefTarget{sga3:ix:bibliography}'):]
change(f,76,old,r'''\SGARefTarget{sga3:ix:bibliography}%
\SGARefTarget{sga3:ix:bib:bens}%
''','re-edition removed','P. 76 ends immediately after Remarques 8.3; the rest of the printed page is blank. Added bibliography heading, TOC entry, editorial footnote and BEns entry are removed, preserving invisible targets.')
