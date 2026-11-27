from audit import change,block
f='09_expose_ix/components/05_seccion_4_parte_2.tex'
block(f,56,'\\emph{Demonstração.}\nPara simplificar', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:theorem:4:7}',r'''Suponhamos para simplificar (U) retrocompacto em (X) (cf.
EGA IV 11.10.10 para o caso geral). O caso (X) localmente
noetheriano só é incluído para memória, está contido em
\SGARefLink{sga3:ix:corollary:4:3}{4.3}. No segundo caso
considerado, pode-se evidentemente supor (S) e (X) afins,
então (X) e (U) são de apresentação finita sobre
(S=\operatorname{Spec}(A)). (A) é limite indutivo de suas
sub-(\mathbb Z)-álgebras (A_i) de tipo finito. O
«procedimento patenteado» já utilizado (explicitado longamente em
EGA IV 8) mostra que existe um (i), um esquema afim (X_i)
sobre (S_i=\operatorname{Spec}(A_i)) e um aberto (U_i) em
(X_i), dos quais (X,U) se deduzem por mudança de base
(S\to S_i). Seja (E_i) a parte de (S_i) formada pelos
(s\in S_i) tais que (U_{i,s}) seja esquematicamente denso
em (X_{i,s}). Essa condição significa também que (U_{i,s})
contém o conjunto (\operatorname{Ass}\mathscr O_{X_{j,s}})
dos pontos «associados» ao feixe estrutural de (X_{i,s}), e
os resultados de EGA IV 9 mostram então que essa condição é de
natureza construtível, i.e. que (E_i) é uma parte construtível
de (S_i). Aliás, a condição considerada nas fibras é invariante
por extensão do corpo de base, o que prova em virtude da hipótese
feita que a imagem inversa (E) de (E_i) por (S\to S_i)
é (S), e implica por EGA IV 8 que existe um (j\geq i) tal
que a imagem inversa (E_j) de (E_i) em (S_j) seja (S_j),
i.e. que para todo (s\in S_j), (U_{j,s}) seja
esquematicamente denso em (X_{j,s}). Em virtude de
\SGARefLink{sga3:ix:lemma:4:4}{4.4} aplicado a
((S_j,X_j,U_j)) e à mudança de base (S\to S_j), segue-se
que (U) é esquematicamente denso em (X). Note-se aliás que
só se utiliza aqui \SGARefLink{sga3:ix:lemma:4:4}{4.4} no caso
de uma família cujo conjunto de índices é finito (de fato,
reduzido a um elemento), caso em que a demonstração de
\SGARefLink{sga3:ix:lemma:4:4}{4.4} se simplifica muito, como o
leitor constatará por si mesmo.
\label{fnref:IX-24}
''','re-edition removed','Printed p.56 has one continuous proof of4.6, no proof heading or square, EGA IV11.10.10/8/9 only, no explicit4.5 reference and no editorial note or expanded constructive argument. Restored quotation marks, original final reader remark and the literal subscript j in Ass O_{X_{j s}}, followed by X_{i s}. A 5x crop verifies that j; the original note label is retained invisibly.')
block(f,56,r'\noindent\SGARefTarget{sga3:ix:theorem:4:7}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:theorem:4:7}\textbf{Teorema 4.7.}
\textit{Sejam (S) um pré-esquema, (G) um grupo de tipo
multiplicativo e de tipo finito sobre (S). Para todo inteiro
(n>0), seja ({}_nG) o núcleo de (n\operatorname{id}_G).
Então a família dos subpré-esquemas (({}_nG)_{n>0}) de (G)
é esquematicamente densa (def.
\SGARefLink{sga3:ix:definition:4:1}{4.1}).}
''','translation','Theorem4.7 uses a Soient list, n id_G without dot, and ends with parenthetic (déf.4.1). Restored the original sentence structure.')
block(f,56,'\\emph{Demonstração.}\nDistinguimos dois casos.', 'Então,\n\\[\n  M\\simeq',r'''Distinguimos dois casos.
\SGARefTarget{sga3:ix:theorem:4:7:proof:item:a}a) Caso (S)
localmente noetheriano. Então por
\SGARefLink{sga3:ix:corollary:4:3}{4.3} reduz-se ao caso em
que (S) é o espectro de um corpo (k), e, fazendo uma extensão
deste, ao caso (k) algebricamente fechado e (G)
diagonalizável, i.e. da forma (D_k(M)), onde (M) é um grupo
comutativo de tipo finito. ''','re-edition removed','Original4.7 proof begins continuously Nous distinguons deux cas. a) Cas...; no separate proof heading or italic subheading and no4.5.0 reference. D_k(M) is inline; On est ramené is impersonal. Removed the added G=D_k(M) display.')
