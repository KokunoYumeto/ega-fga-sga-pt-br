# Preparação técnica da compilação

## Escopo

Esta intervenção preparou apenas a infraestrutura de composição. Nenhuma página
do escaneamento foi lida pelo agente de apoio, e nenhum arquivo de texto
matemático recebido foi alterado por ele. O cotejo, as decisões de leitura e a
verificação visual final pertencem ao fluxo principal.

## Lacunas do material recebido

Os dois arquivos denominados `ptbr_current.tex` e `ptbr_original.tex` contêm
somente a matéria preliminar: não incluem classe, preâmbulo, ambiente `document`
ou chamadas às exposições. Nenhum arquivo de compilação ou definição das macros
`SGA...` acompanha o conjunto. Os arquivos `body.tex` usam ainda o prefixo
`units/`, ausente da árvore recebida.

Foram criados `sources/build_support.tex` e `scripts/build.py`. O primeiro
implementa as macros tipográficas já chamadas pelos arquivos, sem fornecer texto
matemático. O segundo compila ambos os mestres até estabilizarem os arquivos
auxiliares, conserva os PDFs e grava logs sem caminhos locais ou endereços
eletrônicos. Se um mestre ainda for um fragmento, o script cria uma montagem
temporária; um mestre que inclua `build_support` é compilado diretamente.
O prefixo antigo `units/` também é resolvido no diretório temporário de compilação.

Para tornar os mestres diretamente utilizáveis, basta que o fluxo principal
adicione o preâmbulo, o ambiente `document` e as chamadas às exposições ao redor
da matéria preliminar. Essa alteração estrutural deve constar do registro de
correções.

## Ambiente e solução reproduzível

Estão instalados pdfTeX 1.40.26, LuaHBTeX 1.18.0 e latexmk 4.86. Os arquivos
de pacotes e fontes estão presentes, mas os índices e formatos gerados do TeX
Live não estavam disponíveis. O script localiza os diretórios de recursos
pelas variáveis do próprio `kpsewhich`, desativa a dependência dos índices
ausentes, gera um formato pdfLaTeX em cache privado e compõe o mapa das fontes
já instaladas. Nenhum download é necessário. Em uma instalação normal com
formato pronto, usa diretamente essa instalação.

O pacote de hifenização português não está instalado neste ambiente. A
localização brasileira do Babel está disponível; a composição usa essa
localização sem hifenização automática de palavras portuguesas. São usados
Latin Modern, AMS e RSFS, em A4, corpo de 11 pontos e margens de 25 mm. O ajuste
de composição é exclusivamente tipográfico.

## Ensaio técnico isolado

Uma montagem temporária, fora dos entregáveis, usou o texto recebido sem
alterações. Ela gerou 68 páginas e estabilizou em duas execuções. O primeiro
ensaio apresentou uma única caixa excedente: 23,92921 pt no título longo da
Exposição XI no índice geral. A macro desse título foi ajustada para alinhamento
à esquerda, preservando integralmente as palavras. O ensaio seguinte registrou
zero caixas excedentes. As remissões foram ajustadas na implementação da macro
para empregar o destino do `label` do Hyperref, inclusive quando a fonte usa
`label` diretamente em uma equação. O último ensaio não apresentou avisos de
referências indefinidas, destinos inexistentes ou caracteres ausentes.

Esses resultados são apenas ensaios da infraestrutura. Não constituem o cotejo
do texto recebido nem a verificação dos PDFs finais. Os mestres corrigidos devem
ser compilados novamente e os resultados registrados em `PDF_CHECK.md`.

## Uso

```sh
python scripts/build.py
```

O resultado inclui os dois PDFs, os logs de cada execução e
`pdf/BUILD_SUMMARY.json`, com o número de execuções, estabilização, contagem de
caixas excedentes e avisos de referências ou caracteres. Pode-se usar `--cache`
para reutilizar uma pasta de compilação. O cache não deve entrar no ZIP de
entrega.

## Empacotamento dos checkpoints e da entrega

Foi criado também `scripts/package.py`. O chamador controla o intervalo de 45
minutos e o envio durável; o script não agenda nem envia arquivos. Os modos são:

```sh
python scripts/package.py --checkpoint 01
python scripts/package.py --final
```

`--dry-run` realiza apenas a conferência do inventário, sem criar arquivos. O
manifesto é localizado por padrão em `inputs/MANIFEST.tsv`, ao lado da árvore de
trabalho; `--manifest` permite indicar outra posição. A saída fica fora da árvore
de trabalho, em `deliverables/`, e pode ser alterada com `--output-directory`.

O empacotamento compara SHA-256 com todas as entradas do manifesto e omite
qualquer cópia exata de um anexo. Também exclui caches, intermediários de
compilação, imagens de inspeção, escaneamentos, extrações e ZIPs. Cada checkpoint
recebe um inventário próprio e instruções para restaurar as fontes ainda
inalteradas a partir do anexo antes de sobrepor os arquivos corrigidos. O modo
final exige a presença de todos os arquivos esperados da árvore portuguesa,
modificados, além dos documentos e dos dois PDFs solicitados.

