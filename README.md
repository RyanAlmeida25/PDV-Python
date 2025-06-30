## IMPORTAÇÕES

```python
import os
import datetime
import dados
from dados import clientes, produtos, vendedores, lista_produtos, comissao_vendedores, vendas, imposto, produtos_vendidos
```

- **`datetime`**: Utilizada para registrar a data e hora da compra.
- **`dados`**: Módulo com listas globais que armazenam os dados persistentes.
- **Listas importadas**:
  - `clientes`: lista de dicionários com os dados dos clientes.
  - `produtos`: lista de dicionários com os produtos cadastrados.
  - `vendedores`: lista de dicionários com os vendedores.
  - `lista_produtos`: produtos adicionados temporariamente durante uma compra.
  - `comissao_vendedores`: histórico de comissões por venda.
  - `vendas`: histórico das compras realizadas.
  - `imposto`: registros dos impostos calculados por venda.
  - `produtos_vendidos`: nomes dos produtos vendidos (para relatório).

---

- `os`: biblioteca padrão do Python para manipulação de caminhos e arquivos.
- `from dados import ...`: importa as listas globais onde os dados são armazenados.

---

## FUNÇÃO: dados_cliente

```python
def dados_cliente(codigo, nome):
```

- Cria um dicionário `cliente` com os dados recebidos e adiciona à lista global `clientes`.
- Exibe mensagem de sucesso ao cadastrar.

---

## FUNÇÃO: cadastro

```python
def cadastro():
```

- **Fluxo:**
  1. Pergunta se o usuário deseja cadastrar um novo cliente.
     - Se não, encerra o processo.
  2. Inicia um `while True` para permitir múltiplos cadastros.
     - Solicita `codigo` e `nome`.
     - Chama `dados_cliente()` para armazenar.
     - Chama `salvar_dados()` para persistência.
     - Pergunta se deseja continuar.
  3. Encerra com mensagem final.

---

## FUNÇÃO: dados_produto

```python
def dados_produto(codigo, nome, valor, estoque):
```

- Cria um dicionário com os dados do produto.
- Adiciona à lista global `produtos`.
- Exibe mensagem de sucesso.

---

## FUNÇÃO: cadastro_produto

```python
def cadastro_produto():
```

- **Fluxo:**
  1. Pergunta se deseja cadastrar um produto.
  2. Em caso afirmativo:
     - Solicita `codigo`, `nome`, `valor`, `estoque`.
     - Chama `dados_produto()` para armazenar.
     - Chama `salvar_dados()` para persistência.
     - Pergunta se deseja continuar.
  3. Encerra o processo com mensagem final.

---

## FUNÇÃO: dados_vendedores

```python
def dados_vendedores(codigo, nome):
```

- Cria um dicionário com os dados do vendedor.
- Adiciona à lista global `vendedores`.
- Exibe mensagem de sucesso.

---

## FUNÇÃO: cadastro_vendedor

```python
def cadastro_vendedor():
```

- **Fluxo:**
  1. Pergunta se deseja cadastrar um vendedor.
  2. Em caso afirmativo:
     - Solicita `codigo` e `nome`.
     - Chama `dados_vendedores()`.
     - Chama `salvar_dados()`.
     - Pergunta se deseja continuar.
  3. Encerra o processo com mensagem final.

---

## FUNÇÃO: salvar_dados

```python
def salvar_dados():
```

- Define o caminho do arquivo `dados.py`.
- Abre o arquivo e escreve:
  - Lista `clientes`
  - Lista `produtos`
  - Lista `vendedores`
- Em caso de sucesso, exibe mensagem.
- Em caso de erro, exibe exceção capturada.


## FUNÇÃO: verificar_cliente

```python
def verificar_cliente():
```

### Objetivo:
Verificar se o código informado pertence a um cliente já cadastrado.

### Fluxo:
1. Solicita o código do cliente via `input`.
2. Tenta converter para inteiro — se falhar, repete a função.
3. Procura o cliente na lista `clientes`.
4. Se encontrado:
   - Exibe nome do cliente.
   - Chama `verificar_vendedor()`.
5. Se não encontrado:
   - Oferece a opção de cadastro (chama `cadastro()`).
   - Retorna `False` se o usuário não desejar cadastrar.

