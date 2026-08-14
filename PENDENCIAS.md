# PENDÊNCIAS — Site EngPalmas

Documento gerado na refatoração do site. Lista **tudo que ficou como
placeholder** porque o dado não foi fornecido, mais o que precisa ser
decidido ou conseguido antes de publicar.

**Nada neste site foi inventado.** Todo dado que não foi informado aparece
na tela como um marcador laranja tracejado no formato `[[PREENCHER: chave]]`.
São **131 ocorrências** de **76 chaves distintas**, distribuídas nas 9 páginas.

> O salto de 67 para 131 é da Fase 7: o portfólio passou de 4 para 8 obras.
> Cada obra nova traz uma ficha técnica inteira em aberto. **Isso não é
> regressão** — são obras reais que antes nem apareciam no site.

Para localizar todos de uma vez, rode na pasta do projeto:

```powershell
Select-String -Path *.html -Pattern '\[\[PREENCHER:.*?\]\]'
```

---

## 🔴 BLOQUEIA A PUBLICAÇÃO

Sem estes itens o site não deve ir ao ar — ou aparece quebrado, ou aparece
com marcador de pendência à vista de um pregoeiro.

### 1. Domínio do site

O endereço final ainda não existe no código. Está como `SEU-DOMINIO-AQUI.com.br`
em **31 lugares** (7 no index, 6 em cada página de obra).

Isso afeta `canonical`, `og:url`, `og:image`, `twitter:image` e o JSON-LD.

**Consequência prática:** enquanto não for trocado, **colar o link no WhatsApp
continua mostrando retângulo vazio** — que é exatamente o problema que a
refatoração deveria resolver. O og:image precisa de URL absoluta e real.

Substituir com:

```powershell
Get-ChildItem *.html | ForEach-Object {
    (Get-Content $_.FullName -Raw) -replace 'SEU-DOMINIO-AQUI\.com\.br', 'engpalmas.com.br' |
        Set-Content $_.FullName -Encoding utf8
}
```

### 2. Dados cadastrais da empresa

Aparecem na seção **A Empresa** e no **rodapé de todas as 5 páginas**.

| Chave | Onde aparece | Ocorrências |
|---|---|---|
| `razao-social` | A Empresa + JSON-LD de todas as páginas | 6 |
| `cnpj` | A Empresa + rodapé de todas + JSON-LD | 11 |
| `ano-de-fundacao` | A Empresa + JSON-LD | 2 |
| `crea-pj` | A Empresa + rodapé de todas | 6 |
| `nome-responsavel-tecnico` | A Empresa | 1 |
| `crea-responsavel-tecnico` | A Empresa | 1 |
| `cep` | Localização + JSON-LD de todas | 6 |
| `email-institucional` | Rodapé (texto + link `mailto:`) | 2 |

> **O CNPJ é o item de maior peso da lista.** Você mesmo apontou: rodapé com
> CNPJ é sinal de seriedade. Hoje ele aparece como marcador laranja em todas
> as páginas.

---

## 🟠 CAPACIDADE TÉCNICA

Seção nova, criada do zero. Os quatro números estão vazios.

| Chave | Rótulo na tela |
|---|---|
| `n-obras-entregues` | Obras entregues |
| `m2-construidos` | m² construídos |
| `anos-de-atuacao` | Anos de atuação |
| `n-orgaos-atendidos` | Órgãos atendidos |

**Cuidado com esses números.** Eles são verificáveis por qualquer comissão.
Prefira subestimar. Se não houver como apurar os m² com segurança, é melhor
me pedir para **remover o card** do que publicar um número frágil — um dado
contestado numa impugnação custa mais do que um card a menos.

---

## 🟠 FICHA TÉCNICA DAS 4 OBRAS

Os campos abaixo são exatamente os de um **atestado de capacidade técnica**.
São o motivo pelo qual a comissão abre a página.

### Fórum de Natividade — `obra-natividade.html`

- [ ] `orgao-contratante-natividade`
- [ ] `objeto-contrato-natividade`
- [ ] `modalidade-natividade`
- [ ] `area-natividade`
- [ ] `prazo-natividade`

Já preenchidos (vieram do site antigo — **confirmar se estão corretos**):
Local: Natividade / TO · Escopo: construção civil completa e subestação
abrigada de 34,5 kV · Situação: Concluída.

