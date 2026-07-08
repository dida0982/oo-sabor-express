# 🍽️ Sistema de Avaliação de Restaurantes

Projeto desenvolvido em Python durante os estudos na Alura, com o objetivo de praticar Programação Orientada a Objetos (POO) aplicada a um caso real: um sistema simples para cadastro de restaurantes e recebimento de avaliações de clientes. A aplicação simula o funcionamento de uma plataforma de reviews, calculando a média de notas de cada estabelecimento e exibindo um painel geral com status de atividade.

## ✅ Funcionalidades

- ✅ Cadastro de restaurantes com nome e categoria
- ✅ Formatação automática do nome (title case) e da categoria (uppercase)
- ✅ Recebimento de avaliações de clientes, com validação de nota (0 a 5)
- ✅ Cálculo automático da média de avaliações por restaurante
- ✅ Alternância de status ativo/inativo do restaurante
- ✅ Listagem geral de todos os restaurantes cadastrados, com nome, categoria, média e status
- ✅ Exibição amigável via `__str__` para representação simplificada do objeto

## 🛠️ Tecnologias e conceitos utilizados

- **Python 3**
- Programação Orientada a Objetos (classes, atributos encapsulados, `@property`, `@classmethod`)
- Modularização de código (organização em pacotes `model`)
- Listas e list comprehensions
- Formatação de strings com f-strings (`ljust`, alinhamento de colunas)
- Composição de objetos (`Restaurant` compõe `Assessment`)

## 📁 Estrutura do projeto

```
├── app.py                  # Ponto de entrada da aplicação
└── model/
    ├── restaurant.py        # Classe Restaurant
    └── assessment.py        # Classe Assessment
```

## ▶️ Como executar

```bash
python app.py
```

O script cadastra um restaurante de exemplo, registra algumas avaliações e imprime no terminal a listagem geral com nome, categoria, média de notas e status de atividade.

Este projeto reforça na prática conceitos essenciais de POO em Python, como encapsulamento de atributos, uso de propriedades computadas e métodos de classe para gerenciar coleções de objetos — uma base sólida para sistemas maiores que envolvam relacionamento entre entidades.

---

**Instrutores:**

**Guilherme Lima**

<img src="https://media.licdn.com/dms/image/v2/D4E03AQFodSTnO1qe9w/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1727180159904?e=1784764800&v=beta&t=r83QSJOEmBXirzSl8Ta2Jjw_9f_yPYTL8kmpj0xfiwE" width="150" alt="Foto de perfil">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-lima-developer/)

**Laís Urano**

<img src="https://github.com/uranolais.png" width="150" alt="Foto de perfil">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/la%C3%ADs-urano-9a41451b3/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/uranolais)

## 👤 Autor

**Guilherme Barros**

<img src="https://github.com/dida0982.png" width="150" alt="Foto de perfil">

Desenvolvedor Full Stack | Brasília, DF - Brasil

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-barros-6a0369209/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dida0982)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/guilherme_barros_jr/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://developerguilhermebarros.netlify.app/)

---

<p align="center">⭐ Se este projeto te ajudou de alguma forma, deixe uma estrela no repositório!</p>
