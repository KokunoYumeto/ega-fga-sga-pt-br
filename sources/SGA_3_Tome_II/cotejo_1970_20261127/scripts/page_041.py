from audit import change,block
f='09_expose_ix/components/02_seccion_2.tex'
block(f,41,r'  \item[(b)]\SGARefTarget{sga3:ix:proposition:2:1:item:b:01}', '\\end{enumerate}',r'''  \item[(b)]\SGARefTarget{sga3:ix:proposition:2:1:item:b:01}
  \textit{\(G\) de tipo finito sobre \(S\) \(\Longleftrightarrow\)
  \(G\) de apresentação finita sobre \(S\) \(\Longleftrightarrow\)
  para todo \(s\in S\), o tipo de \(G\) em \(s\) é dado por um
  grupo comutativo de tipo finito.}

  \item[(c)]\SGARefTarget{sga3:ix:proposition:2:1:item:c:01}
  \textit{\(G\) finito sobre \(S\) \(\Longleftrightarrow\) para
  todo \(s\in S\), o tipo de \(G\) em \(s\) é dado por um grupo
  comutativo finito \(\Longleftrightarrow\) (se \(S\) é
  quase-compacto) \(G\) é de tipo finito sobre \(S\) e é anulado
  por um inteiro \(n>0\).}

  \item[\((c')\)]\SGARefTarget{sga3:ix:proposition:2:1:item:cprime:01}
  \textit{\(G\) inteiro sobre \(S\) \(\Longleftrightarrow\) para
  todo \(s\in S\), o tipo de \(G\) em \(s\) é dado por um grupo
  comutativo de torção.}

  \item[(d)]\SGARefTarget{sga3:ix:proposition:2:1:item:d:01}
  \textit{\(G\) é o grupo unidade \(\Longleftrightarrow\) para
  todo \(s\in S\), o tipo de \(G\) em \(s\) é dado pelo grupo
  comutativo nulo.}

  \item[(e)]\SGARefTarget{sga3:ix:proposition:2:1:item:e:01}
  \textit{\(G\) é suave sobre \(S\) \(\Longleftrightarrow\) para
  todo \(s\in S\), o tipo de \(G\) em \(s\) é dado por um grupo
  comutativo de tipo finito cujo subgrupo de torção é de ordem prima
  com a característica de \(k(s)\).}
''','1970 restored','Items b–e print equivalence arrows, full stops, the adjective lisse and the residue-field notation k(s). Restored these rather than expanded iff phrases, and the settled Portuguese term suave.')
change(f,41,r'''Essas afirmações deduzem-se de
\SGARefLink{sga3:viii:proposition:2:1}{VIII~2.1}, levando em conta que
as propriedades em questão descendem por morfismos fielmente planos e
quase compactos (cf. SGA~1, VIII, ou EGA~IV\textsubscript{2}, \S2).

Utilizando \SGARefLink{sga3:viii:corollary:3:5}{VIII~3.5}, obtém-se
também:''',r'''Esses enunciados resultam de
\SGARefLink{sga3:viii:proposition:2:1}{VIII 2.1}, levando em conta que
as propriedades em questão se descendem por morfismos fielmente planos
e quase-compactos (cf. SGA 1 VIII ou EGA IV 2).

Utilizando \SGARefLink{sga3:viii:corollary:3:5}{3.5}, obtém-se igualmente:''','1970 restored','The proof cites SGA 1 VIII ou EGA IV 2, without a volume subscript or section symbol, and the next sentence cites only 3.5, without VIII.')
change(f,41,r'''\(S\). Para todo inteiro \(n\ne0\), o núcleo
\({}_nG=\ker(n\cdot\operatorname{id}_G)\) é um grupo de tipo
multiplicativo, finito sobre \(S\).}''',r'''\(S\), então, para todo inteiro \(n\ne0\), o núcleo \({}_nG\)
de \(n\operatorname{id}_G\) é um grupo de tipo multiplicativo
finito sobre \(S\).}''','1970 restored','Proposition 2.2 is a single sentence and describes the kernel in words, without the added equation =ker(...).')
block(f,41,r'\noindent\SGARefTarget{sga3:ix:proposition:2:3}', '\n\\SGARefLink{sga3:ix:proposition:2:3:item:a:01}',r'''\noindent\SGARefTarget{sga3:ix:proposition:2:3}\textbf{Proposição 2.3.}
\textit{Seja \(G\) um grupo de tipo multiplicativo sobre o pré-esquema
\(S\), que atua livremente à direita sobre o \(S\)-pré-esquema
\(X\) afim sobre \(S\). Então
\SGARefTarget{sga3:ix:proposition:2:3:item:a:01}a relação de equivalência
definida por \(G\) em \(X\) é \(\mathcal M\)-efetiva, onde
\(\mathcal M\) é o conjunto dos morfismos fielmente planos e
quase-compactos (\SGARefLink{sga3:iv:subsection:3:4}{IV 3.4}), além
disso, \(Y=X/G\) é afim sobre \(S\).
\SGARefTarget{sga3:ix:proposition:2:3:item:b:01}Se, além disso, \(X\)
é de apresentação finita (resp. de tipo finito) sobre \(S\), o mesmo
vale para \(Y\).}
''','re-edition removed','The original proposition has one paragraph, no items a/b, and defines M within its first assertion. Restored that definition from its original position instead of the added Definition 2.0; preserved invisible item targets.')
