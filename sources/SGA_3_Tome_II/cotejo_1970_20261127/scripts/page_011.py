from audit import *
f='08_expose_viii/components/05_seccion_4_parte_1.tex'
block(f,11,'% Tradução brasileira revista','\\SGARefTarget{sga3:viii:section:4}', '% SGA 3, Exposé VIII, tradução brasileira: §4.\n% Autoridade: LNM 152 (1970), pp. 11--14.\n\n','structure','Comentário de autoridade atualizado para LNM 152, pp. 11–14.')
change(f,11,r'''Determinaremos os
\(G\)-torsores (ou fibrados principais homogêneos sob \(G\)) sobre \(S\)
para a topologia fielmente plana e quase compacta; cf. Exposé IV,
\SGARefLink{sga3:iv:subsection:5:1}{5.1}.''',r'''Propomo-nos determinar os \emph{torsores} (ou \emph{fibrados principais
homogêneos}) sobre \(S\), no sentido da «topologia fielmente plana
quase-compacta», cf. Exposé~IV.''','re-edition removed','P. 11, abertura: retirada a localização IV 5.1, ausente; restaurada a formulação e ênfase da primeira frase.')
change(f,11,'com grupo de operadores \\(S\\)-grupal \\(G\\)','com grupo de operadores \\(G\\)','translation','P. 11: à groupes d’opérateurs G, sem a expressão S-grupal.')
change(f,11,r'''quase compacto sobre \(S\) (cf. IV,
\SGARefLink{sga3:iv:proposition:5:1:6}{5.1.6}).''',r'''quase-compacto sobre \(S\) (cf. IV).''','re-edition removed','P. 11: cf. IV sem referência numerada 5.1.6.')
change(f,11,r'''(\SGARefLink{sga3:i:proposition:4-7-3}{Exposé I, 4.7.3})''',r'''(Exposé~I)''','re-edition removed','P. 11: a referência ao caso afim é somente Exp. I.')
s=(ROOT/'sources'/f).read_text();a=s.index('\\SGARefTarget{sga3:viii:section:4:problem:01}');b=s.index('\\medskip',a);old=s[a:b]
change(f,11,old,old.replace('quase compacto','quase-compacto').replace('\\subseteq','\\subset'),'reading','P. 11: a multiplicação usa o sinal de inclusão simples; normalizada a grafia de quasi-compact segundo o padrão anexo.')
