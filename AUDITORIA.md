# AUDITORIA DE SEGURANÇA E PRIVACIDADE

**Escopo:** site institucional da EngPalmas — HTML, CSS e JavaScript
estáticos, hospedados no GitHub Pages, repositório público. Sem back-end,
sem banco de dados, sem autenticação.

**Data:** 14/08/2026 · **Páginas auditadas:** 9 · **Commits examinados:** 11

> A revisão foi feita para *esta* arquitetura. Ameaças que dependem de
> servidor de aplicação não foram inventadas para engrossar o relatório —
> estão isoladas na seção (c), marcadas como não aplicáveis hoje.

---

# (a) Encontrado e corrigido

## a.1 — Repositório sem `.gitignore`

**Achado:** o repositório não tinha `.gitignore` nenhum. Num repositório
público, isso significa que qualquer arquivo colocado na pasta entrava no
commit seguinte sem nenhuma barreira — incluindo um `.env` ou uma chave
privada colocada ali por engano.

**Correção:** criado `.gitignore` cobrindo credenciais (`.env`, `*.pem`,
`*.key`, `*.p12`, `id_rsa`, `.netrc`), temporários, lixo de sistema
operacional, arquivos compactados, material de estudo e os arquivos
`fase*.md` de instrução interna.

## a.2 — Cinco atributos `style=` inline

**Achado:** o `index.html` tinha 5 atributos `style=` embutidos. Estilo
inline obriga o CSP a liberar `'unsafe-inline'` em `style-src`, o que
esvazia boa parte da proteção contra injeção de conteúdo.

**Correção:** os 5 viraram classes no `style.css` (`.centralizado`,
`.sem-barra`, `.sem-margem-baixo`, e `border: 0` movido para
`.container-mapa iframe`). Hoje há **zero** atributos `style=` nas 9
páginas, e o `style-src` não precisa de `'unsafe-inline'`.

## a.3 — Ausência de Content-Security-Policy

**Achado:** nenhuma página declarava CSP. Sem ela, qualquer conteúdo
injetado no HTML — por comprometimento da conta do GitHub, por exemplo —
executaria sem restrição.

**Correção:** CSP via `<meta http-equiv>` nas 9 páginas, com comentário
explicando cada diretiva no próprio arquivo. Política aplicada:

| Diretiva | Valor | O que libera |
|---|---|---|
| `default-src` | `'none'` | nada; tudo o mais é exceção explícita |
| `script-src` | `'sha256-…'` ×2 | **só os dois scripts inline daquela página**, por hash. Nenhum script externo, nenhum `eval` |
| `style-src` | `'self'` + `fonts.googleapis.com` | o `style.css` e a folha do Google Fonts |
| `font-src` | `fonts.gstatic.com` | os arquivos `.woff2` da Montserrat |
| `img-src` | `'self'` | só imagens do próprio domínio |
| `frame-src` | `www.google.com` | apenas no `index.html`, para o mapa. Nas outras 8 páginas a diretiva nem existe — `default-src 'none'` já bloqueia |
| `base-uri` | `'none'` | impede injeção de `<base>` para sequestrar links relativos |
| `form-action` | `'none'` | o formulário é tratado em JS; nada deve ser submetido a servidor nenhum |

**Sem `'unsafe-inline'` em nenhuma diretiva.** Os scripts são autorizados
por hash SHA-256, não por permissão geral.

> ### ⚠️ Consequência operacional do hash
>
> **Editar qualquer script inline invalida o hash, e o script para de
> rodar** — silenciosamente, com erro só no console. Depois de mexer no JS,
> o hash tem de ser recalculado. Comando, na pasta do projeto:
>
> ```powershell
> $sha=[System.Security.Cryptography.SHA256]::Create()
> Get-ChildItem *.html | ForEach-Object {
>   $t=[System.IO.File]::ReadAllText($_.FullName,[System.Text.Encoding]::UTF8)
>   $_.Name
>   foreach($m in [regex]::Matches($t,'(?s)<script>(.*?)</script>')){
>     $src=$m.Groups[1].Value -replace "`r`n","`n"
>     "  'sha256-"+[Convert]::ToBase64String($sha.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($src)))+"'"
>   }
> }
> ```
>
> Se preferir não conviver com isso, a alternativa é mover o JavaScript para
> um arquivo `.js` externo e trocar `script-src` por `'self'`. Fica mais
> fácil de manter e continua muito melhor que `'unsafe-inline'`.

## a.4 — Iframe do mapa sem `sandbox`

**Achado:** o `<iframe>` do Google Maps rodava sem restrição de
capacidades, com `referrerpolicy="no-referrer-when-downgrade"` — que envia
a URL completa da página ao Google.

**Correção:**

- `sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"`
  — o mínimo para o mapa funcionar. Ficam bloqueados formulários,
  downloads, travamento de ponteiro, apresentação em tela cheia e navegação
  da janela principal a partir do iframe.
