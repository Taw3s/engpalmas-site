# SEGURANÇA — requisitos para quando houver back-end

> **Este documento não descreve o site atual.** Hoje o site da EngPalmas é
> estático: HTML, CSS e JavaScript servidos pelo GitHub Pages, sem servidor
> de aplicação, sem banco de dados e sem autenticação. Nada aqui está
> implementado, e nada aqui precisa ser implementado enquanto essa
> arquitetura não mudar.
>
> Ele existe para o dia em que o formulário de contato deixar de abrir o
> WhatsApp e passar a **gravar** a mensagem em algum lugar. Nesse dia, tudo
> abaixo passa a valer de uma vez.

---

## O gatilho: o que muda quando aparece persistência

Hoje o formulário monta um texto e abre `wa.me`. Nenhum dado é recebido,
processado ou armazenado por nós — o navegador do visitante fala direto com
o WhatsApp. **Não há superfície de ataque de servidor porque não há
servidor.**

No momento em que existir um endpoint que receba `POST` e escreva em banco,
disco ou e-mail, o site passa a ter:

- dado de terceiro sob nossa guarda (LGPD)
- código nosso executando com privilégio
- um alvo que responde a requisições automatizadas

Os itens seguintes são o mínimo para esse cenário.

---

## 1. Validação no servidor

**A validação que existe hoje no formulário não conta.** `required` no HTML
e `checkValidity()` em JavaScript são conveniência para o usuário honesto.
Quem quer atacar não usa o formulário: manda a requisição direto.

Regra: **toda entrada é revalidada no servidor, sempre**, mesmo que o
JavaScript já tenha validado.

Para cada campo, definir antes de aceitar:

| Campo | Tipo | Tamanho máximo | Regra |
|---|---|---|---|
| nome | texto | 120 | não vazio depois de `trim` |
| empresa/órgão | texto | 160 | opcional |
| telefone | texto | 20 | apenas dígitos, parênteses, hífen, espaço, `+` |
| mensagem | texto | 2000 | não vazio depois de `trim` |

Princípios:

- **Lista de permissão, não de bloqueio.** Defina o que é aceito; não tente
  enumerar o que é perigoso. Listas de bloqueio sempre têm buraco.
- **Rejeite, não conserte.** Se veio fora do formato, devolva erro. Tentar
  "limpar" a entrada cria comportamento imprevisível.
- **Limite o tamanho do corpo da requisição** no servidor web, antes mesmo
  de o código ver o conteúdo. Um POST de 50 MB não deve chegar à aplicação.
- **Não confie em `Content-Type`, `Referer` ou cabeçalho nenhum** enviado
  pelo cliente. Todos são forjáveis.

---

## 2. Consultas parametrizadas

Se houver banco de dados, **toda** consulta usa parâmetros. Sem exceção,
sem "esse campo é só número".

Errado — concatenação:

```php
$sql = "INSERT INTO contatos (nome, telefone) VALUES ('$nome', '$telefone')";
```

Certo — parâmetros:

```php
$stmt = $pdo->prepare('INSERT INTO contatos (nome, telefone) VALUES (?, ?)');
$stmt->execute([$nome, $telefone]);
```

O que muda: na primeira versão, o conteúdo de `$nome` vira parte do comando
SQL. Na segunda, o banco recebe o comando e os dados separadamente, e o
dado nunca é interpretado como instrução.

Observações:

- Isso vale igualmente para Node (`pg`, `mysql2`), Python (`psycopg`,
  `sqlite3`) e qualquer outra linguagem. O nome muda, o princípio não.
- **Nome de tabela e de coluna não podem ser parametrizados.** Se algum dia
  forem dinâmicos, valide contra uma lista fixa no código.
- Use um ORM ou query builder se preferir, mas confirme que ele parametriza
  de fato — vários permitem "raw" e aí a proteção some.
- A conta do banco usada pela aplicação deve ter **só as permissões
  necessárias** (`INSERT` na tabela de contatos, provavelmente nada mais).
  Nada de conta administrativa em produção.

---

## 3. Limite de requisições

Sem limite, o formulário vira canal de spam e de custo. Um script simples
manda milhares de mensagens por minuto.

Camadas, da mais externa para a mais interna:

1. **Por IP, no servidor web ou na CDN** — algo como 5 envios por IP a cada
   10 minutos. É a barreira mais barata.
