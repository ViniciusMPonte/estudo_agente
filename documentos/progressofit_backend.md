# ProgressoFit - Backend

O ProgressoFit é uma plataforma web acadêmica para monitoramento de treinos. O backend fornece a infraestrutura para que os usuários registrem diariamente exercícios, cargas, tempos, sensações e outras métricas. Esses dados são transformados em relatórios e gráficos de evolução. O sistema também integra inteligência artificial para gerar mensagens motivacionais e recomendações de treino personalizadas com base no perfil e desempenho de cada usuário.

O projeto está em desenvolvimento e foi criado pelos desenvolvedores Vinícius Menezes Pontes, Matheus Aquino de Andrade, Isabela Soares dos Santos e Juan Pablo Lima Rassi.

---

## Tecnologias utilizadas no Backend

O backend do ProgressoFit utiliza Java 17 com Spring Boot como linguagem e framework principal. O banco de dados utilizado é o PostgreSQL. A containerização é feita com Docker e Docker Compose. A ferramenta de build utilizada é o Gradle.

---

## Pré-requisitos para executar o Backend

Para executar o backend do ProgressoFit, é necessário ter instalado o Java 17 ou superior, o Docker com Docker Compose e o Git.

Para verificar as versões instaladas, use os comandos abaixo:

```bash
java -version
docker --version
docker-compose --version
```

---

## Como executar o Backend

**Passo 1 — Clone o repositório:**
```bash
gh repo clone ViniciusMPonte/ProgressoFit-Backend
cd ProgressoFit-Backend
```

**Passo 2 — Inicie os serviços com Docker:**
```bash
docker-compose up
```

O comando acima configura todas as dependências necessárias e inicializa o banco de dados PostgreSQL, deixando-o pronto para conexão.

**Passo 3 — Execute a aplicação Spring Boot:**
```bash
./gradlew bootRun
```

**Passo 4 — Acesse a aplicação:**

A aplicação estará disponível em `http://localhost:8090`.