from audit import block,change,rows,write_rows
f='09_expose_ix/components/09_seccion_8_y_bibliografia.tex'
block(f,75,r'Seja \(N\) o subgrupo de \(M\)',r'\medskip'+'\n'+r'\noindent\SGARefTarget{sga3:ix:proposition:8:2}',r'''Essa relação pode também escrever-se
\[
 \chi_{m'-m}(g)=1\qquad\text{se }m,m'\in Z_i.
\]
Denotando por \(N\) o subgrupo de \(G\) gerado por
todos os \(m'-m\) (\(i\) variável, e, \(m,m'\in Z_i\)),
deduz-se da definição de \(D_k(M)\) (\(\simeq G\))
que \(H\) se identifica com \(D_k(M/N)\). Resulta então
de \SGARefLink{sga3:viii:theorem:3:1}{VIII 3.1} que
\(G/H\) se identifica com \(D_k(N)\), cqfd.

''','1970 restored','P. 75 begins with the equivalent character-difference relation (it belongs here, not to p. 74). Restore literal subgroup of G (not M), parenthetical index conditions and isomorphism, and cqfd.')
block(f,75,r'\textbf{Proposição 8.2.}',r'Para a demonstração de',r'''\textbf{Proposição 8.2.}
\SGARefTarget{sga3:ix:eq:8:2:0}%
\textit{Sejam \(G\) um grupo algébrico sobre um corpo
\(k\), extensão de um grupo de tipo multiplicativo
\(K\) por um grupo de tipo multiplicativo \(H\).
\SGARefTarget{sga3:ix:proposition:8:2:item:i}%
Se \(G\) é comutativo ou \(K\) conexo, então \(G\) é
de tipo multiplicativo.
\SGARefTarget{sga3:ix:proposition:8:2:item:ii}%
Se \(K\) e \(H\) são diagonalizáveis, sendo \(K\) um
toro, então \(G\) é diagonalizável.}

''','re-edition removed','P. 75, Proposition 8.2 is a single paragraph beginning Soient G un groupe algébrique. Remove editor footnote, explicit exact sequence and added finiteness hypotheses/parenthesis, and item (i)/(ii) structure; retain their invisible targets.')
block(f,75,'Para a demonstração de',r'e toda extensão de \(K\) por \(H\) já é diagonalizável.',r'''Para a demonstração da primeira asserção, o leitor
se reportará a
\SGARefLink{sga3:xvii:proposition:7:1:1}{XVII 7.1.1},
do qual \SGARefLink{sga3:ix:proposition:8:2}{8.2} é
um caso particular; o caso
\SGARefLink{sga3:ix:proposition:8:2}{8.2} é tratado
na parte (i) da demonstração de
\SGARefLink{sga3:xvii:proposition:7:1:1}{XVII 7.1.1}
(não utilizando os resultados dos exposés seguintes).
Suponhamos agora \(K\) e \(H\) diagonalizáveis:
\[
 K\simeq D_k(M),\quad H\simeq D_k(N),
\]
então pela definição
\SGARefLink{sga3:ix:definition:1:1}{1.1} e pelo sorites
de exatidão \SGARefLink{sga3:viii:theorem:3:1}{VIII 3.1},
vê-se que a classificação das extensões \(G\) de \(K\)
por \(H\), que sobre um fecho algébrico de \(k\) se
tornam isomorfas a uma extensão diagonalizável
\emph{dada} \(G_0\) de \(G\), é a mesma que a dos
torsores para fpqc sob o grupo
\(\underline{\operatorname{Hom}}(K,H)\), que é o
\(k\)-grupo constante de valor \(L=\operatorname{Hom}(N,M)\).
Se \(K\) é um toro i.e. \(M\) é sem torção, o mesmo
ocorre com \(L\), donde resulta
\SGARefTarget{sga3:ix:eq:8:2:1}%
\SGARefTarget{sga3:ix:eq:8:2:2}%
\SGARefTarget{sga3:ix:eq:8:2:3}%
\SGARefTarget{sga3:ix:eq:8:2:4}%
''','re-edition removed','P. 75: replace expanded proof by original single paragraph using definition 1.1 and VIII 3.1, algebraic closure and fpqc torsors. Printed given extension G_0 de G retained. Remove added X 1.4/isotrivial reduction, E/E_0, sequences (1)–(3), automorphism-functor discussion, source-error comments, separable closure/Gamma and cohomology formula. Invisible equation targets retained.')
rr=rows()
for r in rr:
 if r['printed_page']=='74' and 'extra equivalent character-difference formula' in r['evidence']:
  r['evidence']='P. 74 ends with a_im = 0 (equality, enlarged at 5x), not a_im nonzero. The following character-difference formula belongs to p. 75 and is restored in that page’s correction.'
  r['confidence']='amended; equality confirmed at second reading; deletion of following formula withdrawn upon reading p. 75 and formula restored there'
write_rows(rr)
