from audit import change,block
f='09_expose_ix/components/02_seccion_2.tex'
block(f,42,'\\SGARefLink{sga3:ix:proposition:2:3:item:a:01}{A primeira afirmação}', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:2:4}',r'''\SGARefLink{sga3:ix:proposition:2:3:item:a:01}{A primeira afirmação}
resulta de \SGARefLink{sga3:viii:theorem:5:1}{VIII 5.1}, que trata do
caso em que \(G\) é diagonalizável, e de
\SGARefLink{sga3:iv:proposition:3:5:2}{IV 3.5.2}, que permite
reduzir-se a ele, levando em conta que os morfismos fielmente planos
e quase-compactos \(S'\to S\) são morfismos de descida \emph{efetiva}
para a categoria fibrada dos esquemas afins sobre outros, i.e. para
todo \(Y'\) afim sobre \(S'\), munido de um dado de descida
relativamente a \(S'\to S\), esse dado de descida é efetivo, i.e.
\(Y'\) provém de um \(Y\) afim sobre \(S\), cf. SGA 1
\SGARefLink{sga1:viii:proposition:2:1}{VIII 2.1}. Para a
\SGARefLink{sga3:ix:proposition:2:3:item:b:01}{segunda afirmação},
reduz-se igualmente ao caso diagonalizável
\SGARefLink{sga3:viii:corollary:5:8}{VIII 5.8}, pois as condições de
finitude consideradas se descendem por morfismos fielmente planos e
quase-compactos (SGA 1 VIII 3.3 e 3.6). Procedendo como em VIII,
corolários 5.5 a 5.7, deduz-se de
\SGARefLink{sga3:ix:proposition:2:3}{2.3}:
''','1970 restored','The proof continuing from page 41 is one paragraph, with effective emphasized and i.e. twice. The reference is SGA 1 VIII 2.1, not an internal SGA 3 VIII 2.1 link; the final range is 5.5 à 5.7.')
change(f,42,r'''\textit{é uma imersão fechada. Para toda seção \(\sigma\) de \(X\)
sobre \(S\), o morfismo correspondente}
\[
  G\longrightarrow X,\qquad g\longmapsto\sigma\cdot g,
\]''',r'''\textit{é uma imersão fechada. Para toda seção \(s\) de \(X\)
sobre \(S\), o morfismo correspondente \(g\mapsto s.g\):}
\[
  G\longrightarrow X
\]''','reading','Corollary 2.4 uses a Latin s for the section and places g↦s.g in the prose before the displayed map G→X.')
change(f,42,r'''e \(H\) é um fibrado principal homogêneo sobre \(Y\) sob \(G_Y\).}''',r'''por fim, \(H\) é um fibrado principal homogêneo sobre \(Y\) de
 grupo \(G_Y\).}''','translation','Corollary 2.5 ends enfin H est un fibré principal homogène sur Y de groupe G_Y.')
change(f,42,r'''de apresentação finita e separado sobre \(S\). Pode-se então demonstrar
que \(u\) é uma imersão fechada utilizando
\SGARefLink{sga3:viii:proposition:7:12}{VIII~7.12} (veja-se a Observação
\SGARefLink{sga3:viii:remark:7-13:item:b}{VIII~7.13(b)}).''',r'''de apresentação finita sobre \(S\) e separado sobre \(S\).
Então se pode mostrar que \(u\) é uma imersão fechada, utilizando
\SGARefLink{sga3:viii:proposition:7:12}{VIII 7.12} (ver observação
\SGARefLink{sga3:viii:remark:7-13:item:b}{VIII 7.13 b}).''','translation','Remark 2.6 repeats sur S for both hypotheses on H and refers to VIII 7.13 b, without extra parentheses around the item letter.')
