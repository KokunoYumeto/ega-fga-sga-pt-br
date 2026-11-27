from audit import change,block
f='09_expose_ix/components/01_apertura_y_seccion_1.tex'
change(f,40,r'''Segue-se que se tem uma partição canônica como união disjunta de
pré-esquemas \(S_i\) tais que, para todo \(i\), \(G_{S_i}\) é de tipo
\(M_i\), onde os grupos comutativos \(M_i\) não são isomorfos dois a dois.

\SGARefTarget{sga3:ix:remark:1:4:1:item:b}\textit{b) Em particular, se
\(S\) é conexo, o tipo das fibras de \(G\) é constante; isto é,
existe um grupo comutativo \(M\) tal que \(G\) é de tipo \(M\). Por
fim, se \(G\) é um toro, o tipo de \(G\) em \(s\) é determinado
pelo inteiro \(\dim G_s\): com efeito, \(G_s\) é de tipo \(\mathbb Z^n\),
onde \(n=\dim G_s\).}''',r'''Segue-se que se tem uma \emph{partição canônica} de \(S\) em soma de
pré-esquemas \(S_i\), tal que, para todo \(i\), \(G_{S_i}\) seja de
tipo \(M_i\), onde os \(M_i\) são grupos comutativos dois a dois não
isomorfos. \SGARefTarget{sga3:ix:remark:1:4:1:item:b}Em particular,
se \(S\) é conexo, então o tipo das fibras de \(G\) é constante,
i.e. existe um grupo comutativo \(M\) tal que \(G\) seja de tipo
\(M\). Por fim, se \(G\) é um toro, o tipo de \(G\) em \(s\) é
caracterizado pelo inteiro \(\dim G_s\) (com efeito, \(G_s\) é de
tipo \(\mathbb Z^n\), onde \(n=\dim G_s\)).''','re-edition removed','Page 40 continues the unnumbered paragraph: partition canonique de S en somme, then En particulier without an item b or italics, ending with a parenthetical explanation. Preserved the invisible b target.')
s=open('work/sources/'+f).read();start=s.index(r'\noindent\SGARefTarget{sga3:ix:remark:1:5}')
change(f,40,s[start:],r'''\noindent\SGARefTarget{sga3:ix:remark:1:5}\textbf{Observações 1.5.}
\SGARefTarget{sga3:ix:remark:1:5:item:a}É trivial, pelas definições
\SGARefLink{sga3:ix:definition:1:1}{1.1} e
\SGARefLink{sga3:ix:definition:1:3}{1.3}, que estas são
«compatíveis com a extensão da base». Assim, se \(G\) é um
pré-esquema em grupos sobre \(S\), e \(S'\to S\) um morfismo de
mudança de base, então, se \(G\) é de tipo multiplicativo (resp. de
tipo multiplicativo isotrivial, etc.), então \(G'\) é de tipo
multiplicativo (resp.\ \dots).
\SGARefTarget{sga3:ix:remark:1:5:item:b}Quando, além disso,
\(S'\to S\) é fielmente plano e quase-compacto, então, se \(G'\)
é de tipo multiplicativo, resp. um toro, o mesmo vale para \(G\).
Se, além disso, \(S'\to S\) é étale (resp. finito étale), e \(G'\)
quase-isotrivial (resp. isotrivial), o mesmo vale para \(G\).
\SGARefTarget{sga3:ix:remark:1:5:item:c}Por fim, voltando a um
morfismo de mudança de base qualquer \(f:S'\to S\), se \(s'\in S'\)
e \(s=f(s')\), então o tipo de \(G'\) em \(s'\) é igual ao de
\(G\) em \(s\), pois \(G'_{s'}=G_s\otimes_{k(s)}k(s')\).

''','re-edition removed','The scan prints Observations (plural), one roman paragraph with no a/b/c subdivision and the final fibre formula inline using k(s),k(s′). All item targets are retained invisibly; resp. and repeated predicates follow the original.')
f='09_expose_ix/components/02_seccion_2.tex'
change(f,40,'% Autoridade: Polo--Gille Exp9-8nov09.pdf; edição original: LNM 152, pp. 40--46.','% Autoridade: SGA 3, LNM 152 (1970), pp. 40--46.','re-edition removed','Section 2 begins on printed page 40; the only textual authority is the 1970 printing.')
change(f,40,r'''dos resultados da Exposição precedente, levando-se em conta
\SGARefLink{sga3:ix:definition:1:1}{as definições de 1.1} e o caráter
«local» (para a topologia fielmente plana e quase compacta) dos
resultados considerados.''',r'''dos resultados do exposé precedente, levando-se em conta as definições
\SGARefLink{sga3:ix:definition:1:1}{1.1} e a natureza «local»
(no sentido da topologia fielmente plana e quase-compacta) dos
resultados em questão.''','translation','The section opening says exposé précédent, définitions 1.1 and nature locale (au sens de la topologie...), with no change in mathematical content.')
block(f,40,'\\medskip\n\\noindent\\SGARefTarget{sga3:ix:definition:2:0}', '\\medskip\n\\noindent\\SGARefTarget{sga3:ix:proposition:2:1}',r'''\SGARefTarget{sga3:ix:definition:2:0}

''','re-edition removed','There is no Definition 2.0 or editorial footnote on page 40: the introductory paragraph is followed immediately by Proposition 2.1. The target alone is retained invisibly.')
change(f,40,r'''\(S\). Então:}
\begin{enumerate}
  \item[(a)]\SGARefTarget{sga3:ix:proposition:2:1:item:a:01}
  \textit{\(G\) é fielmente plano sobre \(S\) e afim sobre \(S\)
  (\emph{a fortiori}, quase compacto sobre \(S\));}''',r'''\(S\). Tem-se o seguinte:}
\begin{enumerate}
  \item[(a)]\SGARefTarget{sga3:ix:proposition:2:1:item:a:01}
  \textit{\(G\) é fielmente plano sobre \(S\), e afim sobre \(S\)
  (a fortiori quase-compacto sobre \(S\)).}''','translation','Proposition 2.1 says On a ce qui suit; item a ends with a full stop and no nested emphasis of a fortiori.')
