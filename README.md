# Infraestructure

Repositório criado para guardar as informações da infraestrutura do projeto
South's Eagle.

## Como funciona?

Para conseguir integrar o github actions com o terraform foi utilizado a plataforma
HCP do terraform para conseguir linkar a execução com o workspace da AWS.
Na plataforma é colocado as envs de ambiente como os secrets e token
gerados pela AWS.

[Como conectar o github-actions com Terraform](https://developer.hashicorp.com/terraform/tutorials/automation/github-actions)

## Como funciona a pipeline de desenvolvimento?

Primeiro é necessário criar uma branch nova pois não vai ser possível commitar
direto na main.

`git branch <nome da branch>`

Após isso pode fazer as alterações necessárias de infraestrutura e depois dar push
e abrir um pull request.

Depois de abrir um pull-request a pipeline executará um `terraform plan` que é para
validar os recursos que estão sendo criados e mostrar quais recursos serão criados
na aplicação.

> [!IMPORTANT]
> Não é possível mergear para master sem antes ter terminado de executar o plan

Após o merge será triggado o `terraform apply` que esse de fato irá criar
os recursos que foram colocado no código na AWS.
