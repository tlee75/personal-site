# Kubernetes:

### Containerd

###### Kill all containerd tasks
```shell
for task in $(sudo ctr -n k8s.io task ls | awk '{print $2}' | sed 1d); do sudo kill -9 $task; done
```

###### Delete all containerd containers
```shell
sudo ctr -n k8s.io c rm $(sudo ctr -n k8s.io c ls -q)
```

###### Delete all containerd images: 
```shell
sudo ctr -n k8s.io i rm $(sudo ctr -n k8s.io i ls -q)
```


### Kubectl

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
# Apply:
kubectl -n {namespace} patch ds {daemonset_name} -p '{"spec": {"template" {"spec": {"nodeSelector": {"kubernetes.io/hostname": "YOUR_NODE_HOSTNAME"}}}}}'

# Remove:
kubectl -n {namespace} patch ds {daemonset_name} --type json -p='[{"op": "remove", "path": "/spec/template/spec/nodeSelector/kubernetes.io/hostname"}]'
```
###### Run ubuntu debug pod on current node
```shell
kubectl run -it ubuntu --image=ubuntu:latest --rm --overrides='{"spec": {"nodeSelector": {"kubernetes.io/hostname": "'$(hostname)'"}}}' -- /bin/bash
```

#### K3S

###### Display HA Node Token
```shell
sudo cat /var/lib/rancher/k3s/server/node-token
```

###### View auto generated config.toml
```shell
cat /var/lib/rancher/k3s/agent/etc/containerd/config.toml
```
