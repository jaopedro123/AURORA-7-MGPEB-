## 🚀 MGPEB — Módulo de Gerenciamento de Pouso e Estabilização de Base

> Atividade Integradora — Missão Aurora Siger MGPEB 
> Disciplina: Algoritmos e Estruturas de Dados / Engenharia de Sistemas Espaciais

## 📋 Descrição do Projeto

O **MGPEB** é um sistema crítico de controle de tráfego orbital e descida segura desenvolvido para a colônia marciana Aurora Siger. O software simula a organização de módulos espaciais, executa algoritmos de busca e ordenação para priorizar pousos e utiliza lógica booleana rigorosa para autorizar a descida, garantindo a integridade física da base e dos colonos.


## 🗂️ Estrutura do Projeto
```
│
├── mgpeb.py                   # Código-fonte principal (Python)
└── relatorio_final_completo   # Documentação técnica e modelagem
```



---

## ⚙️ Funcionalidades

| Módulo | Descrição |
|---|---|
| **Gestão de Fila (FIFO)** | Organização cronológica dos módulos que chegam à órbita. |
| **Ordenação Avançada** | Reorganização da fila por **Prioridade** (Bubble Sort) ou **Combustível** (Selection Sort). |
| **Busca e Localização** | Busca linear de recursos e busca binária (O(log n)) para prioridades específicas. |
| **Lógica de Decisão** | Autorização baseada em portas AND (condições normais) e OR (emergências). |
| **Histórico de Alertas** | Registro de eventos críticos em estrutura de **Pilha (LIFO)** para resposta imediata. |
| **Análise de Emergência** | Identificação automática de níveis críticos de combustível (< 15%). |

---

## 🌡️ Regras de Autorização (Lógica Booleana)

Para um pouso ser autorizado, o sistema valida os seguintes critérios:

* **Protocolo de Segurança (AND):**
    * Combustível ≥ 25% **E** Área de Pouso Disponível **E** Sensores OK **E** Clima Favorável.
* **Protocolo de Emergência (OR):**
    * Combustível < 15% **OU** (Criticidade Alta **E** Combustível < 25%).

---

## 📐 Modelagem Matemática (Gravity Turn)

A trajetória de descida é calculada através de uma função quadrática que modela a altitude ($h$) em relação ao tempo ($t$), considerando a desaceleração dos retrofoguetes:

$$h(t) = h_0 + v_0 t + \\frac{1}{2} a t^2$$

Onde o objetivo é atingir o vértice da parábola no solo ($h=0$) com velocidade nula para evitar impactos catastróficos.

---

## ▶️ Instruções de Execução

### Pré-requisitos

- **Python 3.8** ou superior.
- Nenhuma biblioteca externa é necessária (utiliza apenas `collections.deque` da biblioteca padrão).

### Como rodar

``` bash
# Acesse o diretório do projeto
cd aurora-7

# Execute o sistema
python mgpeb.py

---

🖥️ Print da Execução (Exemplo)
============================================================
  PROCESSAMENTO DA FILA DE POUSO
============================================================
  ✔ HAB-01 → POUSO AUTORIZADO
  ⚠ MED-05 → POUSO DE EMERGÊNCIA (prioridade máxima)
  ✘ LOG-04 → AGUARDANDO (condições insuficientes)

============================================================
  HISTÓRICO DE ALERTAS (LIFO — pilha)
============================================================
  [EMERGÊNCIA] MED-08: combustível=12% | criticidade=alta
  [EMERGÊNCIA] MED-05: combustível=30% | criticidade=alta
============================================================

```


##  📐 Estruturas de Dados Aplicadas

- **Fila (deque):** Controle de tráfego e ordem de chegada.  

- **Pilha (list.pop):** Registro de alertas e eventos de segurança (LIFO).  

- **Listas e Dicionários:** Armazenamento de inventário e estado dos módulos.

- **Bubble & Selection Sort:** Algoritmos de ordenação para reorganização de fila.


## 👨‍💻 Autor - João Pedro

Desenvolvido como atividade acadêmica integradora.  
Curso: **[Ciência da Computação]** — **[FIAP]**  
Período: **[2026/ 2º — fase]**

---

> *"A segurança de uma missão começa muito antes do lançamento."*












