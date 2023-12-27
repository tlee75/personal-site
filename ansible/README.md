# Ansible


To run a playbook manually:

```shell
ansible-playbook -i ansible/inventory/nodes.yml --limit node1 ansible/playbooks/deploy_prod.yml \
  -e "IMAGE_TAG=${GITHUB_SHA}" \
  -e "DOCKERHUB_ACCOUNT=${DOCKERHUB_ACCOUNT}" \
  -e "MKDOCS_APP_NAME=${MKDOCS_APP_NAME}" \
  -e "CF_ACCESS_CLIENT_ID=${CF_ACCESS_CLIENT_ID}" \
  -e "CF_ACCESS_CLIENT_SECRET=${CF_ACCESS_CLIENT_SECRET}" \
  --private-key=~/.ssh/arm-k3s-oci"
```

