from audit import *
f='08_expose_viii/components/05_seccion_4_parte_1.tex'
change(f,14,r'''A necessidade é clara em virtude de
\SGARefLink{sga3:viii:corollary:4:2}{4.2}.''',r'''A necessidade é clara em virtude de
\SGARefLink{sga3:viii:proposition:4:1}{4.1}.''','1970 restored','P. 14, passagem de 4.6 a 4.7 imprime 4.1; preservada a referência de 1970 em lugar da correção editorial para 4.2.')
block(f,14,r'''  \makebox[\displaywidth][s]{%''', '\\]\nComo a afirmação',r'''  \sum_i f_ig_i=1.
''','re-edition removed','P. 14: a soma não recebe marca (*); removida a etiqueta acrescentada, mantendo o alvo interno.')
block(f,14,'Como a afirmação a demonstrar', 'Além disso,',r'''Como a conclusão a estabelecer é local sobre \(\operatorname{Spec}(A_0)\),
reduzimo-nos (por localização com o auxílio dos \(f_i\)) ao caso em que
existe \(f\in A_1\), elemento \emph{invertível} de \(A_1\). Então, para
todo \(n\in\mathbb Z\), \(f^n\) é um elemento invertível de \(A_n\),
logo define um isomorfismo \(h\mapsto f^nh\) de \(A_0\) sobre \(A_n\).
''','1970 restored','P. 14: localização pelos f_i e elemento invertível de A_1 são as leituras impressas, inclusive suas dificuldades. Retirados a nota e o argumento ampliado pelos D(f_i g_i).')
f='08_expose_viii/components/06_seccion_4_continuacion.tex'
block(f,14,'% Tradução brasileira revista','Isto mostra', '% SGA 3, Exposé VIII, tradução brasileira: continuação de §4.\n% Autoridade: LNM 152 (1970), p. 14.\n\n','structure','Comentário de autoridade referido à página 14 da impressão de 1970.')
change(f,14,'de álgebras \\(A_0\\)-graduadas','de \\(A_0\\)-álgebras graduadas','translation','P. 14: A_0-algèbres graduées, não álgebras graduadas pelo objeto A_0.')
change(f,14,r'\qquad\text{y}\qquad',r'\qquad\text{e}\qquad','translation','P. 14: corrigida conjunção espanhola residual na tradução portuguesa.')
change(f,14,r'''  \mathscr A_{m+m'}\longrightarrow
  \mathscr A_0\simeq\mathcal O_S''',r'''  \mathscr A_{m+m'}\xrightarrow{\ \sim\ }
  \mathscr A_0\simeq\mathcal O_S''','reading','P. 14, homomorfismo antes do diagrama: a primeira seta também recebe sinal de isomorfismo.')
change(f,14,r'isomorfismo. \hfill\(\square\)',r'isomorfismo, c.q.d.','1970 restored','P. 14 termina com cqfd., não quadrado.')
