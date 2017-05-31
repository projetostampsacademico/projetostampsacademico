Run
---

```
docker-compose up -d
```

Stop
---

```
docker-compose down
```

Log
---

```
docker logs -f kafka
docker logs -f zookeeper
```

Test
---

Consumer (terminal-1):
```
docker run --rm -it ryane/kafkacat -C -b 34.204.88.242 -t test
```

Producer (terminal-2):
```
docker run --rm -it ryane/kafkacat -P -b 34.204.88.242 -t test
```

