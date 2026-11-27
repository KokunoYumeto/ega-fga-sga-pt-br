from audit import block
f='09_expose_ix/components/07_seccion_6.tex'
block(f,65,'\\emph{Demonstração.}\nComo \\(S\\) é noetheriano', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:lemma:6:3}',r'''Como \(S\) é noetheriano, existe um aberto \(U\)
\emph{maximal} tal que se tenha \(X|U=X^i|U\) para \(i\)
grande, vai-se mostrar que \(U=S\). Em outros termos,
vai-se mostrar que se \(U/S\), pode-se encontrar um \(U'\)
estritamente maior que \(U\), e um \(i\) tal que
\(X|U'=X^i|U'\). Localizando em um ponto \emph{maximal}
\(s\) de \(S-U\), reduz-se ao caso em que \(S\) é local
de ponto fechado \(s\), e \(U=X-\{s\}\). (NB se
\(S'=\operatorname{Spec}(\mathscr O_{S,s})\) e se \(i\)
é tal que \(X\times_SS'=X^i\times_SS'\), então existe
uma vizinhança aberta \(V\) de \(s\) tal que \(X|V=X^i|V\),
logo, com a condição de tomar \(i\) suficientemente grande,
ter-se-á \(X|W=X^i|W\), onde \(W=U\cup V\)). Como
\(X|U=X_i|U\) para \(i\) grande, vê-se que \(X_i\) é um
subpré-esquema fechado de \(X\) definido por um Ideal
\(\mathscr I^{(i)}\) de suporte contido em
\(X_0=X\times_SS_0\) (onde
\(S_n=\operatorname{Spec}(A/\mathfrak m^{n+1})\),
\(S=\operatorname{Spec}(A)\)). Como \(X_0\) é quase-finito
sobre \(S\), \(X_0\) é uma parte fechada finita de \(X\)
noetheriano, logo \(\mathscr I^{(i)}\) é um Módulo
\emph{de comprimento finito}. Segue-se que existe um inteiro
\(n\geq0\) tal que
\(\mathscr I^{(i)}\cap\mathfrak m^{n+1}\mathscr O_X=0\).
Aliás, em virtude da hipótese em
\SGARefLink{sga3:ix:lemma:6:2}{6.2}, pode-se supor (com a
condição de aumentar \(i\)) que a imagem de
\(\mathscr I^{(i)}\) em
\(\mathscr O_{X_n}=\mathscr O_X/\mathfrak m^{n+1}\mathscr O_X\)
é nula. Isso implica \(\mathscr I^{(i)}=0\), logo \(X^i=X\),
cqfd.
''','1970 restored','Printed65 has one paragraph, NB parenthesis, inline formulas, mixed X^i then X_i and final X^i, emphases on maximal and finite length, and literal cqfd. A 5x crop shows U/S (a slash without equality strokes) and U=X-{s}, both preserved. Original says X_0 quasi-finite over S, not S_0. Removed the restructured displayed proof.')
block(f,65,r'\noindent\SGARefTarget{sga3:ix:lemma:6:3}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:lemma:6:3}\textbf{Lema 6.3.}
\textit{Sejam \(S\) um pré-esquema, \(K\) um pré-esquema em
grupos sobre \(S\), localmente de apresentação finita,
\(s\in S\) tal que \(K_s\) seja quase-finito (resp. não
ramificado) sobre \(k(s)\) no elemento unidade. Então existe
uma vizinhança aberta \(U\) de \(s\) tal que \(K|U\) seja
localmente quase-finito (resp. não ramificado) sobre \(U\).}%
\begingroup
\renewcommand{\thefootnote}{\(\ast\)}%
\footnote{Cf.\ VI\textsubscript{B}
\SGARefLink{concl:sga3-VIB-2.5-ii}{2.5(ii)} para um enunciado mais geral.}%
\addtocounter{footnote}{-1}%
\endgroup
''','translation','Original6.3 uses one Soient list with s satisfying the condition, k(s), resp. and baseline restriction K|U. The original star note VI_B2.5(ii) is preserved.')
block(f,65,'\\emph{Demonstração.}\nSeja \\(V\\)', '\\(\\kappa(t)\\), porque tem essa',r'''Seja com efeito \(V\) o conjunto dos pontos \(x\) de
\(K\) tais que \(K_s\) seja quase-finito (resp. não
ramificado) sobre \(k(s)\) em \(x\), i.e. tal que \(x\)
seja isolado em \(K_s\) (resp. e seu anel local em \(K_s\)
uma extensão separável de \(k(s)\)), --- onde \(s\) denota
a imagem de \(x\) em \(S\). Sabe-se que \(V\) é aberto,
pois \(K\) é localmente de apresentação finita sobre \(S\),
logo se \(g\) denota a seção unidade de \(K\), \(g^{-1}(V)\)
é aberto. Por hipótese contém \(s\), logo é uma vizinhança
aberta \(U\) de \(s\). Esta serve, em outros termos \(t\in U\)
implica que \(K_t\) é localmente quase-finito (resp. não
ramificado) sobre \(k(t)\): com efeito, como \(K_t\) é um
grupo localmente de tipo finito sobre
''','1970 restored','Proof6.3 uses s for the image of x and g for the unit section, k(s)/k(t), resp. and the original clause order. Removed proof heading and expanded repeated isolation condition. The page ends after local finite type over.')
