"""One-shot historical pass. The provisional final m in the page-7
replacement was withdrawn by a subsequent audit row; the final source has n.
Do not rerun on the final tree.
"""
from pathlib import Path
from audit import change,block
f='08_expose_viii/components/03_seccion_2.tex'
s=(Path('work/sources')/f).read_text();old=s[s.index('A verificação de '):]
new=r'''A verificação de \SGARefLink{sga3:viii:proposition:2:1:item:a:01}{(a)}
a \SGARefLink{sga3:viii:proposition:2:1:item:d:01}{(d)} é
trivial, e deixada ao leitor. Provemos
\SGARefLink{sga3:viii:proposition:2:1:item:e:01}{(e)}.
Se \(G\) é suave sobre \(S\), é localmente de
apresentação finita sobre \(S\), logo de apresentação
finita sobre \(S\) pois é afim sobre \(S\), logo \(M\)
é de tipo finito. Logo pode-se já supor \(M\) de tipo
finito, logo \(G\) de apresentação finita sobre \(S\).
Então \(G\) é suave sobre \(S\) se e somente se suas
fibras geométricas o são, o que nos reduz ao caso em
que \(S\) é o espectro de um corpo algebricamente
fechado \(k\). Escrevendo \(M=T\times L\), com \(T\)
subgrupo de torção e \(L\) livre, \(L\simeq\mathbb Z^r\),
ter-se-á \(D(M)=D(T)\times D(L)\), onde
\(D(L)\simeq\mathbb G_m^r\) é suave sobre \(k\).
Logo \(G=D(M)\) é suave sobre \(k\) sse \(D(T)\) o é,
o que significa, pois \(D(T)\) é finito sobre \(k\) de
grau igual à ordem \(n\) de \(T\), que \(D(T)(k)\)
tem \(n\) elementos. Ora \(T\) é isomorfo a uma soma
de grupos \(\mathbb Z/n_i\mathbb Z\), sendo \(n\) o
produto dos \(n_i\), logo \(D(T)\) é produto dos
\(D(\mathbb Z/n_i\mathbb Z)=\mu_{n_i}\) (esquema em
grupos das raízes \(n_i\)-ésimas da unidade), logo
\[
 \operatorname{card}(D(T)(k))=\prod_i\operatorname{card}\mu_i(k)
\]
onde \(\operatorname{card}\mu_i(k)=(\text{número das raízes
\(n_i\)-ésimas da unidade em \(k\)})\leq n_i\), sendo
a igualdade atingida sse \(n_i\) é primo à característica
\(p\) de \(k\). Logo tem-se \(\operatorname{card}D(T)(k)=n\)
(\(n=\prod_i n_i\)) sse todos os \(n_i\) são primos a
\(p\), i.e. sse \(m\) é primo a \(p\), cqfd.
'''
change(f,7,old,new,'1970 restored','P. 7 directed rereading: original continuous proof with a single displayed cardinality formula; retain sss as sse, the parenthetical roots explanation, and printed final m (not n), enlarged at 6x. Remove expanded display structure and restore trivial/left-to-reader wording.')
f='08_expose_viii/components/05_seccion_4_parte_1.tex'
change(f,13,'como álgebras graduadas. Obtemos assim o resultado conhecido:', '(isomorfismo de álgebras graduadas). Recupera-se assim o resultado bem conhecido:','1970 restored','P. 13: parenthetical isomorphisme d’Algèbres graduées and On retrouve ainsi le résultat bien connu.')
block(f,13,r'''\textit{A categoria dos fibrados principais homogêneos''','Em particular:',r'''\textit{Há uma equivalência entre a categoria dos
fibrados principais homogêneos \(P\) sobre \(S\) de
grupo \(\mathbb G_{m,S}\), e a categoria dos módulos
invertíveis \(\mathscr L\) sobre \(S\), (tomando como
morfismos para definir uma e outra categoria os
isomorfismos para as estruturas em jogo). Obtêm-se
dois funtores quase inversos um do outro associando a
todo \(P\) a componente de grau 1 de sua álgebra afim
\(\mathbb Z\)-graduada, e associando a todo \(\mathscr L\)
o espectro da álgebra \(\mathbb Z\)-graduada
\(\coprod_{n\in\mathbb Z}\mathscr L^{\otimes n}\).}

''','1970 restored','P. 13, 4.3: restore Il y a une équivalence, parenthetical morphism convention, two quasi-inverse functors and inline final direct-sum algebra.')
change(f,13,r'''sobre \(S\), isto é, a}
\[
  H^1(S,\mathcal O_S^*).
\]''',r'''sobre \(S\), i.e. a \(H^1(S,\mathcal O_S^*)\).}''','1970 restored','P. 13, 4.4: i.e. and the H^1 formula are inline in the statement.')
change(f,13,'é localmente trivial para a topologia de Zariski.}', 'é localmente trivial (no sentido da topologia de Zariski).}','1970 restored','P. 13, 4.5: parenthetical au sens de la topologie de Zariski.')
change(f,14,r'''A necessidade é clara em virtude de
\SGARefLink{sga3:viii:proposition:4:1}{4.1}. Ficamos assim reduzidos a
demonstrar o \SGARefLink{sga3:viii:corollary:4:7}{corolário seguinte}.''',r'''Sendo a necessidade evidente, levando em conta
\SGARefLink{sga3:viii:proposition:4:1}{4.1}, vai-se reduzir
a provar o''','1970 restored','P. 14: La nécessité étant évidente ... on va se ramener à prouver le, directly introducing Corollaire 4.7.')
change(f,14,r'''\textit{Seja}
\[
  A=\coprod_{n\in\mathbb Z}A_n
\]
\textit{um anel \(\mathbb Z\)-graduado tal que}''',r'''\textit{Seja \(A=\coprod_{n\in\mathbb Z}A_n\) um anel
\(\mathbb Z\)-graduado, tal que}''','1970 restored','P. 14, 4.7: A=direct sum A_n is inline in the opening sentence.')
change(f,14,'reduzimo-nos (por localização','reduz-se (por localização','translation','P. 14: on est ramené, impersonal.')
f='08_expose_viii/components/06_seccion_4_continuacion.tex'
change(f,14,r'''Isto mostra que obtemos um isomorfismo
\[
  A_0[t,t^{-1}]\longrightarrow A
\]
de \(A_0\)-álgebras graduadas que envia \(t\) em \(f\), o que conclui a
demonstração de \SGARefLink{sga3:viii:corollary:4:7}{4.7}.''',r'''isso mostra que se obtém um isomorfismo
\(A_0[t,t^{-1}]\to A\) de \(A_0\)-álgebras graduadas
enviando \(t\) em \(f\), e conclui a demonstração de
\SGARefLink{sga3:viii:corollary:4:7}{4.7}.''','1970 restored','P. 14: continuous sentence after De plus, with inline polynomial-algebra isomorphism and impersonal l’on obtient.')
block(f,14,'No caso de',r'\SGARefTarget{sga3:viii:proposition:4:6:diagram:01}',r'''Sob as condições de
\SGARefLink{sga3:viii:proposition:4:6}{4.6},
\SGARefLink{sga3:viii:corollary:4:7}{4.7} já implica
que os \(\mathscr A_m\) (\(m\in M\)) são invertíveis.
Para provar a condição
\SGARefLink{sga3:viii:proposition:4:1:item:b:01}{4.1(b)},
pode-se portanto supor que \(\mathscr A_m,\mathscr A_{m'}\)
tenham bases \(f_m,f_{m'}\), com inversos
\(f_m^{-1}\in\Gamma(\mathscr A_{-m})\),
\(f_{m'}^{-1}\in\Gamma(\mathscr A_{-m'})\).
Então o produto por
\(f_m^{-1}f_{m'}^{-1}\in\Gamma(\mathscr A_{-m-m'})\)
define um homomorfismo
\(\mathscr A_{m+m'}\xrightarrow{\sim}\mathscr A_0
\simeq\mathcal O_S\), transformando a imagem de
\(f_m\otimes f_{m'}\) na seção 1 de \(\mathcal O_S\).
No diagrama
''','1970 restored','P. 14: restore inline local bases, inverse sections and homomorphism, original parentheses m in M and section 1 wording; retain the following printed diagram.')
f='08_expose_viii/components/07_seccion_5.tex'
change(f,15,'Podemos supor, portanto,','Pode-se então supor','translation','P. 15 proof 5.1: On peut alors supposer.')
change(f,17,'Devemos deduzir','É preciso deduzir','translation','P. 17: Il faut en conclure, impersonal.')
change(f,17,'redução, podemos supor','redução, pode-se supor','translation','P. 17: on peut supposer déjà.')
