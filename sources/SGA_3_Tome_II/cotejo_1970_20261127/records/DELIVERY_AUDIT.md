# Auditoria técnica da entrega

Inspeção: 2026-11-27 18:33:09 UTC. Este registro descreve um estado intermediário, com o editor principal ainda revisando as fontes. Nenhum escaneamento foi lido, nenhuma decisão textual foi tomada e nenhuma fonte ou linha da tabela de correções foi alterada por esta auditoria. Os resultados abaixo não certificam a fidelidade ao impresso nem a verdade dos enunciados.

## Cobertura e estrutura verificadas

- records/pages.json, as seções de CHECK_RECORD.md e as linhas de conclusão de progress.log contêm exatamente as páginas 1–76, consecutivas e sem duplicações.
- A primeira linha do progresso é 2026-11-27 17:09:08 UTC.
- As tabelas de correções e eventos têm as colunas solicitadas. Não há evidência vazia nas correções nem campos obrigatórios vazios nos eventos.
- Há 156 eventos e 110 identificadores distintos. Todos os eventos usam carried as background without fault found. Os identificadores repetidos registram a continuação de leitura em páginas distintas.
- A extração mecânica dos cabeçalhos numéricos visíveis das fontes produziu 110 identificadores; seu conjunto é exatamente o conjunto de IDs dos eventos. Isso verifica a correspondência com as fontes atuais, sem substituir a conferência da numeração do impresso pelo editor.
- Os 315 destinos de referência originais estão preservados, sem duplicação. Não se encontraram chaves ou ambientes TeX desequilibrados.
- Os dois mestres são idênticos byte a byte.
- A única redefinição original ausente do inventário de macros é arraystretch, antes local ao índice geral retirado do recorte. Não é uma macro editorial própria; a situação deve permanecer explicada pela alteração estrutural desse índice.
- A montagem de inventário do pacote passou sem caminhos locais absolutos ou endereços eletrônicos nos arquivos elegíveis. Não omite nenhuma fonte esperada por falta de alteração; nenhuma cópia idêntica de arquivo anexo integra o inventário. Escaneamentos, imagens, extrações, caches e ZIPs anteriores são excluídos.

## Pendências do estado inspecionado

A tabela tinha 417 linhas de correção. Contagens por espécie:

| Espécie | Linhas |
|---|---:|
| 1970 restored | 149 |
| re-edition removed | 76 |
| reading | 34 |
| source authority | 1 |
| structure | 37 |
| translation | 95 |
| typesetting | 25 |

1. Corrigir a espécie de C0301, página 58: source authority não pertence à enumeração solicitada; a classificação técnica adequada sugerida é structure. O texto da mudança não precisa ser reaplicado.
2. Concluir a segunda leitura das 14 linhas ainda pendentes neste instante: C0401, C0402, C0403, C0407, C0408, C0409, C0410, C0411, C0412, C0413, C0414, C0415, C0416, C0417. Novas linhas devem receber o mesmo tratamento.
3. Completar o catálogo de passagens removidas: audit.report() inclui somente linhas cuja espécie é re-edition removed. Há remoções explicitamente documentadas também em linhas de restauração e estrutura.
4. Substituir os estados provisórios de README.md e PDF_CHECK.md por resultados efetivamente observados. Ambos ainda dizem que os mestres e PDFs finais estão pendentes.
5. Após congelar as fontes, repetir o replay do histórico, a compilação, a inspeção visual requerida e o validador final. O resumo de compilação intermediário já registra dois mestres autônomos, duas execuções cada, referências estabilizadas e zero caixas excedentes; sua validade final depende da correspondência com o hash da árvore concluída.
6. A biblioteca de hifenização portuguesa está ausente no ambiente utilizado, conforme pdf/BUILD_SUMMARY.json; essa característica da composição deve ser documentada, sem atribuir ao PDF uma hifenização que não foi usada.
7. Produzir o pacote final apenas após os gates acima, conferindo inventário, CRC, tamanho e salvamento durável. O próximo checkpoint tem vencimento registrado em records/CHECKPOINTS.json para 18:39:08 UTC.

## Complemento recomendado ao catálogo de removidos

A melhoria segura é manter a espécie principal de cada correção e criar, no topo de CHECK_RECORD.md, uma seção adicional indexada por IDs de correção. Uma lista explícita curada pelo editor evita que uma expressão regular confunda “a reedição removeu uma hipótese original” com “foi removido um acréscimo da reedição”.

Os seguintes candidatos já têm remoção escrita em sua própria evidência; são referências para decisão do editor, sem nova leitura da autoridade por esta auditoria:

| Correção | Página | Remoção descrita no registro |
|---|---:|---|
| C0058 | 14 | Nota e argumento ampliado pelos abertos auxiliares. |
| C0068 | 16 | Mudança de notação, comentário entre colchetes e expansão do argumento. |
| C0075 | 18 | Correção para P e comentário entre colchetes. |
| C0078 | 18 | Comentário corretivo da leitura impressa. |
| C0167 | 30 | Parêntese acrescentado que identifica 7.3 a VII_A 8.5. |
| C0174 | 31 | Nota do tradutor que corrigia dois índices. |
| C0176 | 32 | Comentário corretivo entre colchetes. |
| C0210 | 37 | Citação acrescentada a VIII 1.1 e estrutura separada de apresentação. |
| C0248 | 45 | Substituições de referências pela reedição. |
| C0282 | 53 | Frase acrescentada sobre noetherianidade e comentário sobre os índices. |
| C0318 | 60 | Justificação acrescentada por VIII 6.3 e liberdade essencial. |
| C0325 | 62 | Citações e equações substitutas acrescentadas. |
| C0333 | 64 | Construção exibida com chave e equações substitutas. |
| C0335 | 65 | Reestruturação da demonstração em fórmulas destacadas. |
| C0337 | 65 | Condição de isolamento repetida e ampliada. |
| C0339 | 66 | Referência acrescentada a VI_B 1.3. |
| C0341 | 67 | Redefinição acrescentada de K. |
| C0343 | 67 | Citação acrescentada a 6.6.1. |

