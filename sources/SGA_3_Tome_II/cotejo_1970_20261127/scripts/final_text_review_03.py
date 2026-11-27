"""One-shot history of directed final rereading; run only on its recorded predecessor."""
from audit import change, block
f='08_expose_viii/components/08_seccion_6_parte_1.tex'
change(f,21,'e temos evidentemente','e tem-se evidentemente','translation','LNM 152 p.21: on a évidemment, impersonal.')
change(f,21,'Podemos, portanto, supor','Pode-se, portanto, supor','translation','LNM 152 p.21: On peut donc supposer.')
change(f,21,'são de descida efetiva','são de \\emph{descida efetiva}','1970 restored','LNM 152 p.21 underlines descente effective.')
f='08_expose_viii/components/10_seccion_7_parte_1.tex'
block(f,26,'Notemos primeiro que podemos supor','Sejam \\(s\\) e \\(s\'\\)',
r'''Notemos primeiro que se pode supor \(S\) afim, e (graças à
hipótese de apresentação finita sobre \(G\) e \(H\), que permite
reduzir-se ao caso do espectro de um anel de tipo finito sobre
\(\mathbf Z\)) \(S\) noetheriano. Então \(G\) e \(H\) são noetherianos.
Dizer que \(u:G\to H\) é uma imersão (resp. uma imersão fechada)
equivale então a dizer que \(u\) é um monomorfismo (o que é verdadeiro
por hipótese) e que \(u\) é próprio em todo ponto de \(u(G)\)
(resp. que \(u\) é próprio). O critério valuativo da propriedade de ser
próprio nos assegura que basta verificar que, para toda mudança de
base \(S'\to S\), com \(S'\) o espectro de um anel de valoração
discreta, completo se se quiser, o morfismo \(u':G'\to H'\) tem a
mesma propriedade de ser próprio. (O caso da propriedade local foi
esquecido em EGA~II 7, e figurará como retificação em EGA~IV\begingroup
\renewcommand{\thefootnote}{(\(\ast\))}%
\footnote[0]{Cf. EGA~IV 15.7.1.}%
\endgroup).
Isso nos reduz, portanto, ao caso em que \emph{o próprio \(S\) é o
espectro de um anel de valoração discreta completo}, sob a ressalva
de que as hipóteses adicionais sobre \(G,H,u\) que seríamos levados
a formular sejam estáveis por mudança de base.

''','1970 restored','LNM 152 pp.26–27: restore the single opening sentence with its parenthetical reduction, the criterion in the same paragraph, the parenthetical remords and the emphasis on the complete valuation-ring spectrum.')
change(f,27,r'''\(G_{s'}\) com um subesquema fechado de \(H_{s'}\). Utilizaremos o
\SGARefLink{sga3:viii:lemma:7:1}{resultado seguinte}.''',r'''\(G_{s'}\) com um subesquema fechado de \(H_{s'}\). Ora, tem-se o
\SGARefLink{sga3:viii:lemma:7:1}{resultado seguinte}:''','translation','LNM 152 p.27: Or on a le résultat suivant :')
block(f,28,'Apliquemos isso ao par','Notemos primeiro que, como',
r'''Aplicando isso à situação \(H,G_{s'}\), vê-se que o monomorfismo
\(u:G\to H\) se fatora em \(G\to L\to H\), onde \(L\) é um
subgrupo de \(H\) que é um subpré-esquema fechado, \emph{plano sobre
\(S\)}, e onde \(G\to L\) induz um isomorfismo nas fibras genéricas.
Então \(u:G\to H\) é uma imersão (resp. uma imersão fechada) sse
\(u':G\to L\) o é. Isso nos reduz, portanto, ao caso em que
\emph{\(H\) é plano sobre \(S\) e \(u_{s'}:G_{s'}\to H_{s'}\) é um
isomorfismo}, (sob a ressalva de que as hipóteses adicionais que
teríamos de formular sobre \(G,H,u\) sejam respeitadas quando se
substitui \(H\) por um subpré-esquema em grupos fechado). Como então
\(H\) é o fecho esquemático de \(H_{s'}\), se \(u\) é uma imersão,
então \(u(G)\) será um subpré-esquema fechado de \(H\) que contém
\(H_{s'}\), logo seu fecho esquemático é também \(H\), e, por
conseguinte, \(u(G)\) é um aberto induzido em \(H\). Por conseguinte,
deveremos provar de fato que \(u\) é uma imersão \emph{aberta},
(resp. um \emph{isomorfismo} se quiséssemos estabelecer que \(u\)
é uma imersão fechada). Como \(G\) e \(H\) são planos sobre \(S\),
equivale a dizer que os morfismos induzidos nas fibras são imersões
abertas, resp. isomorfismos (cf. SGA~1 I
\SGARefLink{sga1:i:5:7}{5.7}), e, como isso já se verifica para
\(u_{s'}\), \emph{reduz-se a provar que \(u_s\) é uma imersão
aberta, resp. um isomorfismo}.

''','1970 restored','LNM 152 p.28: continuous paragraph, inline G→L→H, original parenthetical reservations and resp. clause, nous devrons prouver en fait and underlined conclusions; retains the printed fermé.')
change(f,28,'(Reduzimo-nos ao caso','(Reduz-se ao caso','translation','LNM 152 p.28: (On est ramené au cas ...).')
block(f,29,r'''Substituindo \(H\) por \(H'\), podemos''','\\medskip\n\\noindent\\SGARefTarget{sga3:viii:proposition:7:2}',
r'''Portanto, substituindo \(H\) por \(H'\), pode-se, para provar que
\(u\) é uma imersão, reduzir-se (com a ressalva habitual) ao caso em
que, além das hipóteses anteriores, se supõe \(u\) \emph{bijetivo},
i.e. \(u_s:G_s\to H_s\) \emph{bijetivo}. Reduz-se, portanto, em
todos os casos, a provar que \(u\), ou ainda \(u_s\), é um
isomorfismo, mediante, se for o caso, a hipótese de bijetividade.

Suponhamos então primeiro que \(u\) seja bijetivo. Se \(H_s\) é
\emph{reduzido}, pode-se evidentemente concluir que \(u_s\) é um
isomorfismo, pois \(G_s\) se identifica com um subesquema fechado de
\(H_s\) com o mesmo conjunto subjacente. Em particular, se \(k=k(s)\)
é de característica zero, todo grupo algébrico sobre \(k\) é
reduzido segundo \emph{Cartier} (VII\(_B\) 3.3.1, ou EGA~IV
16.12.2 e 17.12.5) e assim se obteve:

''','1970 restored','LNM 152 p.29: restore on peut/on est ramené, parenthetical reserve, explicit hypotheses, underlined bijectif/réduit/Cartier and the original conclusion.')
change(f,30,'da característica residual, e obtemos o','da característica residual, e obtém-se o','translation','LNM 152 p.30: et on trouve le.')
f='08_expose_viii/components/11_seccion_7_parte_2_y_bibliografia.tex'
change(f,31,'(SGA IV 5.9). Podemos,\nportanto, tomar','(SGA IV 5.9). Pode-se,\nportanto, supor','translation','LNM 152 p.31: donc on peut supposer que n=0.')
f='09_expose_ix/components/06_seccion_5.tex'
change(f,59,r'''\textit{Seja \(u:H\to G\) um homomorfismo''',r'''\textit{Sejam \(u:H\to G\) um homomorfismo''','reading','LNM 152 p.59 Corollaire 5.2 prints Soient before the single homomorphism; preserve the plural printed form.')
