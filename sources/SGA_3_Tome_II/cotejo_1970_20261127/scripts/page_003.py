from audit import *
f='08_expose_viii/components/01_apertura_hasta_corolario_1_3.tex'
block(f,3,'\\medskip\n\\noindent\\SGARefTarget{sga3:viii:definition:1:0:2}', '\\medskip\n\\noindent\\SGARefTarget{sga3:viii:definition:1:1}',r'''\SGARefTarget{sga3:viii:definition:1:0:2}
Como de costume, diremos então que um \(\mathscr C\)-grupo \(G\) é
\emph{reflexivo} se é reflexivo como \(\widehat{\mathscr C}\)-grupo
(sem nos preocuparmos com o fato de \(D(G)\) ser ou não representável).
Obtém-se assim, por \(D\), uma antiequivalência da categoria dos
\(\mathscr C\)-grupos reflexivos \(G\) tais que \(D(G)\) seja
representável consigo mesma.

\SGARefTarget{sga3:viii:remark:1:0:3}
Assinalemos, para concluir estas generalidades, que a formação dos duais
\(D(G)\) comuta com a extensão da base, que transforma, portanto,
grupos reflexivos em grupos reflexivos.

No que segue, interessar-nos-emos pelo caso em que
\(\mathscr C=(\mathrm{Sch})_{/S}\) é a categoria dos pré-esquemas sobre
\(S\), e \(I=\mathbf G_{m,S}\) é o «grupo multiplicativo sobre \(S\)»,
cf. Exposé~I. Para todo grupo ordinário \(M\), consideramos o
\(S\)-grupo \(M_S\). Vê-se imediatamente que, para todo pré-esquema em
grupos \(I\) sobre \(S\), tem-se um isomorfismo canônico
(funtorial em \(M,I\) e compatível com a extensão da base):
\[
  \operatorname{Hom}_{S\text{-}\mathrm{gr}}(M_S,I)
  =\operatorname{Hom}_{\mathrm{gr}}(M,I(S)).
\]
Aplicando isso a um \(S'\) variável sobre \(S\), obtém-se um isomorfismo
funtorial
\SGARefTarget{sga3:viii:eq:1:0:4}
\[
  D(M_S)(S')\xrightarrow{\ \sim\ }
  \operatorname{Hom}_{\mathrm{gr}}(M,\mathbf G_m(S')).
\]
Recupera-se o funtor já considerado no Exposé~I, também denotado por
\(D_S(M)\), que é representável para \(M\) comutativo, pois
\[
  D_S(M)=D(M_S)=\operatorname{Spec}\mathscr O_S(M),
\]
onde \(\mathscr O_S(M)\) denota a álgebra do grupo \(M\) com
coeficientes em \(\mathscr O_S\). (Observemos, aliás, no caso geral,
que \(D(M)\) não se altera se substituímos \(M\) por \(M\) tornado
abeliano, de modo que nada se perde ao supor \(M\) comutativo.)

''','re-edition removed','P. 3 contém apenas prosa e três fórmulas sem numeração: retiradas Definição 1.0.2, Observação 1.0.3 e tag 1.0.4. A letra do pré-esquema em grupos é I, não J; não há remissão I 4.4 nem a explicação Aplicando-o a J=I. Restauradas a formulação e a pontuação, preservando as âncoras.')