Fontes, programas e registros são recusados caso contenham caminhos locais
absolutos ou endereços eletrônicos. Logs podem receber cópias sanitizadas dentro
do pacote, com a quantidade de substituições anotada no inventário. O ZIP é
verificado quanto a CRC, inventário e tamanho estritamente inferior a 500 MB
antes de receber seu nome definitivo. Um arquivo existente nunca é sobrescrito.

O ensaio deste script usou somente `--dry-run`; nenhum checkpoint foi criado
pelo agente de apoio. Os programas e esta documentação foram conferidos para
ausência de caminhos locais literais e endereços eletrônicos. O cabeçalho de
execução do script de compilação foi removido; ambos os scripts são invocados
explicitamente com `python`, como acima.

## Validador técnico

`scripts/validate.py` verifica mecanicamente os entregáveis obrigatórios, a
sequência das 76 páginas nos registros, o estado da segunda leitura de cada
correção, a presença de evidência, a estrutura da tabela de eventos, os rótulos,
a integridade dos textos e a sintaxe dos programas. Para o estado em andamento,
use `python scripts/validate.py --progress`; a execução sem essa opção exige o
estado final.

O validador compara os textos extraídos dos dois PDFs em memória, sem salvar
extrações. Também conta as caixas excedentes dos logs finais, detecta avisos de
referências ou caracteres e verifica se o resumo de compilação corresponde ao
SHA-256 agregado da árvore TeX atual. Esse SHA-256 é registrado pelo script de
compilação; uma alteração das fontes durante a compilação provoca falha, para
evitar PDFs que não correspondam ao estado das fontes.

Os relatórios são `records/TECHNICAL_VALIDATION.json` e
`records/LABEL_INVENTORY.json`. O segundo conserva o inventário original de
rótulos como metadados e informa omissões, duplicações e remissões internas sem
destino. Nenhum rótulo nem linha de correção é alterado pelo validador. Os
resultados são conferências mecânicas; não substituem a leitura do escaneamento,
a inspeção visual dos PDFs ou uma demonstração matemática.

A verificação de privacidade dos PDFs finais examina tanto o texto extraído
como os campos de informação e os metadados XMP fornecidos por `pdfinfo`,
procurando caminhos locais absolutos e endereços eletrônicos. O relatório
registra apenas contagens e nomes relativos dos arquivos; os valores
eventualmente encontrados não são copiados para ele.

### Ajuste lexical do programa da página 20

Cinco literais de `scripts/page_020.py`, originalmente nas linhas 7, 13 e 14,
foram convertidos em literais raw para eliminar os avisos de escapes Python.
Os valores decodificados de cada string foram comparados em UTF-8 e são
idênticos byte a byte; a árvore sintática completa, sem atributos de posição,
também permanece idêntica. O script não foi executado novamente, e nenhuma
fonte traduzida nem linha de `CORRECTIONS.tsv` foi alterada por esse ajuste.

SHA-256 anterior do programa:
`5cc0c201182862ae55c84b7a07168be19a18919b097eba6020d3834501f181b6`.
SHA-256 após o ajuste:
`6344d589df474a5191a2f45ae1e45c2580052652fd0dc0a01b87cfadee080298`.

### Reutilização do cache de compilação

Antes da primeira compilação da árvore corrigida, foi constatado que o cache
do ensaio isolado ainda tinha ligações simbólicas para a árvore daquele ensaio.
O script de compilação foi corrigido para atualizar cada ligação para a árvore
de fontes efetivamente solicitada, inclusive o alias de compatibilidade
`units/`. Uma entrada comum que não seja uma ligação administrada provoca uma
mensagem de erro e exige um cache limpo; o script não a sobrescreve. A correção
é exclusivamente de infraestrutura e não altera fontes traduzidas. Os ensaios
anteriores continuam identificados como ensaios do texto recebido.

### Reprodução do histórico em memória

`scripts/replay_corrections.py` reaplica, em memória, as substituições `old/new`
de `CORRECTIONS.tsv` às fontes iniciais verificadas pelo manifesto. O programa
não modifica fontes ou auditoria. Confere as linhas registradas, os hashes de
todos os arquivos resultantes e os blocos de direitos dos dois mestres.
Operações de substituição global usam todas as ocorrências, conforme a
semântica de `audit.change`; reversões são aplicadas na ordem registrada.

```sh
python scripts/replay_corrections.py --write-report
```

A opção grava somente `records/HISTORY_REPLAY.json`. Sem ela, o programa
imprime um resumo. O original pode ser fornecido como diretório com
`--original-sources` ou como o ZIP anexado com `--original-zip`. O relatório
também verifica que fontes e auditoria não mudaram durante a leitura.
O bloco de direitos recebido tem 992 bytes e SHA-256
`9821543df3e52ad21012de8a30debf0fc1ddd8a293ac8ad6e8abba783f59f7f5`;
o relatório registra a comparação byte a byte para cada mestre.

### Instruções do pacote final

O empacotamento distingue a entrega final dos checkpoints: a entrega final contém todas as fontes e dispensa restauração a partir do anexo para compilar. O anexo é exigido apenas para repetir o cotejo ou o replay histórico. Essa distinção consta tanto da nota de uso como do inventário gerado.
