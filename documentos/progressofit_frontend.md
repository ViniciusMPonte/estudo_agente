# ProgressoFit - Frontend

O ProgressoFit é uma plataforma web acadêmica para monitoramento de treinos. O frontend permite visualizar progresso através de gráficos e relatórios, conquistar recompensas por gamificação e receber frases motivacionais personalizadas geradas por inteligência artificial.

O projeto está em desenvolvimento e foi criado pelos desenvolvedores Vinícius Menezes Pontes, Matheus Aquino de Andrade, Juan Pablo Lima Rassi, Isabela Saores dos Santos, William Santos de Santana e Arthur Moura Silva.

---

## Arquitetura do Frontend

O frontend do ProgressoFit segue o padrão MVC (Model-View-Controller), organizado nas seguintes camadas:

A camada **Models (DTOs)** é responsável pelas estruturas de dados e validações. A camada **Views** cuida da renderização de componentes e páginas. A camada **Controllers** concentra a lógica de negócio e a manipulação de eventos. A camada **Services** gerencia a comunicação com APIs e a manipulação de dados. O **Router** é responsável pelo gerenciamento de rotas e navegação.

---

## Integração do Frontend com o Backend

A comunicação entre o frontend e o backend é feita através da classe `ApiService`. Essa classe gerencia autenticação via JWT, requisições HTTP padronizadas, tratamento de erros e inserção automática de headers de autenticação.

---

## Funcionalidades do Frontend

As funcionalidades já implementadas no frontend são: sistema de autenticação com login e cadastro de usuários, controle de autorização com tokens JWT, arquitetura baseada em componentes reutilizáveis e customização de Bootstrap com Sass/SCSS.

---

## Pré-requisitos para executar o Frontend

Para executar o frontend do ProgressoFit, é necessário ter instalado o Node.js na versão 16 ou superior, o NPM e o Git.

Para verificar as versões instaladas, use os comandos abaixo:

```bash
node --version
npm --version
git --version
```

---

## Como executar o Frontend

**Passo 1 — Clone o repositório:**
```bash
gh repo clone ViniciusMPonte/ProgressoFit-Frontend
cd ProgressoFit-Frontend
```

**Passo 2 — Instale as dependências:**
```bash
npm install
```

**Passo 3 — Configure a URL da API:**

Certifique-se de que o backend esteja rodando em `http://localhost:8090`. Se necessário, ajuste a `baseURL` no arquivo `src/service/ApiService.js`:

```javascript
this.baseURL = 'http://localhost:8090';
```

**Passo 4 — Inicie o servidor de desenvolvimento:**
```bash
npm start
```

O comando acima inicia o Live Server automaticamente e abre a aplicação no navegador.

**Passo 5 — Acesse a aplicação:**

A aplicação estará disponível em `http://localhost:8080`.

---

## Customização do Bootstrap

O frontend usa Bootstrap com customização via Sass/SCSS. O arquivo principal de customização é `bootstrap.scss`, localizado em `src/styles/bootstrap/`.

A estrutura de arquivos do Bootstrap no projeto é:

```
./src/styles/bootstrap/
├── bootstrap.scss
├── bootstrap.css
├── bootstrap.css.map
├── package.json
├── package-lock.json
└── cheatsheet/
    ├── index.html
    ├── cheatsheet.css
    ├── cheatsheet.rtl.css
    └── cheatsheet.js
```

---

## Pré-requisitos para customizar o Bootstrap

Para customizar o Bootstrap, instale as ferramentas abaixo:

```bash
npm install -g sass
npm install -g postcss-cli autoprefixer
```

Para verificar as instalações:

```bash
sass --version
postcss --version
autoprefixer --info
```

---

## Como customizar o Bootstrap

**Passo 1 — Navegue até o diretório do Bootstrap:**
```bash
cd src/styles/bootstrap/
```

**Passo 2 — Instale as dependências locais:**
```bash
npm install
```

**Passo 3 — Edite as variáveis no arquivo `bootstrap.scss`:**

As principais categorias de variáveis disponíveis para personalização são cores, tipografia, espaçamentos e breakpoints. Exemplo de estrutura:

```scss
$primary: #your-brand-color;
$font-family-base: 'Your-Font', sans-serif;
$spacer: 1rem;
$border-radius: 0.5rem;

@import "~bootstrap/scss/bootstrap";
```

**Passo 4 — Compile o SCSS:**
```bash
sass bootstrap.scss bootstrap.css
```

Para recompilar automaticamente a cada alteração:
```bash
sass --watch bootstrap.scss:bootstrap.css
```

---

## Bootstrap Cheatsheet

O projeto inclui uma cheatsheet visual com todos os componentes Bootstrap disponíveis. Ela pode ser acessada em `http://localhost:8080/src/styles/bootstrap/cheatsheet/` após iniciar o servidor.

A cheatsheet contém exemplos visuais de cada componente, código HTML para copiar, variações de componentes, informações sobre responsividade e breakpoints, classes utilitárias e documentação de formulários.

---

## Comandos úteis do Sass e PostCSS

```bash
# Compilação básica
sass bootstrap.scss bootstrap.css

# Watch mode
sass --watch bootstrap.scss:bootstrap.css

# Compilação minificada
sass --style compressed bootstrap.scss bootstrap.css

# Com sourcemap
sass --source-map bootstrap.scss bootstrap.css

# Verificar sintaxe
sass --check bootstrap.scss

# Autoprefixer
postcss bootstrap.css --use autoprefixer -o bootstrap.css
```