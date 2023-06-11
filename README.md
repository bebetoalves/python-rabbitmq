# Aplicação Python com RabbitMQ - Publish-Subscribe

Este projeto implementa uma aplicação em Python com RabbitMQ usando o padrão publish-subscribe. Consiste em um sensor que gera números aleatórios e envia suas leituras para um canal chamado "sensores". Um servidor lê essas mensagens do canal e exibe mensagens de alerta ou sensor normal com base nos valores recebidos.

## Requisitos

- Docker
- Docker Compose

## Configuração e Uso

1. Clone este repositório:

```
git clone https://github.com/bebetoalves/python-rabbitmq.git
```

2. Navegue até o diretório raiz do projeto:

```
cd python-rabbitmq
```

3. Construa as imagens dos containers usando o Docker Compose:

```
docker-compose build
```

4. Inicie os containers:

```
docker-compose up
```

5. Em alguns segundos você verá no console o sensor enviando suas leituras e o servidor consumindo essas leituras.

```log
sensor | 2023-06-11 22:08:22,062 | [INFO] | Enviando para o servidor: 39
server | 2023-06-11 22:08:22,063 | [INFO] | Leitura recebida: 39
sensor | 2023-06-11 22:08:23,928 | [INFO] | Enviando para o servidor: 72
server | 2023-06-11 22:08:23,929 | [INFO] | Leitura recebida: 72
server | 2023-06-11 22:08:23,929 | [CRITICAL] | Sensor apresentando altas temperaturas!
sensor | 2023-06-11 22:08:25,384 | [INFO] | Enviando para o servidor: 8
server | 2023-06-11 22:08:25,384 | [INFO] | Leitura recebida: 8
```

## Funcionamento

A aplicação consiste em dois containers Python: "sensor" e "server".

### Sensor

O container "sensor" é responsável por gerar leituras aleatórias e enviá-las para o canal "sensores" no formato JSON. O sensor aguarda entre 0 e 2 segundos para enviar cada leitura.

### Servidor

O container "server" é responsável por ler as mensagens do canal "sensores". Ele se vincula ao canal "sensores", recebe as mensagens enviadas pelo sensor e exibe no console se a leitura indica altas temperaturas (acima de 60).

Os registros das mensagens enviadas e recebidas são exibidos no console, utilizando a biblioteca de logging do Python.
