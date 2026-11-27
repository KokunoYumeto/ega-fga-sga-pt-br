from audit import *
f='08_expose_viii/components/07_seccion_5.tex'
change(f,16,r'  \theta:A\otimes_{A_0}A\longrightarrow A(M)',r'  A(M)\longleftarrow A\otimes_{A_0}A','1970 restored','P. 16, primeira fórmula: seta para a esquerda e nenhum nome theta.')
block(f,16,r'''Tem-se \(R=\operatorname{Spec}(A(M))\)''',r'''Tem-se \(K\subseteq K'\)''',r'''Ora, tem-se
\[
  R=\operatorname{Spec}(A(M)),\qquad R'=A(M\times M)/J,
\]
onde \(J\) é o ideal gerado pelos elementos da forma
\[
  x_m(e_{m,0}-e_{0,m}),\qquad m\in M,\quad x_m\in A_m,
\]
e, finalmente, o morfismo diagonal \(R\to R'\) é dado pelo homomorfismo
\[
  x e_{m,n}\longmapsto x e_{m+n}\qquad(m,n\in M,\ x\in A)
\]
de \(A(M\times M)\) em \(A(M)\), passando ao quociente por \(J\).
(Os \(e_m\), resp. \(e_{m,n}=e_m\otimes e_n\), são os elementos da
base canônica de \(A(M)\), resp. \(A(M\times M)\).) Ora, o núcleo do
homomorfismo anterior é o ideal gerado pelos
\[
  d_m=e_{m,0}-e_{0,m},
\]
''','1970 restored','P. 16: o ideal se chama J; a impressão dá R′=A(M×M)/J, sem Spec. Não define phi, bar-phi ou K′ nem comenta seus núcleos. Retirados a nota de mudança de notação, o comentário entre colchetes e a expansão; restaurada a redação sobre o homomorfismo anterior.')
