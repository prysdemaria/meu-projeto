# 💳 Analise de Isenção de Anuidade do Cartão de Credito de um cliente 

Este projeto automatiza a verificação de cobrança de anuidade de cartões de crédito utilizando a biblioteca **Pandas**. O objetivo é cruzar dados de clientes com as políticas de isenção do banco para determinar quem deve ou não pagar a taxa mensal/anual.

## 📋 Regras de Isenção

O sistema avalia duas condições principais para conceder o benefício da anuidade zero:

1.  **Regra de Investimento:** Isenção concedida caso o cliente possua um montante investido acima de um valor determinado (ex: R$ 50.000,00).
2.  **Regra de Gasto Mensal:** Isenção concedida caso o gasto na fatura do mês atual supere um limite estabelecido (ex: R$ 5.000,00).

> **Nota:** Se o cliente atender a **qualquer uma** das regras acima, ele fica isento da cobrança.

---

## 🛠️ Tecnologias e Desenvolvimento

* **Linguagem:** Python 3.x
* **Biblioteca:** Pandas (Manipulação de DataFrames)
* **Metodologia:** * `Versão 1.0`: Criada manualmente para validação da lógica de negócio.
    * `Versão 2.0 (Prototipagem)`: Em desenvolvimento, utilizando recursos de IA para otimização de performance e limpeza de dados.

---

## 📂 Estrutura de Arquivos

* `base_clientes.csv`: Arquivo de entrada com dados de investimentos e gastos.
* `analise_anuidade.py`: Script principal desenvolvido manualmente.
* `prototipo_ia_em_andamento.py`: Versão em evolução assistida por IA (Gemini).

---

