# Requisitos 

- Requisitos Funcionais para um Software de Escola Completo ([Baseado no Edukante](https://www.edukante.com/sistemas-gestao-escolar/software-gestao-escolar-web-controle-academico.aspx))
- Referência: [Engenharia de Software Moderna - Prof. Marco Tulio Valente](https://engsoftmoderna.info/)
- [Cap 3 - Requisitos](https://engsoftmoderna.info/cap3.html#requisitos)

## 1. O que são Requisitos?

Requisitos definem o que um sistema deve fazer e sob quais restrições. As funcionalidades de um sistema, o que um sistema deve fazer, são chamados de **Requisitos Funcionais (requisitos de usuário)** normalmente escritos em linguagem natural e por usuários. 

Existe uma outra categoria de requisitos, chamado de **Requisitos Não-Funcionais (requisitos de sistema)**, que tem relação com a qualidade do serviço prestado pelo sistema, incluindo características como desempenho, disponibilidade, segurança, consumo de memória, disco, etc. Esses são mais técnicos, precisos e escritos pelos próprios desenvolvedores.

Diz-se que, os **requisitos funcionais (requisitos de usuário)** estão mais próximos do problema enquanto que, os **requisitos não-funcionais (requisitos de sistema)** estão mais próximos da solução.

A definição dos requisitos é uma etapa crucial na construção de qualquer sistema de software pois, é aqui que se especifica como o sistema irá atender aos seus usuários. 

**Engenharia de Requisitos** é o nome que se dá ao conjunto de atividades relacionadas com a descoberta, análise, especificação e manutenção dos requisitos de um sistema. Para a elicitação de requisitos, há diversas técnicas incluindo entrevistas com stakeholders, aplicação de questionários, leitura de documentos e formulários implementação de protótipos e análise de cenários de uso.

Após elicitados, os requisitos devem ser: 

1. Documentados
2. Verificados e validados
3. Priorizados

## 2. Requisitos Funcionais (requisitos de usuário)

### 2.1 Gerenciamento de Pessoas

- Alunos:
    - Cadastro, consulta e edição de dados pessoais e acadêmicos (incluindo foto);
    - Matrícula em turmas, disciplinas e cursos;
    - Histórico escolar completo (com boletim e notas);
    - Frequência e faltas;
    - Trancamento e transferência;
    - Declarações e atestados;
    - Responsáveis e contatos de emergência.

- Professores:
    - Cadastro, consulta e edição de dados pessoais e profissionais;
    - Alocação em turmas e disciplinas;
    - Lançamento de notas e avaliações;
    - Planejamento de aulas;
    - Frequência e faltas;
    - Reuniões e comunicados.

- Funcionários:
    - Cadastro, consulta e edição de dados pessoais e profissionais;
    - Controle de acesso e permissões;
    - Folha de pagamento;
    - Férias e afastamentos;
    - Histórico funcional.

- Usuários:
    - Perfis de acesso com diferentes níveis de permissão (administrador, coordenador, professor, aluno, responsável);
    - Criação e gerenciamento de contas;
    - Recuperação de senha.

### 2.2 Gerenciamento Acadêmico

- Turmas e Cursos:
    - Criação, edição e desativação de turmas e cursos;
    - Definição de grade curricular e disciplinas;
    - Alocação de professores e alunos;
    - Horários e calendário escolar;
    - Lançamento de notas e médias;
    - Histórico de turmas e cursos.

- Disciplinas:
    - Criação, edição e desativação de disciplinas;
    - Conteúdo programático;
    - Materiais didáticos;
    - Planos de aula;
    - Avaliações e critérios de aprovação.

- Matrícula:
    - Processo de matrícula online;
    - Controle de vagas;
    - Conflitos de horários;
    - Geração de boletos;
    - Cancelamento de matrícula.

- Notas e Avaliações:
    - Lançamento de notas e médias por disciplina;
    - Cálculo automático de médias e conceitos;
    - Consultas de notas por aluno, disciplina e turma;
    - Histórico de notas.

- Frequência:
    - Controle de presença e faltas;
    - Geração de relatórios de frequência;
    - Abono de faltas.

- Progressão Escolar:
    - Promoção e retenção de alunos;
    - Cálculo de médias finais;
    - Emissão de certificados e diplomas.

### 2.3 Gerenciamento Administrativo

- Financeiro:
    - Contas a receber e a pagar;
    - Fluxo de caixa;
    - Boletos e carnês;
    - Conciliação bancária;
    - Relatórios financeiros.

- Secretaria:
    - Protocolo de documentos;
    - Agendamento de reuniões;
    - Controle de correspondências;
    - Emissão de documentos (boletim, histórico, atestados).

- Estoque:
    - Controle de materiais escolares;
    - Entrada e saída de produtos;
    - Inventário.

- Biblioteca:
    - Acervo de livros e outros materiais;
    - Empréstimos e devoluções;
    - Renovação de livros;
    - Multas e extravios.

- Manutenção:
    - Registro de solicitações de manutenção;
    - Controle de ordens de serviço;
    - Histórico de manutenções realizadas.

### 2.4 Comunicação e Colaboração

- Mural Virtual:
    - Avisos e comunicados para a comunidade escolar;
    - Mural de fotos e eventos;
    - Compartilhamento de arquivos.

- Mensagens:
    - Comunicação interna entre usuários (individual e em grupo);
    - Envio de arquivos e anexos.

- Fórum:
    - Discussões sobre temas acadêmicos e extracurriculares;
    - Troca de ideias e experiências;
    - Perguntas e respostas.

- Agenda Escolar:
    - Consulta de eventos e compromissos;
    - Agendamento de reuniões e atividades;
    - Lembretes e notificações.

- Rede Social Escolar:
    - Integração entre a comunidade escolar;
    - Compartilhamento de fotos, vídeos e notícias;


## 3. Diagrama de Pacotes 

[Diagramas de pacotes](https://engsoftmoderna.info/cap4.html#diagrama-de-pacotes) 
são recomendados quando se pretende oferecer um modelo de mais alto nível de 
um sistema, que mostre apenas grupos de classes (isto é, pacotes).

Pelo fato da aplicação **School Days** ser escrita utilizando o [framework Django](https://www.djangoproject.com/), será abstraído os tópicos que representam os requisitos em [Aplicações (ou Django apps)](https://docs.djangoproject.com/en/4.2/ref/applications/#module-django.apps).

Ou seja, para cada tópico, será criado uma aplicação:

- Gerenciamento de Pessoas

```
(venv) $ ./manage.py startapp pessoas
```

- Gerenciamento Acadêmico

```
(venv) $ ./manage.py startapp academico
```

- Gerenciamento Administrativo

```
(venv) $ ./manage.py startapp administrativo
```

- Comunicação e Colaboração

```
(venv) $ ./manage.py startapp colaboracao
```

Como resultado, teremos a seguinte estrutura de diretórios:

```
(venv) $ ls -lF
total 24
drwxr-xr-x 3 darmbrust darmbrust 4096 Apr 22 17:43 academico/
drwxr-xr-x 3 darmbrust darmbrust 4096 Apr 22 17:43 administrativo/
drwxr-xr-x 3 darmbrust darmbrust 4096 Apr 22 17:43 colaboracao/
-rwxr-xr-x 1 darmbrust darmbrust  666 Apr 22 10:37 manage.py*
drwxr-xr-x 3 darmbrust darmbrust 4096 Apr 22 17:43 pessoas/
drwxr-xr-x 3 darmbrust darmbrust 4096 Apr 22 17:43 schooldays/
```