- `referrerpolicy="no-referrer"` — o Google deixa de receber qual página o
  visitante estava vendo.
- `allowfullscreen` removido: não era usado.

## a.5 — Arquivos de trabalho interno versionados

**Achado:** `fase5b.md`, `fase7.md`, `fase8.md` e as respectivas cópias
estão commitados no repositório público. Não são vulnerabilidade, mas são
anotações internas de desenvolvimento visíveis para qualquer um, incluindo
concorrentes que abram o repositório.

**Correção parcial:** o `.gitignore` passa a bloquear `fase*.md`.
**Pendente de ação sua:** o `.gitignore` não remove o que já está
rastreado. Para tirá-los do repositório mantendo os arquivos no disco:

```powershell
git rm --cached fase5b.md fase7.md fase8.md "fase7 - Copia.md" "fase8 - Copia.md"
git commit -m "Remove anotacoes internas do repositorio publico"
```

---

# (a′) Verificado e **sem achado**

Registrado explicitamente para não deixar dúvida de que foi olhado.

| Verificação | Resultado |
|---|---|
| Chave de API (AWS, Google, OpenAI, Slack, GitHub) | **nada** em 52 blobs de texto de todo o histórico |
| Chave privada / certificado | **nada** |
| String de conexão de banco | **nada** |
| Senha ou segredo atribuído em código | **nada** |
| Caminho absoluto de máquina local | **nada** nos arquivos do site |
| Nome de usuário de sistema nos arquivos | **nada** |
| `innerHTML`, `outerHTML`, `insertAdjacentHTML` | **nenhuma ocorrência**; todo texto dinâmico usa `textContent` |
| `eval`, `new Function`, `setTimeout` com string | **nenhuma ocorrência** |
| `document.write` | **nenhuma ocorrência** |
| Manipulador `onclick` inline no HTML | **nenhum**; tudo por `addEventListener` |
| URL `javascript:` | **nenhuma** |
| `target="_blank"` sem `rel` | **nenhum** — os 18 já tinham `rel="noopener noreferrer"` |
| Recurso externo carregado | apenas `fonts.googleapis.com`, `fonts.gstatic.com` e o iframe do `google.com` |

**Sobre o `portedecelular.zip`:** foi extraído do histórico e inspecionado
entrada por entrada. São 19 arquivos — um backup da própria pasta do site
(imagens, `style.css`, páginas antigas e os exercícios de Python), mais o
`testes.html` que as páginas antigas referenciavam. **Nenhum segredo.**
Ele já não está no working tree, mas continua recuperável do histórico;
como o conteúdo é inócuo, não há motivo para reescrever o histórico.

---

# (a″) Dado pessoal exposto — avaliação

| Dado | Onde | Intencional? | Avaliação |
|---|---|---|---|
| Telefone fixo (63) 3215-1305 | rodapé das 9 páginas | **Sim** | Contato comercial. Exposição correta e desejada num site institucional. |
| WhatsApp (63) 98422-2219 | rodapé, botão flutuante, formulário | **Sim** | Idem. É o canal principal de contato do negócio. |
| Endereço da sede | rodapé, seção Localização, JSON-LD | **Sim** | Endereço comercial. Endereço de sede em site de empresa que participa de licitação é esperado. |
| Coordenadas da sede | `index.html`, embed do mapa | **Sim** | Apontam para o endereço comercial já publicado. Não acrescentam exposição. |
| CNPJ, CREA, responsável técnico | ainda como `[[PREENCHER]]` | **Sim, quando preenchidos** | São dados públicos por natureza — CNPJ é consultável na Receita, registro CREA é público. Nome do responsável técnico é dado profissional, não particular. |
| E-mail institucional | ainda como `[[PREENCHER]]` | **Sim, quando preenchido** | Deve ser **institucional**, não pessoal. Ver a ressalva abaixo. |

