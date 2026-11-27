from audit import change,block
import re
f='09_expose_ix/components/04_seccion_4_parte_1.tex'
s=open('work/sources/'+f).read();i=s.index('Mais geralmente,')
change(f,54,s[i:],r'''De modo geral, para todo \(S\)-pré-esquema \(P\), pôr-se-á
\(P_n=P\times_S S_n\). Em virtude de
\SGARefLink{sga3:viii:theorem:6:4}{VIII 6.4}, tem-se isto: para todo
\(n\), e \(i\in I\), existe um subpré-esquema \(T_n^i\) de
\(S_n\), que representa o funtor
\SGARefTarget{sga3:ix:lemma:4:4:display:03}\(F_n^i\) seguinte
\((\mathrm{Sch})/S_n^\circ\to(\mathrm{Ens})\): para \(P\) sobre
\(S_n\), \SGARefTarget{sga3:ix:lemma:4:4:display:04}\(F_n^i(P)\)
é vazio se \((Z_n^i)_P\ne(Y_n^i)_P\) e é reduzido a um elemento
no caso contrário. Posto isso, vê-se imediatamente que, para \(i\)
fixo, e \(m\geq n\), tem-se \(T_n^i=T_m^i\times_{S_m}S_n\).
Seja \(\widehat S=\operatorname{Spec}(\widehat A)\), \(\widehat A\)
o anel completado de \(A\), segue-se imediatamente que existe um
subesquema fechado \(T^i\) de \(\widehat S\) que se reduz aos
\(T_n^i\). Seja \(T\) o subesquema fechado de \(\widehat S\)
interseção dos \(T^i\). Como \(\widehat S\) é noetheriano, existe
uma parte finita \(J\) de \(I\), tal que se tenha
\(T=\bigcap_{i\in J}T^i\).

''','re-edition removed','Page 54 introduces F_n^i directly after VIII 6.4 and describes its empty/singleton values in prose, with no product-functor notation, Γ, id, artinian-flatness explanation, ideals K_n^i or editorial footnote. The original writes Spec(Â), closed subschemes and the finite intersection; it does not use Spf or formal schemes. The rightmost part of the inequality is near the damaged gutter; its visible beginning and the paired Y/Z notation give (Z_n^i)_P≠(Y_n^i)_P.')
f='09_expose_ix/components/05_seccion_4_parte_2.tex'
change(f,54,'% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 54--58.','% Autoridade: SGA 3, LNM 152 (1970), pp. 54--58.','re-edition removed','The continued proof and section 4 are governed solely by LNM152 (1970), pages54–58.')
s=open('work/sources/'+f).read();start=s.index('Para \\(i\\) fixo');end=s.index('\\medskip\n\\noindent\\SGARefTarget{sga3:ix:lemma:4:5}',start)
old=s[start:end];anchors=''.join(re.findall(r'\\(?:SGA(?:Inline)?RefTarget|label)\{[^{}]+\}',old))
change(f,54,old,r'''Como \(Y'{}^i=Z'{}^i\), existe um \(A''\) tal que
\(Y''{}^i=Z''{}^i\) (onde \(A''\) satisfaz as condições
explicitadas acima). A priori, \(A''\) depende de \(i\), mas se
pode encontrar um \(A''\) que sirva para todos os \(i\in J\),
pois \(J\) é finito. Pela definição dos \(T^i\), segue-se que
\(S''_n\to S_n\) se fatora por \(S''_n\to T_n^i\) para todo
\(i\in J\), portanto também por \(T_n=\bigcap_{i\in J}T_n^i\),
portanto também por \(T_n^i\) para \emph{todo} \(i\in I\).
Isso significa que, para todo \(n\), \(f''_n\) se anula sobre os
\(Z''{}^i_n\). Segundo
\SGARefLink{sga3:ix:lemma:4:2}{4.2} aplicado a
\(S''_n,X''_n,(Z''{}^i_n)_{i\in I},S''_0\), e
\SGARefLink{sga3:ix:lemma:4:5}{4.5} abaixo, segue-se que
\(f''_n=0\). Como isso é verdadeiro para todo \(n\) e \(X''\)
é noetheriano, portanto seus anéis locais separados para sua
topologia habitual, segue-se que \(f''\) é nulo nos pontos \(x''\)
de \(X''\) sobre \(s''\). (Note-se que, se \(\mathfrak m\)
designa o ideal maximal de \(A\), então, para todo \(x''\) sobre
\(s''\), a topologia de \(\mathscr O_{X'',x''}\) definida pelos
\(\mathfrak m^n\mathscr O_{X'',x''}\) é separada, pois
\(\mathfrak m\mathscr O_{X'',x''}\) está contido no ideal maximal
de \(\mathscr O_{X'',x''}\)). A fortiori, \(f'\) é nulo nos
pontos \(x'\) de \(X'\) sobre \(s'\), cqfd. Resta apresentar a
demonstração do
'''+anchors+'\n\n','re-edition removed','The original has only this second paragraph before Lemma4.5. Removed the entire expanded formal-scheme/ideal/Mittag–Leffler argument, its exact-sequence diagram and Bourbaki/EGA references, the S″_(n) versus S″_n construction, corrective bracket notes, extra rings/fibres, and added Lemma4.5.0 with its footnote/proof. Restored the original direct factorization, use of 4.2 and 4.5, and parenthetical m-adic separation argument. Retained all removed-block labels invisibly.')
block(f,54,r'\noindent\SGARefTarget{sga3:ix:lemma:4:5}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:lemma:4:5}\textbf{Lema 4.5.}
\textit{Sejam \(X\) um pré-esquema localmente noetheriano sobre um
corpo \(k\), \((Z^i)_{i\in I}\) uma família de subpré-esquemas de
\(X\), \(k'\) uma extensão de \(k\), \(X'\) e \(Z'{}^i\) os
pré-esquemas deduzidos de \(X,Z^i\) pela mudança de base \(k'/k\).
Para que \((Z^i)_{i\in I}\) seja esquematicamente densa em \(X\),
é necessário e suficiente que \((Z'{}^i)_{i\in I}\) o seja em \(X'\).}
''','1970 restored','Lemma4.5 uses one Soient list, superscript i and the phrasing Pour que ... il faut et il suffit; restored those and the explicit term preschemes for X′,Z′^i.')
