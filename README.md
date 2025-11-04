# Book API – Consulta Pública de Livros para Projetos de Machine Learning

Este projeto foi desenvolvido como parte de um desafio técnico para construir uma infraestrutura completa de dados voltada para sistemas de recomendação de livros. Ele realiza web scraping do site [Books to Scrape](https://books.toscrape.com/), armazena os dados localmente e os disponibiliza via uma API RESTful pública.

---

## Objetivo

Criar um pipeline de dados escalável e reutilizável que permita:

- Extração automatizada de dados de livros
- Armazenamento estruturado em CSV
- Disponibilização via API pública com FastAPI
- Integração futura com modelos de machine learning

---

---

## Instalação e Execução Local

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/book-api.git
cd book-api

# Instale as dependências
pip install -r requirements.txt

# Execute o scraping
python scripts/scrape_books.py

# Inicie a API
uvicorn api.main:app --reload
```

Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API em Produção

Acesse a API pública em:

```
https://book-api.onrender.com
```

Documentação interativa:  
[https://book-api.onrender.com/docs](https://api-publica-para-consulta-de-livros.onrender.com/docs#)

---

## Endpoints Disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/v1/books` | Lista todos os livros disponíveis |
| `GET` | `/api/v1/books/{id}` | Retorna detalhes de um livro específico |
| `GET` | `/api/v1/books/search` | Busca por título e/ou categoria |
| `GET` | `/api/v1/categories` | Lista todas as categorias disponíveis |

---

## Exemplos de Uso

### Listar todos os livros

```http
GET /api/v1/books/
```

### Buscar livros por categoria

```http
GET /api/v1/books/?category=Science
```

### Detalhes de um livro específico

```http
GET /api/v1/books/42
```

### Listar categorias

```http
GET /api/v1/categories
```