**Nenhum dado particular foi encontrado publicado no site.** Não há
e-mail pessoal, telefone residencial, CPF, endereço residencial nem nome de
familiar em nenhuma das 9 páginas.

### ⚠️ Uma ressalva sobre autoria dos commits

O que **não** está no site, mas **está** no repositório público:

```
Davi Dantas <davichaves198@gmail.com>          — 5 commits (fev/2026)
almoxarifado 1 <almoxarifado 1@wattssolar.local> — 6 commits (ago/2026)
```

Duas observações:

1. **O e-mail pessoal fica público.** Todo commit carrega nome e e-mail do
   autor, e o GitHub os exibe na interface. Um endereço `@gmail.com`
   pessoal exposto num repositório público é alvo de coleta automatizada
   para spam e phishing. Se incomodar, o GitHub oferece um e-mail de
   encaminhamento anônimo (`ID+usuario@users.noreply.github.com`), em
   *Settings → Emails → Keep my email addresses private*. Passa a valer
   para commits futuros; os antigos só mudam reescrevendo o histórico.

2. **A segunda identidade não é uma pessoa.** `almoxarifado 1` é o nome do
   usuário do Windows e `wattssolar.local` é o nome de rede da máquina —
   o Git montou esse endereço sozinho porque `user.email` nunca foi
   configurado. Vaza, de forma discreta, o nome de usuário e o domínio
   interno da empresa. Para corrigir daqui em diante:

   ```powershell
   git config --global user.name "Davi Dantas"
   git config --global user.email "SEU-EMAIL-AQUI"
   ```

**Não é uma vulnerabilidade** — é exposição de informação, e a decisão de
corrigir ou não é sua.

---

# (b) Encontrado e **não corrigível** no GitHub Pages

O GitHub Pages serve arquivos estáticos e **não permite configurar
cabeçalhos HTTP de resposta**. Não há `.htaccess`, `_headers` nem
equivalente. Os itens abaixo têm solução conhecida, mas ela exige controle
sobre o servidor.

## b.1 — `frame-ancestors` não funciona em `<meta>`

Impede que terceiros embutam o site num `<iframe>` — a proteção contra
*clickjacking*. A especificação do CSP **ignora essa diretiva quando a
política vem por `<meta>`**; ela só vale via cabeçalho HTTP. O mesmo se
aplica a `X-Frame-Options`.

**Impacto real aqui: baixo.** O site não tem login, sessão nem ação
destrutiva de um clique. Clickjacking serve para induzir cliques
privilegiados, e não há nenhum. O risco concreto seria alguém embutir o
site numa página própria fingindo ser a EngPalmas — problema de imagem, não
de segurança técnica.

## b.2 — Cabeçalhos que só existem via HTTP

| Cabeçalho | Para que serve | Situação |
|---|---|---|
| `Strict-Transport-Security` | força HTTPS em acessos futuros | O GitHub Pages já serve por HTTPS e faz o redirecionamento, mas o cabeçalho não é configurável |
| `X-Content-Type-Options: nosniff` | impede o navegador de "adivinhar" tipo de arquivo | Não configurável |
| `Referrer-Policy` | controla o que é enviado ao navegar para fora | Não configurável globalmente. **Mitigado parcialmente**: o iframe recebeu `referrerpolicy="no-referrer"` no próprio elemento |
| `Permissions-Policy` | desliga câmera, microfone, geolocalização | Não configurável. Mitigado em parte pelo `sandbox` do iframe |
| `Cross-Origin-Opener-Policy` | isola o contexto de navegação | Não configurável |

## b.3 — Nenhum controle sobre o `<meta>` CSP em erro 404

A página de erro do GitHub Pages é gerada pela plataforma e não carrega o
nosso CSP.

## b.4 — Como resolver, se um dia importar

Colocar o site atrás de uma CDN que permita cabeçalhos personalizados
(Cloudflare, Netlify, Vercel — todos com plano gratuito para este porte)
resolve **b.1, b.2 e b.3 de uma vez**, sem alterar uma linha do código.
O site continuaria estático; muda só quem o entrega.

**Não recomendo fazer isso agora.** Para o risco real deste site, a
complexidade adicional não se paga. Vale reconsiderar se um dia houver
formulário com persistência ou área restrita.

