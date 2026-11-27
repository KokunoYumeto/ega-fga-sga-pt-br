from audit import change,block
from pathlib import Path
f='09_expose_ix/components/05_seccion_4_parte_2.tex'
block(f,58,'\\emph{Demonstração.}\nPor \\SGARefLink{sga3:ix:theorem:4:7}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:remark:4:10}',r'''Em virtude de \SGARefLink{sga3:ix:theorem:4:7}{4.7}, reduz-se
a provar que o subpré-esquema (H) é \emph{fechado}, ou ainda
que é igual a (G) como conjunto. Isso nos reduz ao caso em que
(S) é o espectro de um corpo, mas então todo subpré-esquema em
grupos de (G) é fechado (VI\(_B)
\SGARefLink{cor:sga3-VIB-1.4.2}{1.4.2}), donde a conclusão.
''','translation','Original4.9 proof distinguishes on est ramené from Cela nous ramène, emphasizes fermé, has the reference parenthetically and no heading/square.')
s=(Path('work/sources')/f).read_text();start=s.index(r'\noindent\SGARefTarget{sga3:ix:remark:4:10}')
change(f,58,s[start:],r'''\noindent\SGARefTarget{sga3:ix:remark:4:10}\textbf{Observação 4.10.}
Sob as condições de \SGARefLink{sga3:ix:theorem:4:7}{4.7}, seja
(m) um inteiro (>0) que tenha as propriedades seguintes:
para todo (s\in S), (m) não é uma potência da característica
de (k(s)), e se (G_s) é de tipo (M), os divisores primos
da torção de (M) dividem (m). (NB essa segunda condição é
sempre verificada se (G) é um toro). Então a demonstração dada
mostra que no enunciado de
\SGARefLink{sga3:ix:theorem:4:7}{4.7} e nos corolários
\SGARefLink{sga3:ix:corollary:4:8}{4.8} e
\SGARefLink{sga3:ix:corollary:4:9}{4.9}, pode-se limitar a
considerar os subgrupos da forma ({}_{m^r}G), com (r>0).
Aliás, vê-se imediatamente que quando (G) é suave sobre (S),
então para todo ponto (s\in S), existe uma vizinhança aberta
(U) de (s) e um inteiro (m>0), primo com todas as
características residuais de (U), e que satisfaz as condições
precedentes para (G_U). (Tomar por exemplo para (m) a ordem
da torção do tipo de (G) em (s)). Sob essas condições,
encontram-se ({}_{m^r}G) que são finitos e \emph{étale} sobre
(S), e cuja família é esquematicamente densa, com a condição
de se restringir acima de (U). Essa observação permite em
certos casos (notadamente os que fazem intervir os teoremas
\SGARefLink{sga3:ix:theorem:3:2}{3.2} e
\SGARefLink{sga3:ix:theorem:3:2:bis}{3.2 bis}, cf. XI 6, mas
não os que fazem intervir os teoremas
\SGARefLink{sga3:ix:theorem:3:6}{3.6} e
\SGARefLink{sga3:ix:theorem:3:6:bis}{3.6 bis}) dispensar o
teorema \SGARefLink{sga3:ix:theorem:3:1}{3.1}, que faz
intervir a cohomologia de Hochschild.
''','re-edition removed','Printed4.10 is one paragraph with k(s), two parenthetical asides (the first NB), inline m^r-torsion and emphasis on étales. Restored lisse as suave and removed added1.4.1(a)/2.1(e) references and rearranged displayed presentation.')
f='09_expose_ix/components/06_seccion_5.tex'
change(f,58,'% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 58--63.','% Autoridade: SGA 3, LNM 152 (1970), páginas impressas 58--63.','source authority','The user restricts authority to the attached1970 scan; the section begins at printed58.')
block(f,58,'\\medskip\n\\noindent\\SGARefTarget{sga3:ix:lemma:5:0}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:theorem:5:1}',r'''\SGARefTarget{sga3:ix:lemma:5:0}
''','re-edition removed','Section5 goes directly from its title to Theorem5.1 on printed58. Removed the entire added Lemma5.0, editorial note and proof; its identifier is retained invisibly.')
block(f,58,r'\noindent\SGARefTarget{sga3:ix:theorem:5:1}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:theorem:5:1}\textbf{Teorema 5.1.}
\textit{Sejam (u,v:H\to G) dois homomorfismos de
(S)-pré-esquemas em grupos, com (H) de tipo multiplicativo
e de tipo finito, e (S) localmente noetheriano ou (G) de
apresentação finita sobre (S). Seja (s\in S) tal que
(u_s=v_s), suponhamos (u_s) central. Então existe uma
vizinhança aberta (U) de (s) tal que (u_U=v_U).}
''','translation','Theorem5.1 places all finiteness conditions in the first Soient sentence; restored the original comma before supposons and sentence order.')
