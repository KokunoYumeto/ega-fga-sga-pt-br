# SGA 3 — Exposições VIII e IX em português brasileiro

## Edição e autoridade

Esta edição traz as Exposições VIII e IX ao texto da impressão de 1970 de
*Schémas en groupes*, tomo II, **Lecture Notes in Mathematics 152**,
páginas impressas **1–76**. As 76 páginas foram lidas sequencialmente contra
o escaneamento fornecido. As 422 operações históricas têm evidência e
segunda leitura registradas; leituras provisórias emendadas permanecem
no histórico.

Os dois mestres, sources/ptbr_current.tex e sources/ptbr_original.tex,
são **idênticos byte a byte**, autônomos e compõem a mesma edição.
A nota preliminar registra a origem da tradução em 2026, seu retorno à
impressão de 1970 em novembro de 2026 e os créditos solicitados.
O texto, as notas, as referências, a estrutura e os comentários dos
exposés foram depurados dos acréscimos e correções da reedição.

Referência: M. Demazure e A. Grothendieck (dir.), *Schémas en groupes
(SGA 3)*, tomo II, Lecture Notes in Mathematics 152, Springer-Verlag,
1970; Exposições VIII e IX, por A. Grothendieck, pp. 1–76.

Arquivo fornecido: SGA3_1970_scan/LNM152_pdf_pages_001-100.pdf,
10.604.758 bytes, SHA-256:

    78b469473551ba306bf536ca3f4312508ce11835d3e717d8ba9d4227eb488c3f

A página impressa N corresponde à página N + 7 do PDF. A página 1 do
PDF é a folha de rosto interna; a página 2 contém as entradas do
sumário para VIII e IX. A capa e o aviso de direitos não constam desse
recorte; foram conservados a partir das fontes recebidas.

Os **48 arquivos** do anexo foram conferidos por tamanho e SHA-256 antes
do cotejo, conforme records/MANIFEST_VERIFICATION.json. O escaneamento
de 1970 foi a única autoridade textual. Os auxiliares ingleses fornecidos
serviram apenas à estrutura e à terminologia; as decisões terminológicas
e o glossário recebidos orientaram os termos portugueses. Nenhuma fonte
externa substituiu o impresso.

## Registros e alcance

| Registro | Conteúdo |
|---|---|
| CORRECTIONS.tsv | 422 operações, com arquivo, página impressa, linha anterior à operação, texto anterior e novo, espécie, evidência e segunda leitura. |
| CHECK_RECORD.md | Totais por espécie, catálogo de retiradas e uma seção para cada uma das 76 páginas. |
| CHECK_EVENTS.tsv | 156 eventos para 110 enunciados numerados distintos. |
| PDF_CHECK.md | Compilação, contagem de caixas, inspeção visual e limites da composição. |
| progress.log | Início em UTC, conclusão sequencial de cada página e etapas finais. |
| records/pages.json | Dados das seções por página e revisões dirigidas posteriores. |
| records/HISTORY_REPLAY.json | Reprodução em memória das alterações a partir das fontes recebidas. |
| records/TECHNICAL_VALIDATION.json | Validação mecânica dos entregáveis. |
| records/LABEL_INVENTORY.json | Preservação e verificação dos 315 destinos originais. |

As 422 operações não representam 422 divergências independentes: incluem
estrutura, composição e emendas posteriores. Os IDs C0001 etc. correspondem
à posição da linha de dados, sem contar o cabeçalho. A coluna line indica
a linha imediatamente anterior à operação; old e new permitem reproduzir
a sequência.

Todos os eventos matemáticos são classificados como
**carried as background without fault found**. Eventos repetidos para o
mesmo ID registram a continuação da leitura em outra página. Não se atribui
ao trabalho uma prova independente, um certificado formal ou uma validação
da verdade de uma gralha preservada. A correspondência mecânica entre os
110 cabeçalhos numéricos e os 110 IDs verifica a cobertura das fontes
atuais; não substitui a leitura do escaneamento.

A leitura e todas as decisões textuais foram do agente principal, em um
único fluxo. O apoio paralelo ficou restrito à compilação, reprodução
do histórico e verificações mecânicas. A inspeção visual final também
pertence ao agente principal.

### Limites materiais de leitura

| Página impressa | Trecho | Limite |
|---|---|---|
| 54 | Extremidade direita da desigualdade entre as fibras de Z e Y | Parcialmente encoberta pela dobra; reconstrução a partir da notação visível e da frase, assinalada em C0286. |
| 68 | Expoente na definição de S_n | A borda direita está encoberta; n+1 é apoiado pela definição explícita de A_n na p.69, conforme C0346. |
| 74 | Último número da remissão «3 a 7» | O 7 está encoberto pela sombra da encadernação e foi mantido por contexto, conforme C0359. |

Esses casos não são apresentados como leituras integralmente visíveis.
As emendas de leituras provisórias, inclusive n na p.7, EGA I na p.51 e
IV_B na p.74, estão na coluna confidence. As gralhas do impresso foram
mantidas, mesmo quando produzem afirmações ou referências problemáticas.

