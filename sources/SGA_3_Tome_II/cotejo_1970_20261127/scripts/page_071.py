from audit import block
f='09_expose_ix/components/08_seccion_7.tex'
block(f,71,r'  \item[(ii)]',r'''tal que
\[
  H'=H\times_SS'
''',r'''  \item[(ii)] \SGARefTarget{sga3:ix:lemma:7:2:item:ii}
  Tem-se
  \SGARefTarget{sga3:ix:lemma:7:2:display:01}
  \[
    a_{m,m'}=\sum_i b_m^ic_{m'}^i,
  \]
  onde os \(b^i,c^i\) são elementos de \(A^M\) em número
  finito (em outros termos, \((a_{m,m'})\) pertence à
  imagem do homomorfismo canônico
  \[
    A^M\otimes_AA^M\longrightarrow A^{M\times M}\;).
  \]
\end{enumerate}
\end{itshape}

Nessas condições, o suporte da família \((a_{m,m'})\)
é \emph{finito}.

Em virtude de \SGARefLink{sga3:ix:lemma:7:2:item:i}{(i)},
a família \((a_{m,m'})\) é determinada pelo conhecimento
dos \(a_m=a_{m,m}\). Ponhamos para todo
\(x=(x_n)_{n\in M}\in A^{(M)}\):
\[
  (u.x)_m=\sum_{m'}a_{m,m'}x_{m'},
\]
i.e. interpretemos \((a_{m,m'})\) como a matriz de um
homomorfismo \(u:A^{(M)}\to A^M\). Então em virtude de
\SGARefLink{sga3:ix:lemma:7:2:item:i}{(i)} ter-se-á simplesmente
\[
  (u.x)_m=a_mx_m\quad\text{i.e.}\quad u.x=ax,
\]
por outro lado em virtude de
\SGARefLink{sga3:ix:lemma:7:2:item:ii}{(ii)} ter-se-á
\[
  u.x\in\sum_i A.b^i,
\]
logo \(u(A^{(I)})\) fica em um \(A\)-módulo de tipo
finito. Por conseguinte, denotando por \((e^m)_{m\in M}\)
a base canônica de \(A^{(M)}\subset A^M\), os
\(a_me^m\) ficam em um \(A\)-módulo de tipo finito.
Como \(A\) é noetheriano, o módulo que eles geram é ele
próprio de tipo finito, o que implica (pois os \(e^m\)
são linearmente independentes) que todos os \(a_m\),
salvo um número finito, são nulos. Isso prova
\SGARefLink{sga3:ix:lemma:7:2}{7.2} e por conseguinte
\SGARefLink{sga3:ix:theorem:7:1}{7.1} no caso em que
\(H\) é diagonalizável.

Provemos o caso geral em que se supõe somente \(H\)
isotrivial, i.e. que existe um morfismo finito étale
sobrejetivo
\[
  S'\longrightarrow S
\]
''','1970 restored','P. 71: restore parenthetical reformulation in (ii), roman conclusion with finite emphasized, continuous proof without heading or square, direct-sum notation A^{(M)}, the printed isolated A^{(I)}, basis e^m (superscript), u.x=ax, parentheses and original transition. The I and superscripts were enlarged at 6x.')
