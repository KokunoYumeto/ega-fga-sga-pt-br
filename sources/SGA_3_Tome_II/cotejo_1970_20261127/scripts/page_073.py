from audit import block,change
from pathlib import Path
f='09_expose_ix/components/08_seccion_7.tex'
block(f,73,r"levantamentos \(u,u'\), constroem-se",r'\medskip'+'\n'+r'\noindent\SGARefTarget{sga3:ix:remark:7:4}',r'''levantamentos \(u\) e \(u'\), para construir \(g\)
tal que \(u'=\operatorname{int}(g)u\), \(g_0=1\),
constroem-se sucessivamente \(g_n\), tais que \(g_0=1\),
\(g_n\) se deduz de \(g_{n+1}\) por redução,
\(u'_n=\operatorname{int}(g_n)u_n\); isso é possível
graças a \SGARefLink{sga3:ix:theorem:3:6}{3.6}. Como
\(A\) é separado e completo, os \(g_n\) provêm de um
\(g\in G(S)\) e para provar que \(u'=\operatorname{int}(g)u\),
basta utilizar a \emph{injetividade} na asserção
\SGARefLink{sga3:ix:theorem:7:1}{7.1}.

''','1970 restored','P. 73, end of 7.3: restore the requested g with g_0=1, both occurrences of that condition, inline induction data, and emphasis on injectivity; no added display or final square.')
s=(Path('work/sources')/f).read_text()
old=s[s.index(r'\textbf{Observação 7.4.}'):]
new=r'''\textbf{Observações 7.4.}
Comparar-se-á \SGARefLink{sga3:ix:theorem:7:1}{7.1}
com EGA III 5.4.1, que implica que o enunciado
\SGARefLink{sga3:ix:theorem:7:1}{7.1} é válido se,
em vez de supor \(H\) de tipo multiplicativo e \(G\)
afim, se supõe \(H\) próprio sobre \(S\), e \(G\)
separado e localmente de tipo finito sobre \(S\).
O fato de ter um enunciado como
\SGARefLink{sga3:ix:theorem:7:1}{7.1} \emph{sem hipótese
de propriedade} é bastante excepcional, e deve aqui
ser interpretado como um dos aspectos da grande
«\emph{rigidez}» da estrutura de um grupo de tipo
multiplicativo. O enunciado análogo com
\(G=H=\mathbf G_a\) (grupo aditivo) é falso em geral,
como se vê tomando \(A\) de característica \(p>0\), e
definindo os \(u_n\) por redução \(\bmod I^{n+1}\) a
partir de uma série formal aditiva
\SGARefTarget{sga3:ix:remark:7:4:display:01}
\[
  u(T)=\sum_{n\geq0}a_nT^{p^n},
\]
onde os \(a_n\) são elementos de \(A\) que tendem a 0
para a topologia \(I\)-ádica, mas não para a topologia
discreta. O enunciado
\SGARefLink{sga3:ix:theorem:7:1}{7.1} torna-se falso
igualmente se nele se suprime a hipótese \(G\) afim,
mesmo para \(H=\mathbf G_m\) (grupo multiplicativo);
vê-se um exemplo (com \(A\) anel de valoração discreta
completo) partindo de uma curva elíptica sobre o corpo
das frações \(K\) de \(A\), que se reduz (na teoria de
redução de Néron--Kodaira, digamos) segundo o grupo
\(\mathbf G_m\) sobre o corpo residual \(k\): ter-se-á,
portanto, um esquema em grupos comutativo suave \(G\)
sobre \(S\), cuja fibra especial é \(\mathbf G_{m,k}\),
(o que permite graças a
\SGARefLink{sga3:ix:theorem:3:6}{3.6} definir um sistema
projetivo de isomorfismos
\(u_n:H_n\xrightarrow{\sim}G_n\), onde
\(H=\mathbf G_{m,A}\)), mas cuja fibra genérica é uma
variedade abeliana, de modo que não existe outro
homomorfismo de \(S\)-grupos \(H\to G\) senão 0.
'''
change(f,73,old,new,'1970 restored','P. 73, Remarques 7.4: plural heading, roman continuous paragraph and selective emphasis; assez exceptionnel replaces the incorrect impossible en général reading. Restore quoted rigidity, additive/multiplicative parentheticals, original Néron–Kodaira parenthesis and inline isomorphisms. Lisse = suave; valuation = valoração.')
