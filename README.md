#globantChallenge

Olá! Me chamo Breno e estou participando de um Challenge da Globant, que descrevia algumas tarefas que dizem respeito a área de engenharia de dados que eu atuo...

Vou comentar um pouco sobre a minha arquitetura, o que pensei para responder, o que não deu tempo/houve dificuldade entre outras coisas interessantes do processo!

Começo confessando que infelizmente só consegui dedicar o dia de domingo para a tarefa toda, até então só havia lido por cima, mas mesmo assim acho que consegui ter uma boa curva de evolução dentro do desenvolvimento dessa tarefa.

Cenário executado:
![Diagrama sem nome drawio (2)](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/df92d988-921f-403d-94df-5162443de9d8)

Para explicar resumidamente o cenário, temos duas fontes de dados para extrairmos, uma fonte de dados histórica, em CSV, simulando uma "migração", por exemplo. E a segunda fonte, e um dos desafios para mim (que nunca havia criado do 0) era criar uma API, que fosse possivel inserir dados via API dentro do banco, como se esse fosse o "fluxo normal" do cenário.

Optei por utilizar o Django REST framework, pois além de ser bastante utilizado hoje em dia, estã numa linguagem (python) que eu domino mais...
Abaixo temos alguns prints da API rodando...
![Captura de Tela 2023-07-24 às 05 38 37](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/b2744a8e-3b3e-4941-8ecc-a51826990ca4)
![Captura de Tela 2023-07-24 às 05 38 18](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/d7100c55-310a-44a6-86d7-bd43b35033ce)
![Captura de Tela 2023-07-24 às 05 38 10](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/bcf5af63-21f0-487d-95da-e19a97393de2)


O programa precisava possuir uma funcão que realizava backup das tabelas do banco em formato AVRO (acrescentei uma pasta de backup em CSV também, não custava nada...) e que poderia ser restaurado como um backup de verdade.

O banco de dados que escolhi foi o PostgreSQL e optei por realizar um ELT. Segue as tabelas criadas no banco...
![Captura de Tela 2023-07-24 às 05 40 19](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/e917cfdd-a220-4aff-bcfc-c85ed789fe0c)



E nada melhor para transformar nosso dados (que sofreram apenas transformações simples) do que o DBT! Ferramenta apenas de transformação que ajuda e é super organizada, possuindo versionamentos e muitos pontos positivos. Segue abaixo as tabelas geradas pela ferramenta:
![Captura de Tela 2023-07-24 às 05 40 35](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/96a5cdf1-6a12-4c2f-8328-bfcf9f3b9b57)
![Captura de Tela 2023-07-24 às 05 40 43](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/bc4e0bc3-1c9c-4b1b-919e-e46a81b551ae)

![Captura de Tela 2023-07-24 às 05 37 38](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/22bf1505-12d1-4e02-bd07-745205609e4c)
![Captura de Tela 2023-07-24 às 05 37 43](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/b3423854-edbf-4725-8ee8-1db0fcee6747)


Após transformar os dados gerando as tabelas do Challenge #2, carrego elas no mesmo banco de dados utilizando os dois modelos que criei no DBT e pronto!
![Captura de Tela 2023-07-24 às 05 37 31](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/9cdc6463-3c34-46e8-9787-cd1ef6e46704)


Alguns pontos que eu não alcancei totalmente o que foi pedido:
-Em especial a API, nunca havia criado uma do 0 e foi uma experiencia nova, funcionou tudo certo! Mas não alcancei os requisitos de segurança e de performance pedidos!
-Não tive o menor tempo para conteinarizar (docker) a aplicação.
-Não utilizei ferramentas de Cloud pois ja gastei meus créditos grátis em todas...


De resto, creio que esteja tudo nos conformes, para um dia de trabalho, rs!

Todas as tarefas citadas acima, que fazem parte do desafio, (pelo menos as que diziam respeito diretamente ao python e não ferramentas externas), eu executei no main.py, referenciando elas de outros arquivos, e claro que em um cenário comum teriamos um gatilho ou algo do tipo...
![Captura de Tela 2023-07-24 às 06 01 39](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/a71746e0-bf0b-4ac1-b18e-3b9f5c62b27b)

Um ponto interessante para comentar, o documento do desafio possui o link para os arquivos csv's, mas não da permissão para baixar eles... então necessitei utilizar um sample Fake de dados, que criei com Python mesmo...
![Captura de Tela 2023-07-24 às 05 37 00](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/042a59a0-d945-453c-bb01-c5dd5de63435)

![Captura de Tela 2023-07-24 às 05 38 56](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/3a79c8d4-b09f-4fad-bea4-87874d7f848f)





Tomei a liberdade de pensar uma possivel arquitetura para esse cenário dentro do GCP...
Idéia de adaptação para GCP:
![Diagrama sem nome drawio](https://github.com/brenoDataEngineer/globantChallenge/assets/140327557/da7ec592-e1ba-4656-997f-f8dd9dcefc7c)