## Organização e preservação

Os nomes de arquivos, as macros editoriais e os destinos recebidos foram
preservados. Destinos de estruturas adicionais retiradas permanecem
invisíveis para compatibilidade. Remissões a exposés não incluídos
conservam seu texto, sem destino eletrônico fictício.

O índice geral do tomo II está fora do recorte 1–76 e referia uma página
do escaneamento não fornecida. Seu conteúdo visível e seus comentários foram
suprimidos, mantendo arquivo, inclusão e destino. A redefinição local de
arraystretch, exclusiva dessa tabela retirada, foi suprimida com ela;
nenhuma macro editorial própria foi eliminada. O sumário limita-se a VIII
e IX e conserva os números de página de 1970. Os PDFs têm paginação própria.

O aviso de direitos foi mantido **exatamente**, inclusive a nota de
proveniência que já fazia parte dele. Seu bloco tem 992 bytes e SHA-256:

    9821543df3e52ad21012de8a30debf0fc1ddd8a293ac8ad6e8abba783f59f7f5

O pacote contém toda a árvore portuguesa corrigida. Omite cópias inalteradas
dos anexos, escaneamento, imagens e extrações dele, auxiliares ingleses,
arquivos terminológicos recebidos, caches, recursos de fontes tipográficas
e ZIPs anteriores. As transcrições e traduções necessárias à edição e ao
histórico integram a entrega.

## Compilação e validação

No diretório extraído, que contém sources/ e scripts/, execute:

    python scripts/build.py
    python scripts/validate.py

São necessários Python 3 e TeX Live com pdfLaTeX e os pacotes declarados em
sources/build_support.tex. O script usa recursos instalados, sem downloads,
e pode gerar um formato local quando faltam índices ou formatos preparados.
Compila diretamente os dois mestres até estabilizarem os auxiliares e
grava os PDFs, logs e pdf/BUILD_SUMMARY.json, incluindo o SHA-256 agregado
das fontes e as contagens de caixas e avisos.

A composição usa A4, corpo de 11 pontos, margens de 25 mm, Latin Modern,
AMS e RSFS. A localização brasileira do Babel está disponível no ambiente;
os padrões de hifenização automática portuguesa não estão instalados.
Os resultados observados constam de PDF_CHECK.md. A infraestrutura foi
necessária porque o anexo continha fragmentos preliminares sem preâmbulo,
definições das macros ou montagem completa; ver records/BUILD_SETUP.md.

O validador confere as 76 páginas, os campos e enumerações das tabelas,
as segundas leituras, IDs, rótulos, integridade do TeX, correspondência
entre fontes e PDFs, igualdade textual dos PDFs e avisos dos logs.
Não lê o escaneamento nem realiza inspeção visual.

Para reproduzir o histórico em memória a partir do anexo original:

    python scripts/replay_corrections.py --original-zip ANEXO.zip --write-report

O programa aplica old/new em memória, confere as linhas históricas e compara
os 27 arquivos resultantes com a árvore entregue; também confere o aviso de
direitos. O anexo original é necessário apenas para essa auditoria, não para
compilar a edição.

Os programas page_*.py, final_text_review*.py, finalize_sources.py e os
demais programas de alteração documentam operações já aplicadas.
**Não devem ser reaplicados à árvore final.** Há operações provisórias
posteriormente emendadas; o estado definitivo é sources/, conferido pelo
replay completo de CORRECTIONS.tsv.

scripts/package.py oferece --checkpoint NN, --final e --dry-run.
O manifesto recebido pode ser indicado por --manifest, e a saída por
--output-directory. O programa compara hashes, exclui anexos inalterados,
verifica privacidade, CRC e tamanho inferior a 500 MB, e não sobrescreve ZIPs.

## Checkpoints e método

Cada checkpoint contém os entregáveis e registros existentes naquele
instante, omitindo os materiais recebidos inalterados e os itens excluídos.
Nenhum checkpoint contém um ZIP anterior. Os horários estão em
records/CHECKPOINTS.json. Para retomar um checkpoint intermediário, extraia
SGA3_PTBR_sources/ do anexo como sources/ e sobreponha o checkpoint.
Consulte records/CHECKPOINT_RESTORE.md e o inventário. Essa restauração
não é necessária para a entrega final, que contém todas as fontes.

O progresso começa em 27 de novembro de 2026, 17:09:08 UTC.
A rotina inicial gravava a linha de progresso imediatamente antes de
regenerar o relatório da página na mesma chamada; a partir da p.70 a
ordem interna foi ajustada para relatório e depois progresso. Os horários
históricos não foram reescritos. As 76 seções e as linhas de progresso
foram verificadas quanto à ordem e à ausência de lacunas.

## Créditos

Primeira tradução: **OpenAI Codex (GPT-5.6 Sol, esforço de raciocínio ultra)**.
Este cotejo: **GPT-6.0 Astra (OpenAI), modo ChatGPT Pro**. O identificador
operacional disponível nesta sessão é GPT-6 Astra Pro; o nível de esforço
deste passe não foi exposto pela interface e não foi inventado.