Também há remoções de comentários de trabalho nas correções de estrutura C0001, C0024, C0205, C0207, C0377 e C0378. O catálogo pode distingui-las de passagens matemáticas, sem reclassificar as linhas ou afirmar que todo comentário de trabalho provinha da reedição.

## Limites do validador atual

O programa validate.py confere colunas, evidência, campos vazios e conclusão da segunda leitura, mas não rejeita uma espécie fora da enumeração nem um tipo de evento fora da lista permitida. Tampouco compara por si mesmo os IDs com os cabeçalhos numéricos. Esses três checks foram executados manualmente nesta auditoria; podem ser adicionados tecnicamente ao programa antes da entrega. Nenhuma mudança de fonte é necessária para isso.

O inventário de privacidade trabalha com nomes relativos de arquivos e textos elegíveis. A privacidade dos PDFs deve ser confirmada pelo validador em sua execução final, incluindo texto e metadados. Este registro não afirma que a inspeção visual final já ocorreu.


## Atualização técnica do validador

Por solicitação do editor principal, scripts/validate.py foi ampliado em 2026-11-27 18:34:45 UTC. A versão agora rejeita espécies de correção fora das seis permitidas e tipos de evento fora dos seis permitidos. O tipo refuted permanece um tipo próprio; a identificação do enunciado refinado pertence ao registro do resultado. Nenhuma refutação foi declarada neste trabalho.

O programa também extrai cabeçalhos numéricos visíveis das duas exposições nas fontes TeX, descartando comentários e alvos invisíveis, e compara seus identificadores com CHECK_EVENTS.tsv. São registrados cabeçalhos sem eventos, eventos sem cabeçalhos e cabeçalhos repetidos. O relatório declara explicitamente que essa conferência é mecânica, relativa às fontes atuais, e não equivale à leitura do escaneamento.

Foi executada a validação em modo final. Resultado desse instante:

- 417 linhas de correção; 0 espécies inválidas; 0 segundas leituras pendentes.
- 156 eventos; 110 IDs; 0 tipos inválidos.
- 110 cabeçalhos visíveis e 110 IDs distintos; nenhuma diferença entre os conjuntos de cabeçalhos e eventos, nem repetição de cabeçalhos.
- Nenhum aviso técnico.
- Único erro restante: a árvore TeX atual difere do hash registrado pela compilação disponível; é necessária a compilação da árvore final. Nenhuma aprovação visual é inferida deste resultado.

A saída detalhada está em records/TECHNICAL_VALIDATION.json. A execução também atualizou records/LABEL_INVENTORY.json, conforme o comportamento já existente do validador. Nenhum arquivo em sources, CORRECTIONS.tsv ou material de consulta foi alterado.


## Fechamento da auditoria técnica

Fechamento em 2026-11-27 18:46:56 UTC, após aviso do editor principal de que a compilação e a inspeção visual finais foram concluídas. Os estados intermediários acima são preservados como histórico; as pendências ali enumeradas receberam os seguintes desfechos.

- **Espécies e segunda leitura:** C0301 está classificada como structure. As 422 correções têm evidência e estado de segunda leitura concluído, sem espécie inválida ou campo de evidência vazio.
- **Eventos:** os 156 eventos abrangem 110 IDs distintos, exatamente correspondentes aos 110 cabeçalhos numéricos visíveis das fontes atuais, sem tipos inválidos ou cabeçalhos duplicados. Essa equivalência permanece uma verificação mecânica das fontes.
- **Catálogo de remoções:** o topo de CHECK_RECORD.md inclui agora remoções embutidas em restaurações; a presença das entradas C0058, C0068, C0167, C0248, C0318 e C0343 foi conferida, resolvendo a limitação do catálogo anterior.
- **Documentação final:** README.md e PDF_CHECK.md foram atualizados para o estado concluído. A limitação relativa à hifenização portuguesa está documentada. O registro records/PDF_VISUAL_CHECK.json identifica o editor principal como responsável pela inspeção, as páginas efetivamente examinadas e a nova inspeção das páginas 20 e 22.
- **Compilação:** a correspondência entre o hash da árvore TeX e o resumo da compilação está correta. Os dois PDFs têm 43 páginas, textos extraídos idênticos, referências estabilizadas e zero caixas excedentes, caracteres ausentes ou avisos de destinos inválidos.
- **Inspeção visual registrada:** o registro do editor informa cobertura das 43 páginas por folhas de contato e inspeção detalhada de 21 páginas, incluindo as páginas 20 e 22 recompostas. A identidade de pixels dos 43 pares de páginas consta dos registros técnicos. Esta auditoria verificou os registros, sem realizar nova inspeção visual.

A execução final de scripts/validate.py terminou com **passed: true**, **zero erros**, **zero avisos** e **zero pendências**. O resultado completo consta de records/TECHNICAL_VALIDATION.json. Não restou gate técnico aberto dentre os itens desta auditoria; a produção e o salvamento durável do ZIP final são a etapa de entrega do editor principal.

Nenhuma fonte, correção ou material de consulta foi alterado por este fechamento.
