from audit import block
f='09_expose_ix/components/08_seccion_7.tex'
block(f,69,'\\emph{Demonstração.}\nSuponhamos primeiro', 'envia \\(C\\) em \\(B\\).',r'''Suponhamos primeiro \(H\) diagonalizável, logo da forma
\[
  H=\operatorname{Spec}A(M),
\]
onde \(B=A(M)\) é a álgebra do grupo comutativo \(M\)
com coeficientes em \(A\). Ter-se-á também
\(G=\operatorname{Spec}(C)\), onde \(C\) é uma
\(A\)-álgebra munida de uma aplicação diagonal
(satisfazendo aos axiomas conhecidos). Então os
homomorfismos de \(S\)-grupos \(H\to G\) correspondem
biunivocamente aos homomorfismos de \(A\)-álgebras
\(\varphi:C\to B\) compatíveis com as aplicações
diagonais, i.e. tais que
\SGARefTarget{sga3:ix:theorem:7:1:display:01}
\[
  \Delta_H\varphi(f)=(\varphi\otimes\varphi)(\Delta_G(f))
\]
para todo \(f\in C\), onde \(\Delta_H\) e \(\Delta_G\)
são as aplicações diagonais. Tem-se uma descrição
análoga para os homomorfismos de \(S_n\)-grupos
\(H_n\to G_n\), definidos por certos homomorfismos de
\(A_n\)-álgebras \(\varphi_n:C_n\to B_n\), (onde se põe
\(A_n=A/I^{n+1}\), \(B_n=B\otimes_AA_n\),
\(C=C\otimes_AA_n\)). Ponhamos
\SGARefTarget{sga3:ix:theorem:7:1:display:02}
\[
  \widehat B=\varprojlim_nB_n,\qquad
  \widehat C=\varprojlim_nC_n,
\]
então \(\widehat B=\varprojlim_nA_n(M)\) identifica-se
com um submódulo do produto \(A^M\) (a saber, aquele
formado pelas famílias \((a_m)_{m\in M}\) de elementos
de \(A\) que tendem a 0 segundo o filtro dos
complementares das partes finitas de \(M\)), o que
implica em todo caso que o homomorfismo canônico
\(B\to\widehat B\) é injetivo, donde resulta imediatamente
que o homomorfismo
\SGARefLink{sga3:ix:theorem:7:1:equation:x}{(x)} de
\SGARefLink{sga3:ix:theorem:7:1}{7.1} é injetivo.
\SGARefTarget{sga3:ix:theorem:7:1:diagram:01}%
Provemos que é sobrejetivo, logo tomemos um sistema
projetivo \((\varphi_n)_{n\geq0}\) e provemos que provém
por redução de um \(\varphi\) do primeiro membro.
A priori, \((\varphi_n)\) define um homomorfismo nas
álgebras completadas
\[
  \widehat\varphi:\widehat C\to\widehat B,
\]
e tudo se reduz a ver que sua composta
\(\Phi:C\to\widehat C\xrightarrow{\widehat\varphi}\widehat B\)
com o homomorfismo
''','re-edition removed','Printed69 has the original displayed H, compatibility formula, completions and completed homomorphism, with other maps inline. Restored the omitted Delta_H/Delta_G explanation and direct injectivity conclusion for(x). Preserved C=C tensor A_n without subscript; removed the bracketed correction, editorial footnote, added theta notation, commuting square and expanded reduction text. The explicit A_n=A/I^{n+1} confirms the exponent used at the occluded right edge of printed68.')
