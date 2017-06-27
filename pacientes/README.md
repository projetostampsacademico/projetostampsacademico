# Segmento Pacientes

Serviços
---
- **pacientes**: ferramenta para envio de sintomas de pacientes até o tópico det-paciente
- **triagem**: triagem dos tópicos det-*
- **timeline**: ferramenta que apresenta os eventos ocorridos no *STAMPSNet*
- **kafka**: broker do *STAMPSNet*

**OBS**: Ajuste as variáveis de ambiente (environment) no `docker-compose.yml` conforme sua necessidade

Serviço: pacientes
---
```
docker-compose build pacientes #compila
docker-compose up pacientes #executa
docker-compose down pacientes #interrompe e remove o container
```

Serviço: triagem
---
```
docker-compose build triagem #compila
docker-compose up triagem #executa
docker-compose down triagem #interrompe e remove o container
```

Serviço: timeline
---
```
docker-compose build timeline #compila
docker-compose up timeline #executa
docker-compose down timeline #interrompe e remove o container
```

Serviço: kafka
---
```
docker-compose up kafka #executa
docker-compose down kafka #interrompe e remove o container
```

Executar tudo
---
```
docker-compose build #compila
docker-compose up #executa
docker-compose down #interrompe e remove todos os container
```