---

## FUNÇÃO: verificar_vendedor

```python
def verificar_vendedor():
```

### Objetivo:
Verificar se o vendedor informado está cadastrado.

### Fluxo:
1. Solicita o código do vendedor.
2. Verifica na lista `vendedores`.
3. Se encontrado:
   - Exibe nome e retorna o `vendedor` (dicionário).
4. Se não:
   - Oferece a opção de cadastrar.
   - Se sim, chama `cadastro_vendedor()` e reinicia verificação.
   - Caso contrário, retorna `False`.

---

## FUNÇÃO: verificar_produto

```python
def verificar_produto(vendedor):
```

### Objetivo:
Verificar a existência de um produto e adicioná-lo à lista de compra (`lista_produtos`).

### Fluxo:
1. Solicita código do produto.
2. Busca na lista `produtos`.
3. Se encontrado:
   - Verifica se há estoque suficiente.
   - Adiciona o produto em `lista_produtos`.
   - Pergunta se deseja adicionar mais produtos.
   - Se sim, chama a si mesma (recursão).
4. Se não encontrado:
   - Oferece opção de cadastrar via `cadastro_produto()`.
   - Retorna `False` caso usuário recuse o cadastro.

---

## FUNÇÃO: verificacao_compra

```python
def verificacao_compra():
```

### Objetivo:
Executa a verificação de cliente antes da compra.

- Chama `verificar_cliente()` e imprime o resultado da verificação.

---

## FUNÇÃO: compra

```python
def compra():
```

### Objetivo:
Realiza o processo completo de compra.

### Fluxo completo:
1. Exibe mensagem inicial.
2. Executa `verificar_vendedor()` e armazena vendedor.
3. Chama `verificar_produto()` (pode adicionar múltiplos produtos).
4. Exibe todos os produtos em `lista_produtos`.
5. Pergunta se deseja finalizar a compra.
6. Se sim:
   - Soma os valores de todos os produtos.
   - Cria dicionário com quantidade de cada produto vendido (por código).
   - Atualiza o estoque dos produtos.
   - Calcula a comissão (5%) e salva em `comissao_vendedores`.
   - Cria dicionário `total_vendas` com data/hora.
   - Exibe resumo da compra (nomes, valor, vendedor, data).
   - Adiciona produtos vendidos em `produtos_vendidos`.
   - Limpa `lista_produtos`.
   - Salva os dados em `dados.py`.

---

## FUNÇÃO: calcular_imposto

```python
def calcular_imposto():
```

### Objetivo:
Calcula imposto total das vendas já realizadas.

### Detalhes:
- Soma o campo `'valor total'` de cada venda.
- Aplica uma taxa fixa de 25%.
- Exibe o valor do imposto.
- Registra o cálculo em `imposto` com data/hora.
- Salva dados.

---

## FUNÇÃO: relatorio

```python
def relatorio():
```

### Objetivo:
Exibir um relatório completo do sistema.

### Exibe:
- Data/hora atual.
- Lista completa de vendas (`vendas`).
- Lista de produtos vendidos (`produtos_vendidos`).
- Histórico de impostos (`imposto`).
- Comissões por vendedor (`comissao_vendedores`).

### Observação:
- Após exibir, esvazia a lista `produtos_vendidos`.
- Salva os dados.

---

## NOTAS TÉCNICAS

- A função `compra()` evita duplicações de produtos no inventário, mas permite repetições do mesmo produto na mesma compra.
- O uso de listas globais exige cuidado com a concorrência em ambientes multiusuário.
- A função `salvar_dados()` sobrescreve `dados.py`, por isso é importante manter backups em caso de falha.

---

## SUGESTÕES DE MELHORIA

- Separar dados persistentes em arquivos `.json` ou `.csv`, eliminando dependência de sobrescrever código.
- Implementar verificação de tipo em todos os inputs.
- Implementar interface gráfica com bibliotecas como `Tkinter` ou `PyQt`.
- Centralizar a verificação de código duplicado em funções utilitárias para evitar repetição de lógica.

========================================  
FIM DA DOCUMENTAÇÃO  
========================================