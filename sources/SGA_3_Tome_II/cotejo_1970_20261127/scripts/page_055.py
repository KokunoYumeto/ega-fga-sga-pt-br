from audit import change,block
f='09_expose_ix/components/05_seccion_4_parte_2.tex'
block(f,55,'\\emph{Demonstração.}\nA implicação', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:corollary:4:6}',r'''O «é suficiente» é quase trivial pelas definições, e resulta do
simples fato de que \(k'\) é fielmente plano sobre \(k\) (com
exclusão de toda hipótese noetheriana ou outras). Provemos o «é
necessário». Considerando \(k'\) como limite indutivo de suas
subextensões de tipo finito \(k''\), e procedendo como no início da
demonstração precedente, reduz-se facilmente ao caso em que \(k'\)
é uma extensão de tipo finito de \(k\). (NB toda seção \(f''\)
de \(\mathscr O_{X''}\) tal que sua imagem inversa
\(f'\in\Gamma(X',\mathscr O_{X'})\) seja nula é nula). Então
\(k'\) é limite indutivo de suas subálgebras de tipo finito \(A\)
sobre \(k\), e reduz-se a ver que a família dos \(Z^i_A\) é
esquematicamente densa em \(X_A\). (NB toda seção de
\(\mathscr O_{X_A}\) tal que sua imagem inversa sobre \(X_{k'}\)
se anula sobre os \(Z^i_{k'}\) se anula sobre os \(Z^i_A\), pois,
para todo \(A\)-pré-esquema \emph{plano} \(Z\) --- tal como um
\(Z^i_A\) ---, toda seção de \(\mathscr O_Z\) nula sobre
\(Z_{k'}\) é nula, como se vê, por exemplo, reduzindo-se ao caso
em que \(Z\) é afim). Utilizando
\SGARefLink{sga3:ix:corollary:4:3}{4.3} para os \(X_{A'}\), onde
\(A'\) é um quociente de \(A\) por uma potência de um ideal
maximal, e o Nullstellensatz de Hilbert, reduz-se ao caso em que
\(k'\) é uma extensão finita de \(k\). Notemos que a hipótese
feita sobre \((Z^i)_{i\in I}\) significa também que a interseção
dos núcleos dos homomorfismos canônicos
\[
  u_i:\mathscr O_X\longrightarrow(v_i)_*(\mathscr O_{Z^i})
\]
é nula, onde \(v_i:Z^i\to X\) é a imersão canônica. Sob essa
forma, vê-se que\begingroup
\renewcommand{\thefootnote}{\(\ast\)}%
\footnote{É breve! Para uma demonstração, cf. EGA IV 11.10.6.}%
\addtocounter{footnote}{-1}%
\endgroup\ essa hipótese é estável por extensão \emph{finita}
\(k'/k\), o que conclui a demonstração.

Notemos de passagem o
\SGARefLink{sga3:ix:corollary:4:6}{resultado seguinte}, que servirá
em um exposé posterior:
''','re-edition removed','The entire proof of4.5 was replaced/expanded in the re-edition. Restored its original direct sufficiency argument, two parenthetical NB passages, reductions through finite-type subextensions/subalgebras and Hilbert Nullstellensatz, canonical-map display, and original star note C’est bref! cf.EGA IV11.10.6. Removed the added reference to4.5.0, two editorial notes, affine-cover/localization proof, EGA IV_3 11.9.10(b) substitution and final square.')
block(f,55,r'\noindent\SGARefTarget{sga3:ix:corollary:4:6}', '\n\\emph{Demonstração.}',r'''\noindent\SGARefTarget{sga3:ix:corollary:4:6}\textbf{Corolário 4.6.}
\textit{Sejam \(X\) um \(S\)-pré-esquema plano, \(U\) uma parte
aberta de \(X\), supõe-se que, para todo \(s\in S\), \(U_s\) é
esquematicamente denso em \(X_s\). Suponhamos além disso que \(X\)
é localmente noetheriano, ou \(X\) localmente de apresentação
finita sobre \(S\). Então \(U\) é esquematicamente denso em \(X\).}
''','translation','Corollary4.6 first gives the fibre-density assumption with On suppose, then a separate Supposons de plus sentence for the two finiteness alternatives; restored that order and register.')
