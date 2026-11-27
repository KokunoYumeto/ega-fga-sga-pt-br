from audit import change,block
f='09_expose_ix/components/02_seccion_2.tex'
change(f,45,r'''

Por \SGARefLink{sga3:ix:corollary:2:9}{2.9}, segue que \(U\) é aberto
e fechado e que \(H''_U\to H_U\) (respectivamente, \(H''_U\to H_U\) e
\(H''_U\to H'_U\)) são isomorfismos. Isso dá a conclusão desejada.''',r'''
Em virtude de \SGARefLink{sga3:ix:corollary:2:9}{2.9}, segue-se que
\(U\) é aberto e fechado, e que \(H''_U\to H_U\) (resp.
\(H''_U\to H_U\) e \(H''_U\to H'_U\)) são isomorfismos. Daí a
conclusão desejada.''','structure','The proof of 2.10 continues without a paragraph break across pages 44–45, with resp. and D’où la conclusion voulue.')
change(f,45,r'''\textit{Seja \(S\) um pré-esquema, seja \(G\) um \(S\)-grupo de tipo
multiplicativo e de tipo finito sobre \(S\), seja \(H\) um subgrupo de
\(G\) de tipo multiplicativo, e ponhamos \(K=G/H\), grupo quociente de
\(G\) de tipo multiplicativo.}''',r'''\textit{Sejam \(S\) um pré-esquema, \(G\) um \(S\)-grupo de tipo
multiplicativo e de tipo finito sobre \(S\), \(H\) um subgrupo de tipo
multiplicativo de \(G\), \(K=G/H\) (que é um grupo de tipo
multiplicativo quociente de \(G\)).}''','translation','The opening of 2.11 uses Soient once and places the explanation of K in parentheses, without an additional let us put instruction.')
change(f,45,r'''\textit{Suponhamos que \(G\) seja trivial, isto é, diagonalizável.
  Existe uma partição de \(S\) em subconjuntos abertos e fechados \(S_i\)''',r'''\textit{Suponhamos \(G\) trivial i.e. diagonalizável.
  Então existe uma partição de \(S\) em partes \(S_i\) abertas e fechadas''','translation','Item i prints Supposons G trivial i.e. diagonalisable. Alors il existe une partition de S en parties S_i ouvertes et fermées.')
change(f,45,r'''\textit{\SGARefLink{sga3:ix:proposition:2:11:item:i:01}{A mesma
  afirmação} vale substituindo «diagonalizável» por «isotrivial», desde
  que \(S\) seja conexo, localmente conexo ou quase compacto.}''',r'''\textit{Mesmo enunciado que em
  \SGARefLink{sga3:ix:proposition:2:11:item:i:01}{(i)}, substituindo
  «diagonalizável» por «isotrivial», desde que \(S\) seja conexo,
  ou loc. conexo, ou quase-compacto.}''','reading','Item ii explicitly refers to (i) and abbreviates loc. connexe; restore that structure and abbreviation.')
change(f,45,r'''\textit{Se \(G\) é localmente trivial (respectivamente, localmente
  isotrivial, respectivamente, quase-isotrivial), o mesmo vale para \(K\)
  e \(H\).}''',r'''\textit{Suponhamos \(G\) localmente trivial (resp. localmente
  isotrivial, resp. quase-isotrivial), então o mesmo vale para \(K\)
  e para \(H\).}''','translation','Item iii starts Supposons and uses resp., then alors il en est de même de K et de H.')
block(f,45,r'\SGARefLink{sga3:ix:proposition:2:11:item:i:01}{(i)} Por hipótese,', '\n\\SGARefLink{sga3:ix:proposition:2:11:item:ii:01}{(ii)} Por hipótese,',r'''\SGARefLink{sga3:ix:proposition:2:11:item:i:01}{(i)} Por hipótese,
tem-se \(G=D_S(M)\), onde \(M\) é um grupo comutativo de tipo
finito. Para todo grupo quociente \(M_i\) de \(M\), seja
\(H_i=D_S(M_i)\) o subgrupo diagonalizável correspondente de \(G\)
(\SGARefLink{sga3:viii:corollary:3:2}{VIII 3.2}). Seja \(S_i\) o
conjunto dos \(s\in S\) tais que \(H_s=(H_i)_s\); em virtude de
\SGARefLink{sga3:ix:corollary:2:10}{2.10}, \(S_i\) é aberto e
fechado, e tem-se \(H_{S_i}=(H_i)_{S_i}\), portanto \(H_{S_i}\) é
diagonalizável, portanto também \(K_{S_i}\)
(\SGARefLink{sga3:viii:corollary:3:2}{VIII 3.2}). Evidentemente os
\(S_i\) são dois a dois disjuntos, afirmo que cobrem \(S\). Isso
resulta do fato de que, para todo \(s\), \(H_s\) é diagonalizável,
como subgrupo do grupo diagonalizável \(G_s\)
(\SGARefLink{sga3:iv:proposition:4:7:5}{IV 4.7.5}), portanto \(H_s\)
é da forma \(D_{k(s)}(M_i)\)
(\SGARefLink{sga3:viii:corollary:3:2}{VIII 3.2}). Limitando-se à
família dos \(S_i\) não vazios, a conclusão
\SGARefLink{sga3:ix:proposition:2:11:item:i:01}{(i)} aparece.
''','1970 restored','The proof of i cites VIII 3.2 three times and IV 4.7.5; removed the re-edition substitutions VIII 3.1, forward 8.1, VIII 1.5 and 3.2(b). Restored k(s), first-person singular Je dis and the impersonal ending.')
