Run
---

```
docker build -t triagem .
docker run -it -h triagem --name triagem -v ${PWD}:/app triagem
```

Re-build
---

```
docker rm -f triagem
docker rmi triagem
docker build -t triagem .
```
