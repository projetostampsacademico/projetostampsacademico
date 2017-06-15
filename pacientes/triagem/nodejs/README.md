```
docker build -t triagem .
docker run -it --name triagem -e "TOPICIN=det-paciente" -e "TOPICOUT=tri-paciente" triagem
```
