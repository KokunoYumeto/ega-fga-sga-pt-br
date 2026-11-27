from audit import *
import re
f='08_expose_viii/components/05_seccion_4_parte_1.tex'
change(f,13,r'H^1(S,\mathcal O_S^\times)',r'H^1(S,\mathcal O_S^*)','reading','P. 13, 4.4: o feixe de unidades é O_S com asterisco, não sinal de multiplicação.')
change(f,13,r'''\SGARefLink{sga3:viii:corollary:4:5}{enunciado seguinte}, uma das formas
do «\SGARefLink{sga3:viii:corollary:4:5}{Teorema 90}» de Hilbert.''',r'''\SGARefLink{sga3:viii:corollary:4:5}{enunciado seguinte}:''','structure','P. 13: a menção ao teorema 90 vem depois do Corolário 4.5.')
change(f,13,r'''\medskip
\noindent\SGARefTarget{sga3:viii:remark:4:5:1}\textbf{Observação 4.5.1.}
\SGARefLink{sga3:viii:corollary:4:5}{O enunciado anterior}''',r'''Esta é uma das variantes do «teorema 90» de Hilbert.
\SGARefTarget{sga3:viii:remark:4:5:1}
Observe-se que \SGARefLink{sga3:viii:corollary:4:5}{o enunciado anterior}''','re-edition removed','P. 13: não há Observação 4.5.1; restaura-se o parágrafo contínuo começando pela variante do teorema 90.')
s=(ROOT/'sources'/f).read_text();a=s.index('\\footnote{Nota do editor: foi acrescentado o que segue.}');b=s.index('Precisaremos do',a);old=s[a:b]
anchors=re.findall(r'\\SGA(?:Inline)?RefTarget\{[^{}]+\}',old)
change(f,13,old,'\n'.join(anchors)+'\n\n','re-edition removed','P. 13: a observação termina na afirmação de que o primeiro grupo de cohomologia é Z/2Z e passa ao resultado seguinte. Retirados a norma C/R, o torsor N(z)=-1, a sequência exata e sua cohomologia, a referência XXIV 8.4 e a prova expandida.')
change(f,13,'primeiro grupo de coomologia','primeiro grupo de cohomologia','translation','P. 13: 1-cohomologie; grafia cohomologia do glossário anexo.')
