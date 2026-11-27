from audit import *
f='08_expose_viii/components/05_seccion_4_parte_1.tex'
change(f,12,'é fielmente plano sobre \\(S\\); de qualquer modo, é quase compacto sobre \\(S\\),','é fielmente plano sobre \\(S\\); de qualquer modo, é quase-compacto sobre \\(S\\),','translation','P. 12, prova de 4.1: quasi-compact, grafia do padrão.')
change(f,12,'Em termos de álgebras graduadas,','Sobre as álgebras afins,','translation','P. 12 imprime sur les Algèbres affines; graduadas não corresponde a affines.')
change(f,12,r'''  \mathscr A\otimes\mathscr A
  \longrightarrow
  \mathscr A(M)=\mathscr A\otimes\mathcal O_S(M).''',r'''  \mathscr A\otimes\mathcal O_S(M)=\mathscr A(M)
  \longleftarrow\mathscr A\otimes\mathscr A.''','reading','P. 12: a fórmula está ordenada A tensor O_S(M)=A(M) ← A tensor A; verificada a direção e os fatores.')
change(f,12,'o que mostra que\n\\SGARefLink{sga3:viii:proposition:4:1:item:b:01}', 'que é um isomorfismo. Isso mostra que\n\\SGARefLink{sga3:viii:proposition:4:1:item:b:01}','1970 restored','P. 12, após (m,n) ↦ (m+n,n): estava omitida a oração qui est un isomorphisme.')
