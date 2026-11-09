import sys

def obter_entrada(mensagem):
    while True:
        valor = input(mensagem).strip().upper()
        if valor in ['1', 'S', 'SIM', 'Y', 'TRUE', 'V']:
            return 1
        elif valor in ['0', 'N', 'NAO', 'NÃO', 'FALSE', 'F']:
            return 0
        else:
            print("  [!] Entrada inválida. Por favor, digite '1' para SIM ou '0' para NÃO.\n")

def regra_negocio_original(a, b, c, d):
    return 1 if (a == 1 and b == 1 and (c == 1 or d == 1)) else 0

def expressao_canonica(a, b, c, d):
    """
    Expressão canônica da Soma de Mintermos:
    S = (A · B · ¬C · D) + (A · B · C · ¬D) + (A · B · C · D)
    """
    m13 = a and b and (not c) and d
    m14 = a and b and c and (not d)
    m15 = a and b and c and d
    return 1 if (m13 or m14 or m15) else 0

def expressao_simplificada(a, b, c, d):
    """
    Expressão simplificada via Álgebra Booleana e Mapa de Karnaugh:
    S = A · B · (C + D)
    """
    return 1 if (a and b and (c or d)) else 0

def executar_validacao_completa():
    """
    Item 8: Valida todas as 16 combinações da tabela-verdade, comparando:
    1. Regra original
    2. Expressão canônica (SOP)
    3. Expressão simplificada
    4. Implementação executada
    """
    print("\n" + "=" * 78)
    print("VALIDAÇÃO COMPLETA DA TABELA-VERDADE (2^4 = 16 Combinações)")
    print("=" * 78)
    print(f"{'Linha':<6} | {'A':<3} {'B':<3} {'C':<3} {'D':<3} | {'Regra':<7} | {'Canônica':<9} | {'Simplif.':<9} | {'Equivalência'}")
    print("-" * 78)

    todos_equivalentes = True
    for linha in range(16):
        a = (linha >> 3) & 1
        b = (linha >> 2) & 1
        c = (linha >> 1) & 1
        d = (linha >> 0) & 1

        r_original = regra_negocio_original(a, b, c, d)
        r_canonica = expressao_canonica(a, b, c, d)
        r_simplif = expressao_simplificada(a, b, c, d)

        equivalente = (r_original == r_canonica == r_simplif)
        if not equivalente:
            todos_equivalentes = False

        status = "OK (Equivalente)" if equivalente else "ERRO"
        print(f"{linha:<6} | {a:<3} {b:<3} {c:<3} {d:<3} | {r_original:<7} | {r_canonica:<9} | {r_simplif:<9} | {status}")

    print("-" * 78)
    if todos_equivalentes:
        print("[SUCESSO] Todas as 16 combinações demonstraram 100% de equivalência lógica!\n")
    else:
        print("[FALHA] Foi encontrada divergência lógica entre as representações.\n")

def modo_interativo():
    print("=" * 70)
    print("  CITIZEN ASSIST AI - MÓDULO DE TRIAGEM LÓGICA DO BPC / LOAS")
    print("  Curso: Ciência da Computação | Disciplina: Computer Science")
    print("=" * 70)
    print("Responda às 4 perguntas com '1' (Sim) ou '0' (Não):\n")

    A = obter_entrada("A) Cidadão possui inscrição regular e atualizada no CadÚnico? (1/0): ")
    B = obter_entrada("B) A renda familiar per capita é <= 1/4 do salário mínimo? (1/0): ")
    C = obter_entrada("C) O cidadão tem 65 anos de idade ou mais? (1/0): ")
    D = obter_entrada("D) O cidadão é Pessoa com Deficiência (PcD) de longo prazo? (1/0): ")

    S = expressao_simplificada(A, B, C, D)

    print("\n" + "=" * 70)
    print("PARECER E ORIENTAÇÃO DO ASSISTENTE")
    print("=" * 70)

    if S == 1:
        print("\n[+] STATUS: ELEGÍVEL AOS CRITÉRIOS BÁSICOS INICIAIS (S = 1)")
        print("\nOrientações ao Cidadão:")
        print("  1. Documentação necessária:")
        print("     - Documento de identidade com foto (RG/CIN) e CPF de todos do grupo familiar;")
        print("     - Comprovante de residência atualizado;")
        print("     - Laudos, exames e relatórios médicos atualizados (caso solicite como PcD).")
        print("  2. Próximos passos:")
        print("     - Solicite o benefício pelo aplicativo ou site 'Meu INSS' (gov.br/meuinss) ou pelo telefone 135;")
        print("     - Caso necessite de apoio presencial, procure o CRAS mais próximo de sua residência.")
    else:
        print("\n[-] STATUS: NÃO ELEGÍVEL AOS REQUISITOS NESTE MOMENTO (S = 0)")
        print("\nMotivos identificados pelo módulo lógico:")
        
        if not A:
            print("  -> CadÚnico não regular/ausente: É pré-requisito obrigatório estar inscrito e")
            print("     com dados atualizados no Cadastro Único. Procure o CRAS para atualizar.")
        if not B:
            print("  -> Critério de renda não atendido: A renda per capita deve ser de até 1/4")
            print("     do salário mínimo nacional.")
        if not (C or D):
            print("  -> Critério de público-alvo não atendido: O solicitante deve ter 65 anos ou mais,")
            print("     OU comprovar deficiência incapacitante de longo prazo.")

        print("\nOrientação ao Cidadão:")
        print("  - Caso sua situação mude ou precise atualizar seus dados, procure o CRAS da sua região.")

    print("\n" + "-" * 70)
    print("AVISO LEGAL E DE PRIVACIDADE:")
    print("  - O Citizen Assist AI não armazena dados pessoais sensíveis do cidadão.")
    print("  - Este protótipo não representa canal oficial governamental e não garante")
    print("    a concessão de benefício ou direito, servindo apenas para orientação prévia.")
    print("-" * 70 + "\n")

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ['--test', '-t', 'validar']:
        executar_validacao_completa()
    else:
        modo_interativo()
        opcao = input("Deseja executar a validação de todas as 16 combinações da tabela-verdade? (s/n): ").strip().lower()
        if opcao in ['s', 'sim', 'y', '1']:
            executar_validacao_completa()

if __name__ == "__main__":
    main()