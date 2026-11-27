from audit import change,block
f='09_expose_ix/components/02_seccion_2.tex'
change(f,44,r'''monomorfismo (respectivamente, fielmente plano, respectivamente, um
isomorfismo).}''',r'''monomorfismo (resp. fielmente plano, resp. um
isomorfismo).}''','translation','The continuation of 2.9 uses resp. twice.')
block(f,44,'Seja \\(P\\) (respectivamente, \\(Q\\))', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:2:10}',r'''Seja \(P\) (resp. \(Q\)) o núcleo (resp. conúcleo) de \(u\).
Graças a \SGARefLink{sga3:ix:proposition:2:7}{2.7}, \(Q\) existe e
\(P\) e \(Q\) são de tipo multiplicativo, além disso a formação de
\(P\) e de \(Q\) comuta com toda mudança de base \(S'\to S\), em
particular com a formação das fibras. Por outro lado, \(u\) é um
monomorfismo (resp. fielmente plano, resp. um isomorfismo) se, e
somente se, \(P=0\) (resp. \(Q=0\), resp. \(P=Q=0\)). Reduz-se,
portanto, graças a essas observações, a verificar isto: se \(R\) é
um \(S\)-grupo de tipo multiplicativo, então o conjunto \(U\) dos
\(s\in S\) tais que \(R_s=0\) é aberto e fechado, e \(R_U=0\).
Ora, isso está contido nas considerações que seguem a definição
\SGARefLink{sga3:ix:definition:1:4}{1.4}.
''','1970 restored','The original refers to the considerations following Definition 1.4, not the added Remark 1.4.1(a), and uses the impersonal On est donc ramené and resp. abbreviations.')
block(f,44,r'\noindent\SGARefTarget{sga3:ix:corollary:2:10}', '\nAqui, naturalmente',r'''\noindent\SGARefTarget{sga3:ix:corollary:2:10}\textbf{Corolário 2.10.}
\textit{Sejam \(G\) um \(S\)-grupo de tipo multiplicativo e de tipo
finito, \(H\) e \(H'\) dois subgrupos de tipo multiplicativo. Então
\SGARefTarget{sga3:ix:corollary:2:10:item:a:01}\(H''=H\cap H'\) é
um subgrupo de tipo multiplicativo de \(G\).
\SGARefTarget{sga3:ix:corollary:2:10:item:b:01}Seja \(U\) o conjunto
dos \(s\in S\) tais que \(H_s\subset H'_s\) (resp. \(H_s=H'_s\)).
Então \(U\) é aberto e fechado, e \(H_U\subset H'_U\) (resp.
\(H_U=H'_U\)).}
''','re-edition removed','Corollary 2.10 is one paragraph, without items a/b; the inclusions use the plain subset sign, and the abbreviation is resp. Invisible item targets remain.')
block(f,44,'Aqui, naturalmente', '\nPor \\SGARefLink{sga3:ix:corollary:2:9}',r'''Naturalmente, o sinal de interseção em \(H\cap H'\) designa a
interseção no sentido funtorial, i.e. \(H\times_G H'\), que é
evidentemente um sub-\(S\)-grupo de \(G\); do mesmo modo, o sinal de
inclusão designa a relação de ordem entre subobjetos de \(H\) (e não
a igualdade para os conjuntos subjacentes). Aplicando primeiro
\SGARefLink{sga3:ix:proposition:2:7}{2.7} ao morfismo de inclusão
\(H\to G\), encontra-se que \(H\) é de tipo finito, do mesmo modo
\(H'\) é de tipo finito. Resulta então de
\SGARefLink{sga3:ix:corollary:2:8}{2.8} que \(H\cap H'\) é de tipo
multiplicativo e de tipo finito (note-se que o funtor canônico da
categoria considerada em \SGARefLink{sga3:ix:corollary:2:8}{2.8}
para a categoria \((\mathrm{Sch})/S\) comuta com os limites
projetivos finitos). A formação de \(H\cap H'\) comuta com a
extensão da base, em particular com a formação das fibras, aliás
\(H\subset H'\) (resp. \(H=H'\)) equivale a \(H''=H\) (resp.
\(H''=H\) e \(H''=H'\)). Consideremos então os homomorfismos
canônicos \(H''\to H\) e \(H''\to H'\), então \(U\) é o conjunto
dos \(s\in S\) tais que o homomorfismo induzido \(H''_s\to H_s\)
seja um isomorfismo (resp. tais que \(H''_s\to H_s\) e
\(H''_s\to H'_s\) seja um isomorfismo).
''','1970 restored','The original proof is one continuous paragraph. It literally says subobjects of H (not equality for the underlying sets), without the added resp. alternatives or subfunctor wording; preserve its wording even where mathematically awkward. Also restore the singular soit un isomorphisme for the two arrows at the end of page 44, and the subset signs.')
