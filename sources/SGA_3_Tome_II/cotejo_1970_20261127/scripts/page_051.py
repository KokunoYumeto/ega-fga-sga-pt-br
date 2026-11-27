from audit import change,block
f='09_expose_ix/components/04_seccion_4_parte_1.tex'
block(f,51,'inversa da diagonal em', '\n\\medskip\n\\noindent\\SGARefTarget{sga3:ix:lemma:4:2}',r'''inversa da diagonal de \(Y\times_S Y\) pelo \(S\)-morfismo
\(X\to Y\times_S Y\) definido por \((u,v)\); essa diagonal é um
subpré-esquema \emph{fechado} de \(Y\times_S Y\), portanto \(U'\)
é um subpré-esquema fechado de \(U\), que majora os \(Z^i\cap U\)
pela hipótese sobre \((u,v)\), portanto, se a família \((Z^i)\)
é esquematicamente densa, ter-se-á \(U'=U\), donde \(u=v\);
vê-se a implicação inversa tomando simplesmente
\(Y=\operatorname{Spec}\mathscr O_S[T]\)). Com a terminologia
introduzida em SGA I, fim do n.º 9.5, dizer que o subpré-esquema
\(Z\) de \(X\) é esquematicamente denso significa também que
\(X\) é idêntico ao \emph{subpré-esquema aderência de \(Z\) em \(X\)}.
''','1970 restored','The original proof prints X→Y×_S Y (not U→...), uses U′ and Z^i, closes its parenthesis after Spec O_S[T], and continues in the same paragraph. The reference literally reads SGA I fin du n°9.5, not EGA I. Retain those readings.')
block(f,51,r'\noindent\SGARefTarget{sga3:ix:lemma:4:2}', '\nPor hipótese, todos os',r'''\noindent\SGARefTarget{sga3:ix:lemma:4:2}\textbf{Lema 4.2.}
\textit{Seja \(X\) um \(S\)-pré-esquema plano, \((Z^i)_{i\in I}\)
uma família de subpré-esquemas de \(X\), planos sobre \(S\).
Seja \(S_0\) um subpré-esquema de \(S\), definido por um ideal
\(\mathscr J\) nilpotente, e sejam \(X_0,Z^i_0\) deduzidos por
mudança de base \(S_0\to S\), suponhamos enfim os módulos
\(\mathscr J^n/\mathscr J^{n+1}\) localmente livres sobre \(S_0\).
Se a família \((Z^i_0)_{i\in I}\) é esquematicamente densa em
\(X_0\), então a família \((Z^i)_{i\in I}\) o é em \(X\).}

Suponhamos \(\mathscr J^{n+1}=0\) (onde \(n\geq0\)), raciocinemos
por indução sobre \(n\), sendo a afirmação trivial para \(n=0\).
Definindo os \(S_m,X_m,Z^i_m\) por redução mod
\(\mathscr J^{m+1}\), como de costume, a hipótese de indução já
implica que \((Z^i_{n-1})_{i\in I}\) é esquematicamente densa em
\(X_{n-1}\). Substituindo, se necessário, \(X\) por um aberto
induzido, somos reduzidos a provar que toda seção \(f\) de
\(\mathscr O_X\) que se anula sobre os \(Z^i\) é nula. Ora, a
seção \(f_{n-1}\) de \(\mathscr O_{X_{n-1}}\) definida por \(f\)
se anula sobre os \(Z^i_{n-1}\), portanto é nula, portanto \(f\)
é uma seção de \(\mathscr J^n\mathscr O_X\). Como \(X\) é plano
sobre \(S\), tem-se
\SGARefTarget{sga3:ix:lemma:4:2:display:01}
\[
  \mathscr J^n\cdot\mathscr O_X
  \xleftarrow{\ \sim\ }
  \mathscr E\otimes_{\mathscr O_{S_0}}\mathscr O_{X_0},
  \qquad\text{onde }\mathscr E=\mathscr J^n/\mathscr J^{n+1}=\mathscr J^n.
\]
Do mesmo modo, para todo \(i\in I\), a restrição \(f_i\) de
\(f\) a \(Z^i\) pode ser considerada como uma seção de
\SGARefTarget{sga3:ix:lemma:4:2:display:02}
\[
  \mathscr J^n\cdot\mathscr O_{Z^i}
  \xleftarrow{\ \sim\ }
  \mathscr E\otimes_{\mathscr O_{S_0}}\mathscr O_{Z^i_0}.
\]
''','1970 restored','Lemma 4.2 and its proof consistently use superscript i on Z, and put the locally-free hypothesis after X_0,Z^i_0. The proof has no Demonstration heading or added quotient equality O_X/J^nO_X, and does not repeat a flatness premise before the second formula. Restored the continuous proof, nous sommes ramenés, both tensor formulas and the original order E=J^n/J^{n+1}=J^n.')
