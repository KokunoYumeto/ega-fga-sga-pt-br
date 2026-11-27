from audit import *
f='08_expose_viii/components/07_seccion_5.tex'
block(f,17,r'''Tem-se \(K\subseteq K'\)''','Utilizando a trigraduação',r'''portanto, a hipótese de que \(G\) atua livremente sobre \(P\) exprime-se
pelas relações
\[
  d_m\in J=\sum_p A(M\times M)\,A_p\,d_p.
  \tag{xx}\label{sga3:viii:theorem:5:1:eq:xx:01}
\]

''','re-edition removed','P. 17: a primeira frase conduz diretamente a (xx), com J. Não há K contido em K′, equivalência com K=K′ ou bar-phi.')
change(f,17,r'f\in A_{-p}\cdot A_p',r'f\in A_p\cdot A_{-p}','reading','P. 17: a ordem dos fatores no coeficiente de e_{r,s} é A_p A_{-p}.')
change(f,17,r'''  \left\{
  \begin{aligned}
    d_m=e_{m,0}-e_{0,m}
      &=\sum_{r,s}\lambda_{r,s}
        (e_{m-s,s}-e_{r,m-r}),\\
    \lambda_{r,s}&\in J_p=A_p\cdot A_{-p}\subseteq A_0,
      \qquad p=m-(r+s).
  \end{aligned}
  \right.''',r'''  \begin{aligned}
    d_m=e_{m,0}-e_{0,m}
      &=\sum_{r+s}\lambda_{r,s}
        (e_{m-s,s}-e_{r,m-r}),\\
    \text{com }\lambda_{r,s}&\in J_p=A_p\cdot A_{-p}\subset A_0,
      \qquad p=m-(r+s).
  \end{aligned}''','1970 restored','P. 17, (xxx): índice do somatório é r+s, não r,s; não há chave agrupadora; a inclusão é simples. Leitura ampliada preserva a notação impressa mesmo irregular.')
change(f,17,r'''\textit{Sob as condições anteriores, sendo \(A_0\) um corpo, se
\(M\ne0\),''',r'''\textit{Sob as condições anteriores, se \(M\ne0\),''','re-edition removed','P. 17, 5.2 não repete que A_0 é corpo; isso já foi estabelecido no parágrafo anterior.')
change(f,17,r'''se anularia para todo
\(m\in M\), o que é absurdo.''',r'''seria nula, o que é absurdo.''','re-edition removed','P. 17, prova de 5.2: não imprime o quantificador adicional para todo m em M.')
