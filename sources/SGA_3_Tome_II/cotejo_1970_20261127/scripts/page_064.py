from audit import block
f='09_expose_ix/components/07_seccion_6.tex'
block(f,64,'\\emph{Demonstração.}\nSe \\(S\\) é o espectro', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:lemma:6:2}',r'''Quando \(S\) é o espectro de um corpo \(k\), isso foi visto
em VII\(_B\) 8.5, basta tomar \(n=\deg[K:k(s)]\).
Suponhamos agora \(S\) local artiniano, seja
\(n_0=\deg[K_0:k]\), onde \(k\) é o corpo residual e
\(K_0=K\otimes_Ak\), \(S=\operatorname{Spec}(A)\), e
distinguamos dois casos.
\SGARefTarget{sga3:ix:lemma:6:1:proof:item:a}a) \(k\) é de
car. nula, logo \(K_0\) é separável sobre \(k\), logo \(K\)
é não ramificado sobre \(S\). Então a seção unidade de \(K\)
é uma imersão aberta, logo
\({}_nK=\operatorname{Ker}n.\operatorname{id}_K\) é um
subesquema aberto de \(K\), logo para que seja igual a \(K\),
basta que o seja como conjunto, pode-se portanto então tomar
\(n=n_0\).
\SGARefTarget{sga3:ix:lemma:6:1:proof:item:b}b) \(k\) é de
car. \(p>0\), seja então \(m\) um inteiro tal que
\(\mathfrak m^{m+1}=0\), onde \(\mathfrak m\) é o ideal
maximal de \(A\), afirmo que se pode tomar \(n=p^mn_0\).
Com efeito, procedendo por indução sobre \(m\), pode-se supor
que, pondo \(n'=p^{m-1}n_0\), \(n'\operatorname{id}_K\)
induz em \(K_{m-1}=K\otimes_A(A/\mathfrak m^m)\) o
endomorfismo nulo. O conjunto dos endomorfismos \(u\) de
\(K\) que têm essa propriedade está em correspondência
biunívoca com \(H^1(K,M)\), onde \(M\) é o funtor em grupos
sobre \(S\) definido por
\SGARefTarget{sga3:ix:lemma:6:1:display:01}%
\(T\mapsto\operatorname{Hom}_{\mathscr O_{T_0}}
(g_0^*(\Omega^1_{K_0/S_0}),\mathfrak m^m\mathscr O_T)\),
(\(g:T\to S\) denotando a projeção estrutural e
\(g_0:T_0\to S_0\) a projeção deduzida pela mudança de base
\(S_0\to S\)), (cf. III 2). Verifica-se que essa
correspondência biunívoca respeita as leis de grupo, o que
implica que os endomorfismos \(u\) considerados são tais
que \(pu=0\). Logo tem-se \(pn'\operatorname{id}_K=0\),
i.e. \(p^mn_0\operatorname{id}_K=0\).

Suponhamos agora \(S\) noetheriano (reduz-se a isso em
\SGARefLink{sga3:ix:lemma:6:1}{6.1} pela redução habitual ao
caso noetheriano). Basta então conjugar o que precede e o
''','re-edition removed','Printed64 consistently uses K, cites VII_B8.5, gives n=deg[K:k(s)], and directly states a bijection with H^1(K,M) and the Hom formula, referring simply to III2. Restored the original one-paragraph(a)/(b), first-person singular je dis, and following parenthetical reduction. Removed all added E/K kernel functor, III0.1.2/0.9 references, editor note, separate displays and S_r construction.')
block(f,64,r'\noindent\SGARefTarget{sga3:ix:lemma:6:2}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:lemma:6:2}\textbf{Lema 6.2.}
\textit{Seja \(X\) um pré-esquema quase-finito acima de \(S\)
noetheriano, e consideremos uma família filtrante crescente
de subpré-esquemas \((X^i)_{i\in I}\), tendo a propriedade
seguinte: para todo \(s\in S\) e todo inteiro \(n\geq0\),
pondo \(S'=\operatorname{Spec}
(\mathscr O_{S,s}/\mathfrak m^{n+1})\) e denotando por
\(X',X'{}^i\) os pré-esquemas deduzidos de \(X,X^i\) pela
mudança de base \(S'\to S\), existe um \(i\in I\) tal que
\(X'{}^i=X'\). Sob essas condições, existe um \(i\in I\),
tal que \(X^i=X\).}
''','1970 restored','Original6.2 uses superscripts X^i, the base change S-prime with X-prime/X-prime-i, and one continuous paragraph. Removed the displayed brace construction, renamed S_{s,n}, lower indices, and substitute tensor equations.')