> A placa na fachada da foto diz "PODER JUDICIÁRIO — FÓRUM DA COMARCA DE
> NATIVIDADE". Isso **sugere** o TJTO como contratante, mas não confirma:
> a EngPalmas pode ter sido subcontratada. Não preenchi por isso.

### Fórum de Goiatins — `obra-goiatins.html`

- [ ] `orgao-contratante-goiatins`
- [ ] `objeto-contrato-goiatins`
- [ ] `modalidade-goiatins`
- [ ] `area-goiatins`
- [ ] `prazo-goiatins`

Já preenchidos (**confirmar**): Local: Goiatins / TO · Escopo: obra civil e
elétrica integrada, baixa e média tensão · Situação: Concluída.

## 🟠 EDUCAÇÃO — 2 obras *(páginas novas, Fase 7)*

### CEM Félix Camoa — `obra-cem-felix-camoa.html`

Confirmados: nome da obra e cidade (**Porto Nacional / TO**). O resto:

- [ ] `descricao-felix-camoa` — parágrafo descritivo da página
- [ ] `orgao-contratante-felix-camoa`
- [ ] `objeto-contrato-felix-camoa`
- [ ] `modalidade-felix-camoa`
- [ ] `area-felix-camoa`
- [ ] `prazo-felix-camoa`
- [ ] `escopo-felix-camoa`
- [ ] `situacao-felix-camoa`

### Escola Estadual Henrique Cirqueira Amori — `obra-escola-henrique-cirqueira.html`

- [ ] `nome-completo-henrique-cirqueira` — **o nome pode estar truncado.**
      Confirmar a grafia oficial completa. Aparece no `<h1>`, no `<title>`,
      no card da home e na ficha.
- [ ] `cidade-henrique-cirqueira` — **desconhecida.** Aparece no card da
      home e na ficha.
- [ ] `descricao-henrique-cirqueira`
- [ ] `orgao-contratante-henrique-cirqueira`
- [ ] `objeto-contrato-henrique-cirqueira`
- [ ] `modalidade-henrique-cirqueira`
- [ ] `area-henrique-cirqueira`
- [ ] `prazo-henrique-cirqueira`
- [ ] `escopo-henrique-cirqueira`
- [ ] `situacao-henrique-cirqueira`

---

## 🟠 ILUMINAÇÃO PÚBLICA — 3 obras *(páginas novas, Fase 7)*

Confirmados em todas: nome da obra e município. O resto está em aberto.

**Estas três fichas não têm "Área construída"** — não se aplica a obra de
iluminação. No lugar entram **`pontos-*`** (pontos instalados) e
**`extensao-*`** (extensão de via atendida), que são as métricas que
constam de atestado desse tipo de contrato. Os outros 5 campos de atestado
permanecem iguais aos das demais obras.

### Miranorte — `obra-iluminacao-miranorte.html`

- [ ] `descricao-miranorte`
- [ ] `orgao-contratante-miranorte` — provavelmente a Prefeitura, confirmar
- [ ] `objeto-contrato-miranorte`
- [ ] `modalidade-miranorte`
- [ ] `pontos-miranorte`
- [ ] `extensao-miranorte`
- [ ] `prazo-miranorte`
- [ ] `escopo-miranorte`
- [ ] `situacao-miranorte`

### Monte do Carmo — `obra-iluminacao-monte-do-carmo.html`

- [ ] `descricao-monte-do-carmo`
- [ ] `orgao-contratante-monte-do-carmo`
- [ ] `objeto-contrato-monte-do-carmo`
- [ ] `modalidade-monte-do-carmo`
- [ ] `pontos-monte-do-carmo`
- [ ] `extensao-monte-do-carmo`
- [ ] `prazo-monte-do-carmo`
- [ ] `escopo-monte-do-carmo`
- [ ] `situacao-monte-do-carmo`

### Nova Rosalândia — `obra-iluminacao-nova-rosalandia.html`

- [ ] `descricao-nova-rosalandia`
- [ ] `orgao-contratante-nova-rosalandia`
- [ ] `objeto-contrato-nova-rosalandia`
- [ ] `modalidade-nova-rosalandia`
- [ ] `pontos-nova-rosalandia`
- [ ] `extensao-nova-rosalandia`
- [ ] `prazo-nova-rosalandia`
- [ ] `escopo-nova-rosalandia`
- [ ] `situacao-nova-rosalandia`

---

## 🟠 OUTRAS — `obra-ananas.html`

Você confirmou que é obra real, mas ela **não estava na lista das 7** e não
tem categoria. Por isso aparece num grupo "Outras Obras" na home, separado
das três categorias técnicas.

