# Miscellaneous


### Redpanda Kafka

###### Get brokers - No TLS
```shell
rpk cluster info -b --brokers {hostname}:{port}
```


###### Consume from topic
```shell
pk topic consume {topic_name} -o end --brokers {broker}:{port}
```


### SSL

###### Check SANs for HTTPS endpoint
```shell
openssl s_client -connect {hostname}:443 </dev/null 2>/dev/null | openssl x509 -noout -text | grep DNS:
```
