from audit import change, block, ROOT
f='08_expose_viii/components/08_seccion_6_parte_1.tex'
change(f,20,'% Tradução brasileira revista a partir do workpass espanhol congelado;\n% a fonte permanece em source_es.\n','', 're-edition removed','The source comments are not part of the 1970 text.')
change(f,20,'% Autoridade: Polo--Gille Exp8-8nov09.pdf; edição original: LNM 152, pp. 20--23.','% Autoridade: LNM 152 (1970), pp. 20--23.', 'structure','Authority is the supplied 1970 scan, printed pages 20–23.')
change(f,20,'independentemente da teoria de grupos diagonalizáveis; seu local natural\nestaria no Exposé VI','independente da teoria dos grupos diagonalizáveis; seu lugar natural\nseria em VI','translation','Footnote (*): indépendant de la théorie des groupes diagonalisables; sa place naturelle serait dans VI_B.')
change(f,20,'recobrimento aberto afim','cobertura aberta afim','translation','Definition 6.1: recouvrement, covered by the supplied terminology standard.')
change(f,20,r"e um recobrimento \((X'_{ij})_j\)",r"e uma cobertura \((X'_{ij})_j\)",'translation','Definition 6.1: recouvrement by affine opens.')
change(f,20,'quase compacto.','quase-compacto.','translation','6.2(c): quasi-compact; standard Portuguese form.')
start='\\footnote{Nota do\neditor: de fato, seja'
end='\n\n\\medskip\n\\noindent\\SGARefTarget{sga3:viii:proposition:6:3}'
block(f,20,start,end,'','re-edition removed','After the one-sentence proof of 6.2, the scan immediately begins Proposition 6.3; it has no proof of freeness over an Artinian local ring.')
change(f,20,'quase compacta conveniente','quase-compacta conveniente','translation','6.3: quasi-compacte; standard Portuguese form.')
change(f,20,r"""isto é, \(H\) é «de tipo multiplicativo», cf. IX,
\SGARefLink{sga3:ix:definition:1:1}{1.1}).""",r"isto é, \(H\) é «de tipo multiplicativo»).",'re-edition removed','Proposition 6.3 has no reference to IX 1.1.')
change(f,20,r"justifica-se pelo \SGARefLink{sga3:viii:theorem:6:4}{teorema seguinte}.",'justifica-se pelo','structure','The last paragraph of page 20 ends par le, directly followed by the heading Théorème 6.4; no extra introductory sentence.')