---

# (c) Só se aplica se houver back-end

Nada nesta seção existe hoje. Está registrado para não ser esquecido caso a
arquitetura mude — o detalhamento está no `SEGURANCA.md`.

| Item | Por que não se aplica hoje |
|---|---|
| Injeção de SQL | Não há banco de dados nem consulta |
| Validação no servidor | Não há servidor de aplicação; a validação em JS é só conveniência de interface |
| Limite de requisições | Não há endpoint que aceite `POST` |
| Sanitização na exibição | Nenhum conteúdo de terceiro é exibido; todo o texto é estático e escrito por nós |
| Armazenamento de credenciais | Não há credencial nenhuma. O site não autentica em serviço algum |
| Sessão, cookie, autenticação | Não existem. O site não grava nada no navegador — nem cookie, nem `localStorage` |
| CSRF | Não há requisição que altere estado |
| Upload de arquivo | Não existe |
| Log de acesso e retenção | Não temos servidor; os logs são do GitHub |

**Sobre o formulário de contato atual:** ele não é exceção a nada disso. O
`submit` é interceptado, os campos viram texto e o navegador abre `wa.me`
com a mensagem pronta. **Nenhum dado do visitante passa por nós** — a
conversa é entre o navegador dele e o WhatsApp. É, do ponto de vista de
privacidade, a arquitetura mais limpa possível para um formulário.

---

# Recomendação em aberto: fontes locais

Não implementei — depende de decisão sua, porque envolve trazer arquivos de
terceiro para o repositório.

**Situação hoje:** as 9 páginas carregam a Montserrat do Google Fonts. Isso
significa que **todo visitante faz uma requisição para servidores do
Google**, entregando IP, `User-Agent` e horário do acesso, antes mesmo de o
site terminar de carregar.

**Medição real da folha que o site usa hoje:** 15 blocos `@font-face`, 15
arquivos `.woff2`, 167,7 KB somando todos os subconjuntos — que incluem
cirílico e vietnamita, inúteis para um site em português.

**Servindo localmente:**

- bastam os subconjuntos `latin` e `latin-ext` nos pesos 400, 700 e 900 →
  **6 arquivos, cerca de 65 KB**
- some a requisição a terceiro: privacidade do visitante preservada
- o CSP fica mais apertado: `style-src` cai para `'self'` e `font-src`
  deixa de ser necessário (`default-src 'none'` cobre)
- saem 2 `preconnect` e 1 folha de estilo externa bloqueante → primeira
  pintura mais rápida, o que importa num link aberto por dados móveis
- a Montserrat é licenciada em **SIL Open Font License 1.1**, que permite
  redistribuição — exige apenas que o arquivo `OFL.txt` acompanhe as fontes

**Custo:** 6 binários no repositório e a obrigação de manter o `OFL.txt`.

**Recomendo fazer.** É só me dar o aval que eu baixo, gero o `@font-face`
local, aperto o CSP e ajusto o `AUDITORIA.md`.

---

# Verificação de que nada quebrou

A instrução era conferir o console depois do CSP. **Não tenho navegador
nesta sessão** — então fiz a verificação equivalente por análise estática,
que confere exatamente o que o console acusaria como bloqueio:

| Verificação | Resultado |
|---|---|
| Hash de cada script inline confere com o conteúdo atual do arquivo | **9/9 páginas** |
| Script externo não coberto por hash | nenhum |
| Folha de estilo bloqueada pelo `style-src` | nenhuma |
| Imagem bloqueada pelo `img-src` | nenhuma |
| Iframe bloqueado pelo `frame-src` | nenhum |
| Atributo `style=` que exigiria `'unsafe-inline'` | nenhum |
| Tags balanceadas | 9/9 páginas |
| `style.css` — chaves balanceadas | sim |
| Classe usada no HTML sem regra no CSS | nenhuma |
| Link ou imagem quebrada | nenhum |

**Ainda assim, abra o `index.html` no navegador e olhe o console.** Um CSP
por hash é sensível a detalhe de codificação de arquivo, e essa é a única
verificação que fecha a questão de verdade. O que procurar: mensagens
começando com `Refused to execute` ou `Refused to load`. Se aparecerem, me
mande o texto — o ajuste é rápido.