- [ ] `categoria-ananas` — **define em qual grupo ela entra.** Se for uma
      das três categorias existentes, eu movo o card e o grupo "Outras
      Obras" desaparece.
- [ ] `descricao-ananas`
- [ ] `orgao-contratante-ananas`
- [ ] `objeto-contrato-ananas`
- [ ] `modalidade-ananas`
- [ ] `area-ananas`
- [ ] `prazo-ananas`
- [ ] `escopo-ananas`
- [ ] `situacao-ananas`

> **Nota:** a página `obra-em-andamento.html` foi removida na Fase 7. Era um
> card genérico que não correspondia a nenhuma obra real da lista. Se existir
> mesmo uma obra em execução hoje, ela precisa entrar como registro próprio.

---

## 📷 FOTOS — o item de maior retorno da lista

**Das 8 obras, apenas 2 têm foto** — os fóruns de Natividade e Goiatins. As
outras 6 mostram um placeholder com o ícone da categoria: honesto, mas neutro.

- [ ] **CEM Félix Camoa** — Porto Nacional / TO
- [ ] **Escola Estadual Henrique Cirqueira Amori**
- [ ] **Iluminação Pública de Miranorte**
- [ ] **Iluminação Pública de Monte do Carmo**
- [ ] **Iluminação Pública de Nova Rosalândia**
- [ ] **Obra de Ananás**

> Se seu pai tiver qualquer foto dessas obras no celular, isso vale mais do
> que o CNPJ. Foto de obra entregue é a prova visual que a comissão quer —
> os dois fóruns que já estão no site funcionam justamente por isso.

Para as três de iluminação pública, foto noturna da via iluminada é o que
comprova o serviço. Foto de poste durante o dia não mostra resultado.

**Como entregar:** JPG, na horizontal, mínimo 800×533. Coloque na pasta do
projeto e me avise o nome do arquivo — eu troco o placeholder e ajusto o
`og:image` da página (hoje as 6 emprestam as fotos de Natividade e Goiatins
para a prévia do WhatsApp não sair vazia).

---

## ✅ O QUE JÁ FOI RESOLVIDO

Para você não procurar o que já está feito.

**Bugs da sua lista:**

- [x] Tags `<link>` das fontes com sintaxe `[url](url)` — corrigidas. **A
      Montserrat nunca havia carregado no index.**
- [x] Formulário Formspree `SEU_CODIGO_AQUI` — substituído por bloco que monta
      a mensagem e abre `wa.me/5563984222219` em nova aba, sem serviço externo.
- [x] Menu sumindo no celular — hambúrguer acessível, com `aria-expanded`,
      fecha com Esc e fecha ao clicar num item.
- [x] Âncoras atrás do header fixo — `scroll-margin-top` aplicado.
- [x] Cards de Ananás e Obra em Andamento sem link — agora levam a páginas
      de detalhe próprias, no mesmo padrão dos fóruns.
- [x] Mapa com marcador da "Watts Solar" — trocado por embed só de endereço.
- [x] `<span>` de fechar o modal — virou `<button>`, com Esc, trap de foco,
      `role="dialog"` e retorno do foco ao fechar.
- [x] Ordem da nav diferente da ordem da página — alinhadas.

**Bugs encontrados no diagnóstico e corrigidos:**

- [x] **8 links apontavam para `testes.html`, arquivo inexistente.** Quem
      entrasse numa página de obra ficava sem nenhum caminho de volta.
- [x] `.section-title` não existia no CSS — os títulos de seção renderizavam
      no padrão do navegador, sem o peso 900 em caixa alta.
- [x] Site ficava invisível sem JavaScript (`.scroll-hidden` com `opacity:0`
      e nada revertendo). Agora o estado inicial só é aplicado quando há JS.
- [x] `<footer id="contato">` duplicado em `obra-goiatins.html`.
- [x] Seção de obras sem recuo lateral — cards encostavam na borda da tela.
- [x] `contato.html` (arquivo de 0 bytes, nunca preenchido) — removido.

**Requisitos técnicos:**

