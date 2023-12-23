# Cheat Sheet


#### Linux

```shell
# Find disk usage for the current working directory
sudo du --max-depth=1 --block-size=MB ./* | sort -n

# Find all hardlinks
find -type f -links +1


```


#### APT:  
```shell
# Fix APT when stuck on User prompt from automated process: 
sudo fuser -vki -TERM /var/lib/dpkg/lock var/lib/dpkg/lock-frontend
sudo dpkg --configure -a

# Another option:
sudo fuser --vki /var/cache/debconf/config.dat

# Fix broken packages 
sudo apt install -y --fix-broken
```


#### Containerd:

```shell
# Kill all containerd tasks
for task in $(sudo ctr -n k8s.io task ls | awk '{print $2}' | sed 1d); do sudo kill -9 $task; done

# Delete all containerd containers
sudo ctr -n k8s.io c rm $(sudo ctr -n k8s.io c ls -q)

# Delete all containerd images: 
sudo ctr -n k8s.io i rm $(sudo ctr -n k8s.io i ls -q)
```


#### Kubernetes:

###### Copy secret from one namespace to another

```shell
kubectl get secret {source_secret} --namespace={source_namespace} -o yaml | sed 's/namespace: .*namespace: {target_namespace}' | kubectl apply -f -
````
###### List pods by label on current node 
```shell
kubectl get pods -n {namespace} -o wide --field-selector spec.nodeName$(hostname) -l {label_key}={label_value}
```

###### Schedule Daemonset on specific node
```shell
Apply:
kubectl -n {namespace} patch ds {daemonset_name} -p '{"spec": {"template" {"spec": {"nodeSelector": {"kubernetes.io/hostname": "YOUR_NODE_HOSTNAME"}}}}}'

Remove:
kubectl -n {namespace} patch ds {daemonset_name} --type json -p='[{"op": "remove", "path": "/spec/template/spec/nodeSelector/kubernetes.io/hostname"}]'
```
###### Run ubuntu debug pod on current node
```shell
kubectl run -it ubuntu --image=ubuntu:latest --rm --overrides='{"spec": {"nodeSelector": {"kubernetes.io/hostname": "'$(hostname)'"}}}' -- /bin/bash
```


#### Redpanda Kafka

```shell
# Get brokers - No TLS
rpk cluster info -b --brokers {hostname}:{port}

# Consume from topic 

rpk topic consume {topic_name} -o end --brokers {broker}:{port}
```


#### SSL

```shell
# Check SANs for HTTPS endpoint
openssl s_client -connect {hostname}:443 </dev/null 2>/dev/null | openssl x509 -noout -text | grep DNS:
```


##### K3S

```shell
# Display HA Node Token
sudo cat /var/lib/rancher/k3s/server/node-token

# View auto generated config.toml
cat /var/lib/rancher/k3s/agent/etc/containerd/config.toml
```

#### Cloudflare
```shell
# Make GET request using Cloudflare Service Auth Token
curl -s -X GET \
  -H "CF-Access-Client-ID: ${CF_ACCESS_CLIENT_ID}" \
  -H "CF-Acess-Client-Secret: ${CF_ACCESS_CLIENT_SECRET}" \
  -H "Content-Type: applicationjson" \
  {http_endpoint}
  
# Make POST request with JSON payload using Cloudflare Service Auth Token
curl --request POST \
  -H "CF-Access-Client-ID: ${CF_ACCESS_CLIENT_ID}" \
  -H "CF-Acess-Client-Secret: ${CF_ACCESS_CLIENT_SECRET}" \
  -H "Content-Type: applicationjson" \
  --url {http_endpoint} \
  --data '{"key":"value"}'
  
# 
```