from audit import *
f='08_expose_viii/components/04_seccion_3.tex'
block(f,8,r'\begin{enumerate}', 'A primeira afirmação de',r'''\SGARefTarget{sga3:viii:theorem:3:1:item:i:01}
\SGARefTarget{sga3:viii:theorem:3:1:item:ii:01}
\textit{Então \(v'\) induz um isomorfismo de \(D_S(M'')\) sobre o núcleo de
\(u'\), e \(u'\) é fielmente plano e quase-compacto.}

''','re-edition removed','P. 8: Teorema 3.1 tem uma única conclusão, sem itens (i)/(ii); não imprime a afirmação sobre feixe quociente fpqc nem sua prova por M-efetividade.')
change(f,8,r'''A primeira afirmação de
\SGARefLink{sga3:viii:theorem:3:1:item:i:01}{(i)} é uma consequência
imediata da definição dos funtores \(D_S(-)\).''',r'''A primeira afirmação é uma consequência trivial da definição dos
funtores \(D_S(M'')\) etc.''','1970 restored','P. 8: a primeira afirmação não remete a item (i); o argumento cita D_S(M′′) etc., não D_S(-).')
change(f,8,r'''A segunda afirmação de
\SGARefLink{sga3:viii:theorem:3:1:item:i:01}{(i)} deduzir-se-á, portanto,''',r'''A última afirmação de
\SGARefLink{sga3:viii:theorem:3:1}{3.1} resultará, portanto,''','1970 restored','P. 8: a conclusão do parágrafo diz la dernière assertion de 3.1, sem subdivisão editorial.')
s=(ROOT/'sources'/f).read_text();a=s.index('\\SGARefTarget{sga3:viii:theorem:3:1:diagram:02}');b=s.index('Para demonstrar',a);old=s[a:b]
new=old.replace('v^t',"v'").replace('u^t',"u'").replace('quase compacto','quase-compacto')
change(f,8,old,new,'reading','P. 8: transpostos são v′ e u′, com apóstrofo, tanto na sequência quanto em 3.2; restauração da notação de 1970. Grafia quase-compacto conforme padrão.')
