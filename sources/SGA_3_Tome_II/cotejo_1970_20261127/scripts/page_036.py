import re
from audit import change,ROOT
f='08_expose_viii/components/11_seccion_7_parte_2_y_bibliografia.tex'
change(f,36,r"seja finito sobre \(S'\) e \({}_nH'\) separado sobre \(S'\). Então \(u\)",r"seja finito sobre \(S'\) e \({}_nH'\) separado sobre \(S''\). Sob essas condições, \(u\)",'1970 restored','At the top of page 36 Proposition 7.12 prints S″ after the separatedness of {}_nH′, followed by Sous ces conditions. The double prime is retained.')
change(f,36,r'\SGARefTarget{sga3:viii:remark:7:13}\textbf{Observação 7.13.}',r'\SGARefTarget{sga3:viii:remark:7:13}\textbf{Observações 7.13.}','1970 restored','The heading is plural: Remarques 7.13.')
change(f,36,r'''tomando como \(G\) o \(S\)-grupo unidade. Se \(S\) é localmente
  noetheriano,''',r'''tomando como \(G\) o \(S\)-grupo unidade. Notemos também que, quando
  \(S\) é localmente noetheriano,''','translation','7.13(a) explicitly says Notons aussi que lorsque S est localement noethérien.')
change(f,36,'geralmente, de tipo multiplicativo, e \\(H\\)','geralmente, «de tipo multiplicativo», e \\(H\\)','typesetting','7.13(b) puts de type multiplicatif in quotation marks.')
change(f,36,r'''{5.7}. Se \(G\) é liso sobre \(S\),
  aplique-se diretamente a''',r'''{5.7}. Quando \(G\) é suave sobre \(S\),
  basta aplicar a''','translation','7.13(b): Lorsque G est lisse ... il suffit d’appliquer 7.12; standard suave and no added directement.')
change(f,36,r'''da condição \SGARefLink{sga3:viii:proposition:7:9:item:c}{(c)} a''',r'''da condição \SGARefLink{sga3:viii:proposition:7:9:item:c}{7.9 c)} a''','1970 restored','7.13(c) explicitly refers to la condition 7.9 c).')
s=(ROOT/'sources'/f).read_text();i=s.index('\\SGARefTarget{sga3:viii:bibliography}');old=s[i:]
anchors=re.findall(r'\\SGA(?:Inline)?RefTarget\{[^{}]+\}',old)
change(f,36,old,'\n'.join(anchors)+'\n','re-edition removed','Page 36 ends after 7.13(c), with the Raynaud reference VI_B 5.5. There is no Bibliography heading, editorial footnote, RG71 or TO70 entry, or closing workflow comment. All original reference targets are retained invisibly.')
change(f,36,'% SGA 3, Exposé VIII, tradução brasileira: Corolário 7.5 a 7.13 e bibliografia.','% SGA 3, Exposé VIII, tradução brasileira: Corolário 7.5 a 7.13.','structure','The component now ends with 7.13; the bibliography was an addition absent from 1970.')
change(f,36,'% Fim estrito antes do Exposé IX.\n','','structure','Removed the old workflow boundary comment; the source authority header remains.')
