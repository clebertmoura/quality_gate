# Projeto acadêmico para Mestrado em Ciências da Computação

Este projeto tem o objetivo avaliar critérios de qualidade de software estabelecidos pela norma ISO/IEC 9126-1 em códigos-fonte implementados por alunos de turmas de programação. A solução utiliza a ferramenta Sonar para realizar a avaliação, em uma infraestrutura de containers (Docker).

# Tech stack
> Sonar 9.9
> Postgres 15

# Guia de uso

## Para executar o Sonar

Execute o seguinte comando para iniciar os containers.

> docker-compose up -d

## Acessar a console do Sonar

Acesse a URL: http://localhost:9000

No primeiro acesso será solicitada a criação de um usuário e senha. 
Exemplo: `admin` / `password`

## Configurar o projeto

Pela console do Sonar, crie um projeto e configure o project-key no arquivo: `sonar-project.properties`.

## Executar a analise do código

Copiar os arquivos de código-fonte que deseja analisar para pasta `./src` e execute o comando:

> ./run.sh