from audit import block, change
f='09_expose_ix/components/08_seccion_7.tex'
block(f,70,r'envia \(C\) em \(B\).',r'\medskip'+'\n'+r'\noindent\SGARefTarget{sga3:ix:lemma:7:2}',r'''canônico \(C\to\widehat C\) aplica \(C\) em \(B\).
Com efeito, se assim for, encontra-se um homomorfismo de
\(A\)-álgebras \SGARefTarget{sga3:ix:theorem:7:1:display:phi:01}%
\(\varphi:C\to B\), reduzindo-se segundo os
\(\varphi_n\), donde se conclui imediatamente que é
compatível com as aplicações diagonais (pois os
\(\varphi_n\) o são, e
\(B\otimes_AB\to\widehat{B\otimes_AB}\) é injetivo, como
se vê como acima substituindo \(M\) por \(M\times M\)).
Notemos que o homomorfismo diagonal \(\Delta_H\) de
\(H\) define um homomorfismo
\SGARefTarget{sga3:ix:theorem:7:1:display:03}
\[
  \widehat\Delta_H:\widehat B\to\widehat{B\otimes_AB}
\]
passando aos completamentos, e tem-se um diagrama
comutativo (deduzido dos diagramas análogos definidos
pelos \(\varphi_n\) por passagem ao limite projetivo):
\SGARefTarget{sga3:ix:theorem:7:1:diagram:02}
\[
\begin{tikzcd}[column sep=huge,row sep=large]
 C \arrow[r,"\Phi"] \arrow[d,"\Delta_G"']
 & \widehat B \arrow[d,"\Delta_H"]\\
 C\otimes_A C \arrow[r,"\Psi"]
 & \widehat{B\otimes_A B},
\end{tikzcd}
\]
onde \(\Psi\) é a composta
\SGARefTarget{sga3:ix:theorem:7:1:display:04}
\[
 C\xrightarrow{G}C\otimes_A C
 \xrightarrow{\Phi\otimes\Phi}\widehat B\otimes_A\widehat B
 \longrightarrow\widehat{B\otimes_A B}
\]
(a última flecha é o homomorfismo canônico evidente).
Segue-se que para todo \(f\in C\), \(\Phi(f)\) é um
elemento de \(\widehat B\) cuja imagem por
\(\widehat\Delta_H\) é um elemento «decomponível» de
\(\widehat{B\otimes_AB}\), i.e. está na imagem de
\(\widehat B\otimes_A\widehat B\). Basta agora aplicar o

''','1970 restored','P. 70: restore the continuous argument and parentheses; the square prints Delta_H without a hat, and the following chain begins C with arrow label G (both enlarged separately). The extra basis e_m, group-algebra identity and its diagonal calculation do not occur.')
change(f,70,r'''Sejam \(A\) um anel noetheriano, \(M\) um conjunto e
\((a_{m,m'})\) uma família de elementos de \(A\), indexada por
\(M\times M\), que satisfaz:''',r'''Sejam \(A\) um anel noetheriano, \(M\) um conjunto;
\((a_{m,m'})\) uma família de elementos de \(A\) indexada
por \(M\times M\), tal que''','1970 restored','P. 70, lemma 7.2 opening: semicolon after M un ensemble; indexed family followed by telle que, without the expanded introductory wording.')
change(f,70,r'''\(a_{m,m'}=0\) se \(m\neq m'\); isto é, o suporte da família
  está contido na diagonal de \(M\times M\);''',r'''\(a_{m,m'}=0\) se \(m\neq m'\) (i.e. o suporte da
  família está contido na diagonal de \(M\times M\)),''','1970 restored','P. 70, 7.2(i): the explanation of the diagonal support is parenthetical and followed by a comma.')
