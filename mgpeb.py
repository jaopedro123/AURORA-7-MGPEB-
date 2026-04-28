# =============================================================================
# MGPEB - Módulo de Gerenciamento de Pouso e Estabilização de Base
# Missão Aurora Siger | Colônia Marciana
# =============================================================================
# Entregável 2: Código-fonte Python (.py)
# Utiliza: listas, filas (deque), pilhas, busca linear/binária e ordenação
# (bubble sort / selection sort), sem bibliotecas avançadas externas.
# =============================================================================

from collections import deque   # estrutura de fila (FIFO)

# ─────────────────────────────────────────────────────────────────────────────
# 1. DEFINIÇÃO DOS MÓDULOS
# Cada módulo é um dicionário com os atributos exigidos na especificação.
# ─────────────────────────────────────────────────────────────────────────────

# Atributos:
#   nome           – identificador do módulo
#   tipo           – categoria da carga (habitacao, energia, laboratorio,
#                    logistica, medico)
#   prioridade     – inteiro 1 (maior) … 5 (menor)
#   combustivel    – percentual restante (0–100)
#   massa_ton      – massa em toneladas
#   criticidade    – 'alta', 'media' ou 'baixa'
#   horario_orbita – hora estimada de chegada à órbita (formato HH:MM)

modulos_iniciais = [
    {
        "nome": "HAB-01",
        "tipo": "habitacao",
        "prioridade": 1,
        "combustivel": 55,
        "massa_ton": 18.4,
        "criticidade": "alta",
        "horario_orbita": "08:30"
    },
    {
        "nome": "ENE-02",
        "tipo": "energia",
        "prioridade": 2,
        "combustivel": 72,
        "massa_ton": 9.1,
        "criticidade": "alta",
        "horario_orbita": "09:00"
    },
    {
        "nome": "LAB-03",
        "tipo": "laboratorio",
        "prioridade": 3,
        "combustivel": 40,
        "massa_ton": 12.7,
        "criticidade": "media",
        "horario_orbita": "10:15"
    },
    {
        "nome": "LOG-04",
        "tipo": "logistica",
        "prioridade": 4,
        "combustivel": 88,
        "massa_ton": 22.0,
        "criticidade": "baixa",
        "horario_orbita": "11:00"
    },
    {
        "nome": "MED-05",
        "tipo": "medico",
        "prioridade": 2,
        "combustivel": 30,
        "massa_ton": 7.5,
        "criticidade": "alta",
        "horario_orbita": "09:45"
    },
    {
        "nome": "ENE-06",
        "tipo": "energia",
        "prioridade": 3,
        "combustivel": 61,
        "massa_ton": 10.3,
        "criticidade": "media",
        "horario_orbita": "12:00"
    },
    {
        "nome": "LOG-07",
        "tipo": "logistica",
        "prioridade": 5,
        "combustivel": 95,
        "massa_ton": 25.0,
        "criticidade": "baixa",
        "horario_orbita": "13:30"
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# 2. ESTRUTURAS LINEARES
# ─────────────────────────────────────────────────────────────────────────────

# FILA principal — módulos aguardando autorização de pouso (FIFO)
fila_pouso = deque()

# LISTA auxiliar — módulos já pousados com sucesso
lista_pousados = []

# LISTA auxiliar — módulos em espera por problema operacional
lista_espera = []

# PILHA de alertas — registra eventos críticos (LIFO)
pilha_alertas = []

# ─────────────────────────────────────────────────────────────────────────────
# 3. FUNÇÕES AUXILIARES
# ─────────────────────────────────────────────────────────────────────────────

def exibir_separador(titulo=""):
    """Imprime um separador visual com título opcional."""
    print("\n" + "=" * 60)
    if titulo:
        print(f"  {titulo}")
        print("=" * 60)


def exibir_modulo(modulo):
    """Exibe os atributos de um módulo de forma legível."""
    print(f"  Nome        : {modulo['nome']}")
    print(f"  Tipo        : {modulo['tipo']}")
    print(f"  Prioridade  : {modulo['prioridade']}")
    print(f"  Combustível : {modulo['combustivel']}%")
    print(f"  Massa       : {modulo['massa_ton']} ton")
    print(f"  Criticidade : {modulo['criticidade']}")
    print(f"  Horário     : {modulo['horario_orbita']}")


def exibir_fila(fila):
    """Exibe todos os módulos na fila principal."""
    if not fila:
        print("  (fila vazia)")
        return
    for i, m in enumerate(fila):
        print(f"  [{i+1}] {m['nome']} | tipo={m['tipo']} | prior={m['prioridade']}"
              f" | comb={m['combustivel']}% | critic={m['criticidade']}")


# ─────────────────────────────────────────────────────────────────────────────
# 4. CADASTRO DOS MÓDULOS NA FILA
# ─────────────────────────────────────────────────────────────────────────────

def cadastrar_modulos(lista, fila):
    """
    Insere todos os módulos da lista na fila de pouso (enqueue).
    Complexidade: O(n)
    """
    for modulo in lista:
        fila.append(modulo)       # adiciona ao final da fila
    print(f"  {len(lista)} módulos cadastrados na fila de pouso.")


# ─────────────────────────────────────────────────────────────────────────────
# 5. ALGORITMOS DE BUSCA
# ─────────────────────────────────────────────────────────────────────────────

def busca_menor_combustivel(fila):
    """
    Busca linear: encontra o módulo com menor nível de combustível.
    Percorre toda a fila — O(n).
    Retorna o módulo encontrado ou None se a fila estiver vazia.
    """
    if not fila:
        return None

    menor = fila[0]                       # assume o primeiro como mínimo
    for modulo in fila:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor


def busca_maior_prioridade(fila):
    """
    Busca linear: encontra o módulo com maior prioridade (valor numérico menor).
    Retorna o primeiro módulo encontrado com o menor número de prioridade.
    """
    if not fila:
        return None

    mais_prioritario = fila[0]
    for modulo in fila:
        if modulo["prioridade"] < mais_prioritario["prioridade"]:
            mais_prioritario = modulo
    return mais_prioritario


def busca_por_tipo(fila, tipo_buscado):
    """
    Busca linear: retorna lista com todos os módulos de um determinado tipo.
    Ex: busca_por_tipo(fila, 'medico') → lista com módulos médicos.
    Complexidade: O(n)
    """
    resultado = []
    for modulo in fila:
        if modulo["tipo"] == tipo_buscado:
            resultado.append(modulo)
    return resultado


def busca_binaria_prioridade(lista_ordenada, prioridade_alvo):
    """
    Busca binária: localiza o índice de um módulo com a prioridade-alvo
    em uma lista JÁ ORDENADA por prioridade (crescente).
    Retorna o índice ou -1 se não encontrado.
    Complexidade: O(log n)
    """
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        p_meio = lista_ordenada[meio]["prioridade"]

        if p_meio == prioridade_alvo:
            return meio                   # encontrou
        elif p_meio < prioridade_alvo:
            inicio = meio + 1             # busca na metade direita
        else:
            fim = meio - 1               # busca na metade esquerda

    return -1                             # não encontrado


# ─────────────────────────────────────────────────────────────────────────────
# 6. ALGORITMOS DE ORDENAÇÃO
# ─────────────────────────────────────────────────────────────────────────────

def bubble_sort_prioridade(lista):
    """
    Bubble Sort: ordena módulos por prioridade (crescente, 1 = mais urgente).
    A cada passagem, elementos maiores 'sobem' para o final.
    Complexidade: O(n²) — adequado para listas pequenas de módulos.
    Modifica a lista passada por referência.
    """
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["prioridade"] > lista[j + 1]["prioridade"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]   # troca


def selection_sort_combustivel(lista):
    """
    Selection Sort: ordena módulos por combustível (crescente).
    Em cada passo, seleciona o elemento de menor combustível
    e o coloca na posição correta.
    Complexidade: O(n²)
    Modifica a lista passada por referência.
    """
    n = len(lista)
    for i in range(n):
        idx_menor = i
        for j in range(i + 1, n):
            if lista[j]["combustivel"] < lista[idx_menor]["combustivel"]:
                idx_menor = j
        lista[i], lista[idx_menor] = lista[idx_menor], lista[i]   # troca


def reorganizar_fila(fila, criterio="prioridade"):
    """
    Converte a fila em lista, ordena pelo critério escolhido e reconstrói a fila.
    criterio: 'prioridade' (bubble sort) ou 'combustivel' (selection sort).
    """
    lista_temp = list(fila)           # transforma fila em lista para ordenação

    if criterio == "prioridade":
        bubble_sort_prioridade(lista_temp)
        print(f"  Fila reorganizada por PRIORIDADE (Bubble Sort).")
    elif criterio == "combustivel":
        selection_sort_combustivel(lista_temp)
        print(f"  Fila reorganizada por COMBUSTÍVEL (Selection Sort).")
    else:
        print("  Critério inválido. Fila não alterada.")
        return

    fila.clear()
    for m in lista_temp:
        fila.append(m)


# ─────────────────────────────────────────────────────────────────────────────
# 7. REGRAS DE DECISÃO — AUTORIZAÇÃO DE POUSO
# Baseadas nas portas lógicas AND / OR / NOT modeladas no relatório.
#
# Regra de autorização (AND completo):
#   AUTORIZADO SE:
#     combustivel >= 25%                (NOT combustivel_critico)
#     AND area_pouso == True            (área disponível)
#     AND sensores_ok == True           (integridade dos sensores)
#     AND condicoes_atmosfericas == True (condições aceitáveis)
#
# Regra de EMERGÊNCIA (OR — ao menos uma condição crítica):
#   EMERGÊNCIA SE:
#     combustivel < 15%                 (risco de colapso)
#     OR criticidade == 'alta'          (carga de alta criticidade)
# ─────────────────────────────────────────────────────────────────────────────

def autorizar_pouso(modulo, area_pouso, sensores_ok, condicoes_atmosfericas):
    """
    Avalia se um módulo pode pousar com base nas regras lógicas.

    Parâmetros externos de contexto:
        area_pouso             : bool — área de pouso disponível
        sensores_ok            : bool — sensores em pleno funcionamento
        condicoes_atmosfericas : bool — condições atmosféricas aceitáveis

    Retorna uma string com a decisão: 'AUTORIZADO', 'EMERGENCIA' ou 'AGUARDAR'.
    """

    nome = modulo["nome"]
    combustivel = modulo["combustivel"]
    criticidade = modulo["criticidade"]

    # Condição de EMERGÊNCIA (OR): combustível quase zero OU carga crítica urgente
    condicao_emergencia = (combustivel < 15) or (criticidade == "alta" and combustivel < 25)

    if condicao_emergencia:
        alerta = f"[EMERGÊNCIA] {nome}: combustível={combustivel}% | criticidade={criticidade}"
        pilha_alertas.append(alerta)     # empilha o alerta (LIFO)
        return "EMERGENCIA"

    # Condição de AUTORIZAÇÃO (AND): todas as variáveis devem ser verdadeiras
    combustivel_suficiente = combustivel >= 25
    condicao_autorizacao = (combustivel_suficiente
                            and area_pouso
                            and sensores_ok
                            and condicoes_atmosfericas)

    if condicao_autorizacao:
        return "AUTORIZADO"
    else:
        return "AGUARDAR"


def processar_fila(fila, area_pouso, sensores_ok, condicoes_atmosfericas):
    """
    Processa módulo a módulo (dequeue) avaliando a autorização de pouso.
    Módulos autorizados → lista_pousados
    Módulos em espera   → lista_espera (reinseridos no final da fila num cenário real)
    Emergências         → processadas primeiro e enviadas para lista_pousados
    """
    exibir_separador("PROCESSAMENTO DA FILA DE POUSO")

    while fila:
        modulo = fila.popleft()          # retira o primeiro da fila (dequeue)
        decisao = autorizar_pouso(modulo, area_pouso, sensores_ok, condicoes_atmosfericas)

        if decisao == "AUTORIZADO":
            lista_pousados.append(modulo)
            print(f"  ✔ {modulo['nome']} → POUSO AUTORIZADO")

        elif decisao == "EMERGENCIA":
            lista_pousados.insert(0, modulo)    # inserido com prioridade máxima
            print(f"  ⚠ {modulo['nome']} → POUSO DE EMERGÊNCIA (prioridade máxima)")

        else:
            lista_espera.append(modulo)
            print(f"  ✘ {modulo['nome']} → AGUARDANDO (condições insuficientes)")

    print(f"\n  Pousados : {len(lista_pousados)} módulos")
    print(f"  Em espera: {len(lista_espera)} módulos")


# ─────────────────────────────────────────────────────────────────────────────
# 8. EXIBIÇÃO DE ALERTAS (PILHA — LIFO)
# ─────────────────────────────────────────────────────────────────────────────

def exibir_alertas():
    """
    Desempilha e exibe todos os alertas na ordem inversa de geração (LIFO).
    O último alerta gerado é o primeiro a ser exibido.
    """
    exibir_separador("HISTÓRICO DE ALERTAS (LIFO — pilha)")
    if not pilha_alertas:
        print("  Nenhum alerta registrado.")
        return
    alertas_copia = pilha_alertas[:]
    while alertas_copia:
        print(" ", alertas_copia.pop())     # pop() → remove do topo da pilha


# ─────────────────────────────────────────────────────────────────────────────
# 9. EXECUÇÃO PRINCIPAL — DEMONSTRAÇÃO COMPLETA DO MGPEB
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║    MGPEB — Módulo de Gerenciamento de Pouso             ║")
    print("║    e Estabilização de Base | Missão Aurora Siger        ║")
    print("╚══════════════════════════════════════════════════════════╝")

    # ── 9.1 Cadastro na fila ──────────────────────────────────────────────
    exibir_separador("CADASTRO DOS MÓDULOS NA FILA DE POUSO")
    cadastrar_modulos(modulos_iniciais, fila_pouso)

    exibir_separador("FILA INICIAL (ordem de chegada)")
    exibir_fila(fila_pouso)

    # ── 9.2 Buscas ───────────────────────────────────────────────────────
    exibir_separador("BUSCAS NA FILA")

    menor_comb = busca_menor_combustivel(fila_pouso)
    print(f"  Módulo com MENOR combustível: {menor_comb['nome']} ({menor_comb['combustivel']}%)")

    mais_prior = busca_maior_prioridade(fila_pouso)
    print(f"  Módulo com MAIOR prioridade : {mais_prior['nome']} (prioridade {mais_prior['prioridade']})")

    tipo_alvo = "energia"
    modulos_energia = busca_por_tipo(fila_pouso, tipo_alvo)
    nomes_energia = [m["nome"] for m in modulos_energia]
    print(f"  Módulos do tipo '{tipo_alvo}'    : {nomes_energia}")

    # Busca binária após ordenação
    lista_ord_prior = list(fila_pouso)
    bubble_sort_prioridade(lista_ord_prior)
    prioridade_busca = 2
    idx = busca_binaria_prioridade(lista_ord_prior, prioridade_busca)
    if idx != -1:
        print(f"  Busca binária (prior={prioridade_busca}) : encontrado '{lista_ord_prior[idx]['nome']}' no índice {idx}")
    else:
        print(f"  Busca binária (prior={prioridade_busca}) : não encontrado")

    # ── 9.3 Ordenação da fila ────────────────────────────────────────────
    exibir_separador("ORDENAÇÃO DA FILA")
    reorganizar_fila(fila_pouso, criterio="prioridade")

    exibir_separador("FILA APÓS ORDENAÇÃO POR PRIORIDADE")
    exibir_fila(fila_pouso)

    # ── 9.4 Autorização de pouso ─────────────────────────────────────────
    # Condições externas simuladas para o cenário de pouso
    AREA_POUSO_DISPONIVEL   = True     # plataforma livre
    SENSORES_OK             = True     # todos os sensores operacionais
    CONDICOES_ATMOSFERICAS  = True     # tempestade de areia ausente

    processar_fila(fila_pouso, AREA_POUSO_DISPONIVEL, SENSORES_OK, CONDICOES_ATMOSFERICAS)

    # ── 9.5 Resultado final ──────────────────────────────────────────────
    exibir_separador("MÓDULOS POUSADOS (em ordem de processamento)")
    for i, m in enumerate(lista_pousados):
        print(f"  {i+1}. {m['nome']} | tipo={m['tipo']} | prior={m['prioridade']}")

    exibir_separador("MÓDULOS EM ESPERA")
    if lista_espera:
        for m in lista_espera:
            print(f"  - {m['nome']} | comb={m['combustivel']}% | critic={m['criticidade']}")
    else:
        print("  (nenhum módulo em espera)")

    exibir_alertas()

    # ── 9.6 Novo módulo cadastrado em tempo real (demonstração de fila) ──
    exibir_separador("ADIÇÃO DE NOVO MÓDULO EM TEMPO REAL")
    novo_modulo = {
        "nome": "MED-08",
        "tipo": "medico",
        "prioridade": 1,
        "combustivel": 12,        # combustível crítico → emergência
        "massa_ton": 6.0,
        "criticidade": "alta",
        "horario_orbita": "14:00"
    }
    fila_pouso.append(novo_modulo)
    print(f"  Módulo {novo_modulo['nome']} adicionado à fila.")

    decisao_novo = autorizar_pouso(novo_modulo, AREA_POUSO_DISPONIVEL, SENSORES_OK, CONDICOES_ATMOSFERICAS)
    print(f"  Decisão para {novo_modulo['nome']}: {decisao_novo}")

    exibir_alertas()

    print("\n" + "=" * 60)
    print("  MGPEB encerrado. Base Aurora Siger operacional.")
    print("=" * 60 + "\n")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
