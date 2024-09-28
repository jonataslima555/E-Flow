# Tasks

### routes/tasks.py

- Criar, deletar, editar, mostrar tarefas concluidas e pendentes
- Lidar com tempo de conclusão e repetição de tarefas (mês, semana, dia).
- Remover tarefas antingas que não estão alinhadas com a semana corrente

### services/task_service.py

- Lógica de negócio para as tarefas: criar tarefas recorrentes, controlar prazos de conclusão, e remover tarefas inativas.

### models/tasks.py

- Banco de dados SQLite para desenvolvimento
- ORM Peewee para manipualação de dados
- Arquivo de banco (instance/database.db) separado do código para melhor organização

### Front-end/templates/ e /static/

- Pagina principal (templates/index.html) e paginas de login e cadastro
- CSS global e específico para login e cadastro
- JavaScript para notificações de tarefas próximas do vencimento (static/js/notification.js)
- Framework Bootstrap

### APIs

- Verificação de Email e Recuperação de senha (services/auth_service.py)
- Validação dae código de recuperação

### Back-end

- Flask:
  - Rotas separadas em módulos (blueprint) para contas e tarefas
  - Configuração segura com (.env)
  - Segurança: Autenticação e autorização básica com sessões ou JWT.
    - CSRF
    - Hashpasswords

### Testes

- PyTest e MyPy
  - Cobertura de testes unitários para rotas, modelos e serviços
  - verificação de tipos com MyPy para garantir integridade do código

# Models

### **1. Tabela `users` (Usuários)**

Essa tabela armazena os dados dos usuários registrados no sistema.

- **id**: Identificador único do usuário (chave primária, autoincrementado).
- **username**: Nome de usuário, único.
- **email**: Endereço de email do usuário, único.
- **password_hash**: Hash da senha do usuário (nunca armazenar a senha em texto plano).
- **created_at**: Data e hora em que o usuário foi registrado.
- **updated_at**: Data e hora da última atualização do perfil.
- **is_active**: Booleano para indicar se o usuário está ativo ou desativado.
- **is_admin**: Booleano para indicar se o usuário tem permissões administrativas.

### **2. Tabela `tasks` (Tarefas)**

Essa tabela armazena as tarefas criadas pelos usuários.

- **id**: Identificador único da tarefa (chave primária, autoincrementado).
- **user_id**: Chave estrangeira que referencia o usuário criador da tarefa.
- **title**: Título da tarefa.
- **description**: Descrição detalhada da tarefa.
- **status**: Status da tarefa (pendente, em andamento, concluída).
- **due_date**: Data de vencimento da tarefa.
- **created_at**: Data de criação da tarefa.
- **updated_at**: Data de última modificação da tarefa.
- **completed_at**: Data de conclusão da tarefa (caso seja concluída).
- **recurring**: Tipo de recorrência da tarefa (diária, semanal, mensal, ou nula para não recorrente).
- **recurring_until**: Data limite para a recorrência (se aplicável).
- **is_archived**: Booleano para indicar se a tarefa foi arquivada (remover tarefas antigas da visualização sem deletá-las do banco).

### **3. Tabela `task_history` (Histórico de Tarefas)**

Essa tabela armazena o histórico de tarefas concluídas e removidas, útil para auditoria ou para exibir um histórico ao usuário.

- **id**: Identificador único do histórico (chave primária, autoincrementado).
- **task_id**: Chave estrangeira que referencia a tarefa original.
- **user_id**: Chave estrangeira que referencia o usuário responsável pela tarefa.
- **status_before**: Status da tarefa antes de ser removida ou arquivada.
- **status_after**: Status atual da tarefa (concluída, removida, etc.).
- **action_type**: Tipo de ação registrada (conclusão, remoção, etc.).
- **timestamp**: Data e hora da ação registrada.

### **4. Tabela `password_reset_tokens` (Tokens de Recuperação de Senha)**

Essa tabela armazena os tokens para a recuperação de senha, usados no fluxo de "esqueci minha senha".

- **id**: Identificador único do token (chave primária, autoincrementado).
- **user_id**: Chave estrangeira que referencia o usuário para quem o token foi gerado.
- **token**: O token de recuperação (gerado e armazenado com hashing).
- **created_at**: Data e hora em que o token foi gerado.
- **expires_at**: Data e hora de expiração do token (normalmente 1 ou 2 horas após a criação).
- **used**: Booleano para indicar se o token já foi utilizado.

### **5. Tabela `email_verifications` (Verificações de Email)**

Essa tabela armazena os códigos de verificação de email quando um novo usuário se registra ou quando um usuário precisa validar um email.

- **id**: Identificador único (chave primária, autoincrementado).
- **user_id**: Chave estrangeira que referencia o usuário que solicitou a verificação.
- **verification_code**: Código de verificação enviado por email.
- **created_at**: Data e hora de criação do código.
- **expires_at**: Data e hora de expiração do código.
- **is_verified**: Booleano para indicar se o email foi verificado.

### **6. Tabela `sessions` (Sessões de Autenticação)**

Essa tabela armazena as sessões ativas dos usuários logados, útil caso você opte por usar **sessões** ao invés de JWT para autenticação.

- **id**: Identificador único da sessão (chave primária, autoincrementado).
- **user_id**: Chave estrangeira que referencia o usuário que iniciou a sessão.
- **session_token**: Token único de sessão, gerado no login.
- **created_at**: Data e hora em que a sessão foi iniciada.
- **expires_at**: Data e hora de expiração da sessão.
- **is_active**: Booleano para indicar se a sessão está ativa.

### **Relacionamentos entre as tabelas**

* **users ↔ tasks** : Um usuário pode ter várias tarefas. A relação é 1
  , onde um usuário tem muitas tarefas.
* **users ↔ password_reset_tokens** : Um usuário pode ter múltiplos tokens de recuperação de senha (para múltiplas tentativas de recuperação), mas cada token pertence a um único usuário.
* **users ↔ email_verifications** : Cada usuário pode ter um ou mais códigos de verificação pendentes (por exemplo, ao trocar o email).
* **tasks ↔ task_history** : Cada tarefa pode ter um histórico associado que registra ações importantes (como conclusão ou exclusão).
* **users ↔ sessions** : Cada usuário pode ter várias sessões ativas, por exemplo, se estiver logado em dispositivos diferentes.