- [x] Meta description e Open Graph completos nas 5 páginas.
- [x] JSON-LD `GeneralContractor` com endereço, telefone e área de atuação.
- [x] `loading="lazy"` e `width`/`height` em todas as imagens abaixo da dobra.
- [x] Imagem de fundo desativada abaixo de 768px, substituída por gradiente.
- [x] `prefers-reduced-motion` respeitado em todas as animações.
- [x] Contraste AA. **O problema real não era o cinza:** `#cccccc` sobre o
      preto dá 12,3:1 e o laranja sobre preto dá 6,2:1 — ambos aprovados. Quem
      reprovava era **texto branco sobre `#FF5700` (3,17:1)**, em todos os
      botões. Botões agora usam `#C43F00` → **5,17:1**, com hover `#9E3300`
      → 7,17:1. O `#FF5700` original continua em títulos, bordas e checks.
- [x] `lang="pt-BR"` e todo o texto em português do Brasil.
- [x] CSS desminificado e organizado em 20 seções comentadas.

---

## ⚙️ DECISÕES AINDA EM ABERTO

- [ ] **Arquivos de estudo na pasta do site.** `materiais.py`,
      `precos_do_cliente.py`, `saldo = 0.py`, `setur.py` e `portedecelular.zip`
      sobem junto se você publicar a pasta inteira. Li os quatro: são
      exercícios de Python com dados fictícios, **sem credencial e sem dado de
      cliente real**. Não há risco de vazamento; é só organização. Aguardando
      sua decisão para mover para `_estudos/`.

- [ ] **Duplicatas de imagem.** O arquivo sem extensão
      `apps.8453.13655054093851568...` tem hash idêntico ao `whatsapp.png`.
      E `461250122_..._n - Copia.jpg` é cópia do outro `461250122_...n.jpg`.
      Posso apagar as duplicatas — o `461250122_...n.jpg` (logo 150×150) está
      **em uso como favicon**, esse fica.

- [ ] **`rasgaCarniça.png`.** É o Fórum de Natividade recortado em fundo
      branco, hoje sem uso nenhum. Dá para aproveitar na página de Natividade.
      Atenção: o `ç` no nome do arquivo quebra em parte das hospedagens
      estáticas — renomear exigiria sua autorização (regra de não renomear
      imagens).

- [ ] **Telefone fixo (63) 3215-1305.** Confirmar se ainda está ativo. Está
      publicado como link clicável em todas as páginas.

- [ ] **Coordenadas da sede — CONFERIR.** O mapa deixou de buscar pelo
      endereço, porque o Google casava a busca com o negócio cadastrado no
      local e exibia o pin da "Watts Solar". Agora ele fixa um pin neutro nas
      coordenadas `-10.2407635, -48.3384534`.

      **Essas coordenadas vieram do embed original do projeto** — o mesmo que
      apontava para a Watts Solar. Ou seja, marcam o ponto que já estava lá,
      não um endereço verificado por mim. Se a EngPalmas não fica exatamente
      nesse ponto, o mapa aponta para o lugar errado.

      **Como conferir:** abra o Google Maps, ache a sede, clique com o botão
      direito sobre ela e escolha a primeira opção (as coordenadas). Cole aqui
      e eu troco:

      ```
      index.html → linha do <iframe> → src="https://www.google.com/maps?q=LAT,LONG&z=17&hl=pt-BR&output=embed"
      ```

---

## 📋 CHECKLIST PARA CONVERSAR COM SEU PAI

Ordem sugerida — do que mais pesa para o que menos pesa:

1. **Fotos das obras de Ananás e da obra em andamento.** Pode ser foto de
    celular. É o maior ganho isolado do site.
2. **CNPJ e razão social.** Sai na Consulta QSA da Receita, em 1 minuto.
3. **Nome da obra em andamento** e a cidade dela.
4. **Registro CREA/TO da empresa** e o nome + CREA do responsável técnico.
    Está na Certidão de Registro e Quitação do CREA.
5. **Ficha das 4 obras** — órgão contratante, objeto, modalidade, área e
    prazo. **Atalho:** se ele tiver os **atestados de capacidade técnica**
    ou as **ARTs** dessas obras, os 5 campos estão todos lá dentro, prontos.
    É literalmente copiar.
6. **Números da capacidade técnica** — obras entregues, m², anos, órgãos.
7. **E-mail institucional e CEP** da sede.
8. **Ano de fundação** da empresa.
9. **Domínio** — se já existe algum registrado, ou se precisa registrar.

> **Dica sobre o item 5:** peça os atestados em PDF. Além de preencher as
> fichas, eles abrem uma possibilidade forte: publicar os atestados como
> anexo no site. Para quem avalia consórcio ou subcontratação, atestado
> disponível para download vale mais do que qualquer texto descritivo.
