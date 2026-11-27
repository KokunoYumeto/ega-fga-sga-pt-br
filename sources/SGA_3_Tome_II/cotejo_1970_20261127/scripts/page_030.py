from audit import change,block
f='08_expose_viii/components/10_seccion_7_parte_1.tex'
change(f,30,'Segue-se que cada \\(Q_n\\) é finito e plano sobre \\(S_n\\).','Segue-se que cada \\(Q_n\\) é finito e plano sobre \\(S\\).','1970 restored','The first paragraph explicitly says les Q_n sont finis et plats sur S, without the subscript n.')
change(f,30,'livre finita como\n\\(V_n\\)-módulo.','livre de tipo finito como\n\\(V_n\\)-módulo.','translation','Original: un module libre de type fini sur cet anneau.')
change(f,30,'de maneira compatível também com os morfismos de comultiplicação.','isomorfismo que respeita também a aplicação diagonal.','1970 restored','The scan says isomorphisme respectant l’application diagonale également.')
change(f,30,r'\quad\text{é um módulo livre finito sobre}\quad',r'\quad\text{é um módulo livre de tipo finito sobre}\quad','translation','The inverse-limit module is described as libre de type fini.')
change(f,30,'e as comultiplicações dos \\(C_n\\) induzem uma sobre \\(C\\).','e as aplicações diagonais dos \\(C_n\\) definem uma aplicação diagonal de \\(C\\).','1970 restored','Original terminology: les applications diagonales des C_n définissent une application diagonale de C.')
change(f,30,r'''\textit{Seja \(K\) um corpo e seja \(Q\) um esquema em grupos finito sobre
\(K\), de grau \(n\). Então o morfismo potência \(n\)-ésima sobre
\(Q\) é nulo.}''',r'''\textit{Seja \(K\) um corpo e seja \(Q\) um esquema em grupos finito
comutativo sobre \(K\), de grau \(n\). Então \(n\cdot\operatorname{id}_Q=0\),
isto é, o morfismo de potência \(n\)-ésima em \(Q\) é nulo.}''','1970 restored','Lemma 7.3 explicitly assumes commutativity and states n·id_Q=0 before explaining the power morphism. The re-edition had removed both.')
change(f,30,'Veja-se VII\\(_A\\),','Cf. VII\\(_A\\),','translation','The one-line reference following Lemma 7.3 begins Cf.')
block(f,30,'O enunciado do Lema~', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:viii:corollary:7:4}',r'''O enunciado \SGARefLink{sga3:viii:lemma:7:3}{7.3} conserva um sentido
para um esquema em grupos \(Q/S\) finito e localmente livre sobre \(S\),
sendo \(S\) um pré-esquema de base qualquer e \(Q\) não necessariamente
comutativo (portanto, o morfismo de potência \(n\)-ésima em \(Q\) já não
é necessariamente um homomorfismo de grupos). Seria interessante encontrar
uma demonstração nesse caso geral.\begingroup
\renewcommand{\thefootnote}{(\(\ast\))}%
\footnote[0]{Cf. VII\(_A\) \SGARefLink{sga3:VIIA:8.5}{8.5} quando
\(S\) é o espectro de um corpo.}%
\endgroup
Note-se que \SGARefLink{sga3:viii:lemma:7:3}{7.3} prova, em todo caso,
que o enunciado considerado é verdadeiro se \(S\) é reduzido e \(Q\)
comutativo, como se vê aplicando \SGARefLink{sga3:viii:lemma:7:3}{7.3}
às fibras de \(Q\) nos pontos maximais (isto é, pontos genéricos das
componentes irredutíveis) de \(S\). Em particular, nas condições da
demonstração anterior, onde \(S\) é o espectro de um anel de valoração
discreta, encontra-se \(n\cdot\operatorname{id}_Q=0\). Aliás, aqui
\(n\) é uma potência \(p^{\nu_0}\) da característica residual, e obtemos o
''','1970 restored','Remark 7.3.1 retains the noncommutative caveat and the note that a power map need not be a group homomorphism. Restored original footnote (*), the hypothesis Q commutative with S reduced, and the original transition to Corollary 7.4. Removed the added parenthesis equating 7.3 to VII_A 8.5.')