2. **Por sessão/campo, na aplicação** — bloqueio de envios idênticos
   repetidos em sequência.
3. **Campo armadilha (*honeypot*)** — um campo de formulário escondido por
   CSS. Humano nunca preenche; bot preenche. Se vier preenchido, descarta em
   silêncio. Custo quase zero e sem atrito para o usuário.
4. **CAPTCHA só se as camadas acima não bastarem.** Ele prejudica
   acessibilidade e afasta gente legítima. É último recurso, não primeiro.

Ao bloquear, responda com `429 Too Many Requests` e **não explique o
critério** na mensagem de erro.

---

## 4. Sanitização na exibição

A regra que evita a maior parte dos problemas: **guarde o dado como veio;
escape na hora de exibir.**

Escapar na entrada parece seguro e não é — corrompe o dado (um sobrenome
como `D'Ávila` vira lixo) e não protege, porque o mesmo dado pode ser
exibido depois em contexto diferente.

O escape depende de onde o dado vai aparecer:

| Contexto de saída | O que fazer |
|---|---|
| Corpo de HTML | escapar `< > & " '` |
| Atributo HTML | escapar e **sempre usar aspas** no atributo |
| Dentro de `<script>` | não faça isso; se inevitável, serialize como JSON |
| URL / query string | codificação percentual (`urlencode`) |
| Cabeçalho de e-mail | rejeitar `\r` e `\n` — senão permite injeção de cabeçalho |

No front-end, a regra prática que **já vale hoje e deve continuar valendo**:
use `textContent`, nunca `innerHTML`, para inserir qualquer coisa vinda de
fora. O JavaScript atual do site segue isso — a auditoria confirmou que não
há uma única ocorrência de `innerHTML`, `eval` ou `document.write`.

Se um dia houver painel para ler as mensagens recebidas, é **nele** que o
risco mora: é onde texto enviado por terceiro é exibido para alguém de
dentro da empresa.

---

## 5. Onde as credenciais devem viver

**Nunca no repositório.** O repositório é público, e o histórico do Git
guarda tudo: apagar o arquivo num commit posterior não remove nada — o
conteúdo continua recuperável em qualquer clone.

Ordem de preferência:

1. **Variáveis de ambiente da plataforma** (painel do provedor de
   hospedagem, GitHub Actions Secrets, etc.). É o padrão.
2. **Gerenciador de segredos** do provedor, se houver rotação automática.
3. **Arquivo `.env` fora do controle de versão**, apenas em
   desenvolvimento. O `.gitignore` deste repositório já bloqueia `.env`,
   `*.pem`, `*.key` e afins.

Junto com isso:

- **Versione um `.env.example`** com as chaves e valores fictícios, para
  documentar o que a aplicação espera sem revelar nada.
- **Credencial que já foi commitada é credencial queimada.** Não basta
  remover do histórico: tem que ser **revogada e trocada**. Trate como
  vazada a partir do instante do `push`.
- Credenciais diferentes para desenvolvimento e produção.
- Se houver envio de e-mail, a senha SMTP entra na mesma regra.

---

## 6. Itens que acompanham qualquer back-end

Não são o foco deste documento, mas ficam registrados para não serem
esquecidos no dia da migração:

- **HTTPS obrigatório**, com redirecionamento de HTTP e `Strict-Transport-Security`.
- **Cabeçalhos de segurança via HTTP**, que hoje o GitHub Pages não permite
  configurar: `Content-Security-Policy` (mais completo que a versão em
  `<meta>` usada agora), `X-Content-Type-Options: nosniff`,
  `Referrer-Policy`, `X-Frame-Options` ou `frame-ancestors`,
  `Permissions-Policy`.
- **Registro de acesso e de erro**, sem gravar dado pessoal nos logs.
- **Política de retenção**: por quanto tempo as mensagens de contato ficam
  guardadas, e quem tem acesso a elas. Exigência de LGPD, não detalhe
  técnico.
- **Backup do banco**, testado — backup que nunca foi restaurado não é
  backup.
- **Atualização de dependências**, com verificação de vulnerabilidades
  conhecidas.

---

## Resumo em uma linha

Enquanto o site for estático, nada aqui se aplica. No dia em que uma
requisição for gravada em algum lugar, **todos os seis itens passam a valer
simultaneamente** — não são etapas opcionais de um roteiro gradual.
