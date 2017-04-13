# Pacientes

Para desenvolver:
```bash
docker-compose build
docker-compose run -p 8080:3000 server bash
```

Para colocar em produção:
```bash
docker-compose build
docker-compose up -d
docker-compose logs -f server
```


# Sugestão de inicialização de ambiente de desenvolvimento na núvem

1 - Criar conta no Cloud9 (http://c9.io) - Apesar de precisar do cartão de crédito no cadastro, é gratuito, já uso a quase 2 anos e é bastante confiável;

2 - "Create new Workspace":
- Selecionar um nome qualquer (Ex: stamps), 
- no campo "Clone from Git or Mercurial URL" colar o endereço do nosso repositório (https://github.com/projetostampsacademico/projetostampsacademico.git),
- "Choose a Template" => Node.js
- "Create Workspace" 

3 - Aguarda a criação do workspace (IDE online), que nada mais é do que uma maquina virtual linux rodando num servidor, com 3 áreas de interface principais: À esquerda um navegador do sistema de arquivos, à direita superior um editor de arquivos e à direita inferior um shell/terminal;

4 - No shell, executar os seguintes comandos para instalar/atualizar o Node e o Bower:
```sh
$ cd pacientes/server/
$ npm install
$ npm install -g bower
$ bower -v
$ bower install
```

5 - Rodar o servidor: Na área inferior direita, clicar no '+' (nova aba), e selecionar a opção "New run configuration", na nova janela aberta, no campo "Command:" colocar:
```bash
./pacientes/server/index.js
```

6 - Clicar em "Run". O servidor está rodando no endereço que aparecerá nesta janela, que depende do seu usuário e nome do workspace. Em caso de problemas para acessar verificar se a porta no arquivo /pacientes/server/index.js está selecionada para 8080, 8081 ou 8082.