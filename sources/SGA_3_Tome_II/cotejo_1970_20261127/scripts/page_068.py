from pathlib import Path
from audit import change,block
f='09_expose_ix/components/07_seccion_6.tex'
s=(Path('work/sources')/f).read_text();start=s.index("Por construção, \\(v'_s\\)")
change(f,68,s[start:],r'''Então \(v'_s\) é o homomorfismo unidade por construção,
logo em virtude de \SGARefLink{sga3:ix:corollary:5:2}{5.2}
existe uma vizinhança aberta \(U\) de \(s\) tal que
\(v'|U:K'|U\to G|U\) seja o homomorfismo unidade.
Logo, substituindo \(S\) por \(U\), pode-se supor \(v'\)
o homomorfismo unidade, logo que \(u\) se fatora em
\SGARefTarget{sga3:ix:theorem:6:8:diagram:02}
\[
\begin{tikzcd}[column sep=large]
  H \arrow[r,"u'"] & H/K' \arrow[r,"u''"] & G.
\end{tikzcd}
\]
Ora, sendo \(u''_s\) deduzido de \(u_s\) fatorando através
de \(H_s\to H_s/\operatorname{Ker}u_s\), \(u''_s\) é um
monomorfismo (\SGARefLink{sga3:iv:remark:5:2:6}{IV 5.2.6}),
logo em virtude de \SGARefLink{sga3:ix:corollary:6:6}{6.6}
existe uma vizinhança aberta \(U\) de \(s\) tal que
\(u''|U:(H/K')|U\to G|U\) seja um monomorfismo.
Logo, restringindo \(S\), vê-se que \(u''\) é um
monomorfismo, logo
\(\operatorname{Ker}u=\operatorname{Ker}u'=K'\), o que
prova que \(\operatorname{Ker}u\) é de tipo multiplicativo.

A mesma demonstração é válida se, em vez de supor \(G\)
de apresentação finita sobre \(S\), se supõe \(S\)
localmente noetheriano, ao menos no caso em que \(H\) é
diagonalizável. No caso em que não se faz essa hipótese
sobre \(H\), é preciso mostrar que se pode encontrar uma
mudança de base de cobertura \(S'\to S\), com \(S'\)
\emph{localmente noetheriano}, que trivialize \(H\).
É o que se verá com efeito no exposé seguinte
(\SGARefLink{sga3:x:corollary:4-6}{X 4.6}).
''','1970 restored','Printed68 has one displayed factorization only; the restrictions, quotient arrow and kernel identities remain inline. Restored on-register, the parenthetic IV5.2.6/X4.6 references and emphasized locally-noetherian condition. Covering base change is cobertura, not revestimento; no final square.')
f='09_expose_ix/components/08_seccion_7.tex'
change(f,68,'% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 68--73.','% Autoridade: SGA 3, LNM 152 (1970), páginas impressas 68--73.','structure','Section7 begins on printed68; retain only the1970 authority in source comments.')
block(f,68,r'\noindent\SGARefTarget{sga3:ix:theorem:7:1}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:theorem:7:1}\textbf{Teorema 7.1.}
\textit{Sejam \(A\) um anel noetheriano, munido de um ideal
\(I\) tal que \(A\) seja separado e completo para a
topologia \(I\)-ádica, \(S=\operatorname{Spec}(A)\),
\(S_n=\operatorname{Spec}(A/I^{n+1})\), \(H,G\)
\(S\)-pré-esquemas em grupos, com \(H\) de tipo
multiplicativo isotrivial, e \(G\) afim. Então a aplicação
canônica
\SGARefTarget{sga3:ix:theorem:7:1:equation:x}
\begin{equation}
  \tag{x}
  \operatorname{Hom}_{S\text{-}\mathrm{gr}}(H,G)
  \longrightarrow
  \varprojlim_n
  \operatorname{Hom}_{S_n\text{-}\mathrm{gr}}(H_n,G_n)
\end{equation}
é bijetiva (onde \(H_n,G_n\) são os \(S_n\)-grupos
deduzidos de \(H,G\) por mudança de base \(S_n\to S\)).}
''','re-edition removed','Theorem7.1 is one Soient list with S and S_n inline; its canonical arrow(x) is unnamed, and the final explanation is parenthetic. Removed the added theta label and displayed definitions. The right edge of the S_n quotient is affected by the gutter; unchanged n+1 is to be cross-read in the explicit A_n formula on the following page.')
