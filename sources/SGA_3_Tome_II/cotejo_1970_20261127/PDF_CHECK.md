# Verificação final dos PDFs

**Compilação e inspeção visual concluídas em 27 de novembro de 2026.**
Os dois mestres compõem a mesma edição e passam os limites tipográficos
solicitados. A inspeção visual foi feita pelo agente principal; a renderização
e as contagens mecânicas receberam apoio técnico.

## Resultado da compilação

| Métrica | ptbr_current | ptbr_original |
|---|---:|---:|
| Páginas físicas | 43 | 43 |
| Execuções até estabilização | 2 | 2 |
| Mestre autônomo, compilado diretamente | Sim | Sim |
| Referências estabilizadas | Sim | Sim |
| Caixas excedentes (overfull) | 0 | 0 |
| Caixas acima de 2 pt | 0 | 0 |
| Caixas acima de 10 pt | 0 | 0 |
| Maior excesso | 0 pt | 0 pt |
| Avisos de referências indefinidas | 0 | 0 |
| Avisos de destinos inválidos | 0 | 0 |
| Avisos de caracteres ausentes | 0 | 0 |
| Entradas de fontes tipográficas | 38 | 38 |

Todas as fontes estão incorporadas, em subconjuntos e com mapeamento
Unicode. Os dois textos extraídos são idênticos. A comparação dos
43 pares de páginas renderizadas a 1,4× também encontrou **pixels
idênticos em todas as páginas**.

Os mestres TeX são idênticos byte a byte. O SHA-256 agregado da árvore
TeX usada na compilação final é:

    ee4e82aea989aa02812ece3f76aa190e94c9512f25da38f9dcf5bf774bcf11e6

Os logs de cada execução e os logs finais estão em pdf/. O resumo
mecânico é pdf/BUILD_SUMMARY.json; a comparação dos pixels, com dimensões
e hashes por página, está em records/PDF_RENDER_METADATA.json.
Os nomes internos e metadados dos PDFs podem produzir hashes binários
diferentes apesar da identidade do conteúdo e da composição.

## Inspeção visual realizada

Foram renderizadas todas as 43 páginas a 1,4×, equivalentes a 100,8 dpi.
As quatro folhas de contato, cobrindo respectivamente 1–12, 13–24,
25–36 e 37–43, foram examinadas para verificar distribuição, margens,
cabeçalhos, rodapés e páginas finais.

A inspeção ampliada abrangeu as seguintes páginas físicas do PDF.
Ela se aplica aos dois mestres pela identidade dos pixels:

| Páginas físicas | Conteúdo e elementos examinados |
|---|---|
| 2, 4, 5, 6 | Aviso de direitos, sumário, nota e créditos, abertura de VIII e primeiras fórmulas. |
| 8, 9 | Acentuação no subscrito Módulo, homomorfismos, itens de VIII 2.1 e fórmulas de cardinalidade. |
| 13, 14 | Graduações, inversos, diagrama curvo, abertura de VIII 5 e fórmulas do quociente. |
| 16 | Título longo com produto de funtores, enunciados e nota de rodapé. |
| 20, 22 | Notas originais, espaços e pontuação das chamadas, argumento de monomorfismos e diagrama de VIII 7.5. |
| 25, 26 | Abertura de IX, definições e diagrama de implicações. |
| 29 | Itens de IX 2.11, prova e transição de seção. |
| 32, 33 | Índices, primos, fórmulas tensoriais, diagrama e prova de densidade. |
| 38 | Título longo de IX 6, fórmulas locais e nota. |
| 40, 41, 42 | Limites, completamentos, diagramas, somatórios e lema de finitude. |
| 43 | Seção IX 8 inteira, equações numeradas, observação final e nota original. |

Não se observaram cortes de conteúdo, sobreposição de fórmulas ou índices,
rótulos de diagramas colidindo, invasão das margens, notas truncadas ou
cabeçalhos sobrepostos. Os números do sumário são os de 1970; as páginas
da composição são próprias, como explica a nota preliminar. Não há um
índice geral acrescentado após o fim do Exposé IX.

### Ajustes decorrentes da inspeção

A inspeção identificou três espaços suprimidos após chamadas de nota em
VIII §7, nas páginas físicas 20 e 22. Também foi restituída a posição
das chamadas em relação às palavras e aos pontos do impresso. As cinco
operações estão em C0418–C0422, classificadas como typesetting e
confirmadas contra os recortes ampliados do original.

Após a recompilação, a comparação de imagens mostrou que **somente as
páginas 20 e 22 mudaram**; ambas foram novamente examinadas em detalhe.
As outras 41 páginas conservaram os mesmos pixels. Não houve mudança
no número de páginas.

Nenhuma caixa da árvore corrigida excedeu 10 pt. No ensaio técnico
inicial, ainda com o texto recebido, houve um excesso de 23,92921 pt no
título da Exposição XI no índice geral. A macro desse título foi ajustada
para alinhamento à esquerda. A página corrigida do ensaio — página física
5, rótulo V — foi renderizada e examinada. Esse título está fora do recorte
VIII–IX e não integra o sumário final. A página 4 do sumário final também
foi examinada em detalhe.

## Ambiente e limites

A composição usa pdfTeX 1.40.26, papel A4, corpo de 11 pontos e margens
de 25 mm, com Latin Modern, AMS e RSFS. O ambiente tem a localização
brasileira do Babel, mas não os padrões de hifenização automática
portuguesa. A composição entregue foi verificada nesse ambiente,
sem downloads de recursos adicionais.

As imagens de inspeção são temporárias e não integram o pacote.
O mapa mecânico de páginas está em records/PDF_PAGE_MAP.tsv.
A aprovação visual se refere à composição final; não é uma prova
independente das afirmações matemáticas nem elimina as limitações
de leitura do escaneamento registradas nas páginas impressas 54, 68 e 74.

**Conclusão:** os dois PDFs têm referências estabilizadas, zero caixas
excedentes e composição visual aprovada nas páginas inspecionadas,
com verificação global por folhas de contato e identidade de pixels
entre os dois mestres.
