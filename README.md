# Sistema de Chamados

## Escopo do sistema:

Sistema de chamados onde o usuário pode criar, listar, atualizar e deletar chamados. No presente sistema, o usuário deverá poder:

- Criar chamados;
- Listar chamados;
- Atalizar chamados;
- Deletar chamados;
- Atribuir nome, telefone e descrição ao chamado;
- Checar se o chamado foi resolvido ou não;
- Ver a data e hora que o chamado foi criado;
- Ver a data e hora que o chamado foi alterado;
- Visualizar o técnico responsável pelo atendimento.

## Diagrama de Classes

```mermaid
classDiagram
    class Chamado {
        +int id
        +str nome_usuario
        +str telefone_usuario
        +int setor_id
        +text descricao
        +boolean foi_resolvido
        +datetime data_criacao
        +datetime data_atualização
        +int tecnico_responsavel_id
    }

    class Setor {
        +int id
        +str nome 
    }

    class Tecnico {
        +int id
        +str nome
        +str email
    }
    
    Setor ||--o{ Chamado : "possui"
    Setor ||--o{ Tecnico : "contém"
    Tecnico ||--o{ Chamado : "atende"

```