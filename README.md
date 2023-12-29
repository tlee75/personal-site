# Personal Site

This repository contains very basic scripting and automation geared toward deploying a personal website based on [Mkdocs](https://www.mkdocs.org/) 
which can be used during interviews for example.

## Run Locally:

### Mkdocs

Use the built in Mkdocs server with hot reloading

#### Setup
`python3 -m pip install -r requirements.mkdocs.txt`

#### Run Server
`mkdocs serve`

### Docker

Build and run a Docker image locally

### Docker image Usage
`docker build -t interview:v1 -f dockerfiles/mkdocs/Dockerfile .`

`docker run -p 8000:8000 interview:v1`

## Deploy Publicly

### OCI
You will need an [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/) account along with an amd64 based compute 
offered in their free-tier such as the 1 OCPU and 1 GB RAM instances. Currently this repo utilizes the `VM.Standard.E2.1.Micro`.  
Ensure [Docker](https://docs.docker.com/engine/install/ubuntu/) and [cloudflared](https://pkg.cloudflare.com/index.html) 
have been installed. I also recommend creating a separate SSH private key which will be used later which can be rotated
easily on a regular basis.  

### Cloudflare

Create/login to your [Cloudflare dashboard](https://dash.cloudflare.com/) and ensure the domain you want to use for this 
is activated.

The next goal is to configure the Cloudflare Tunnel so we can get access to our compute from a Github Runner and from the 
public internet without the need to open any ports on the firewall. 

Go to the [Cloudflare Zero-Trust Dashboard](https://one.dash.cloudflare.com/) and create a Cloudflare tunnel which will 
run on your OCI instance and create an ingress rule (aka Public Hostname from UI) which will proxy your HTTP and SSH 
traffic received by the tunnel to the correct ports on your instance. For SSH, use a subdomain like `node1-ssh` for 
the host and set the service as SSH type at localhost, port 22. The HTTP rule can use your root domain and the www record, 
pointed at localhost:8000.

Create a Service Auth token that will be used by the Github runner as well as when you SSH from your workstation, give it
a name which represents the application it will be used by, such as "Personal Site" or something to that effect.

Next, it is very important that you create a Cloudflare Application that will protect the `node1-ssh` endpoint with 
the Service Auth Token you just created. Ensure the Application covers ONLY the SSH endpoint and not the `www` or root 
domain itself. Ensure the Policy uses a "Service Auth" action and includes your Service Auth Token in the rules selector.

Lastly, create a DNS record which points at the instance's private IP, so you have an FQDN for the hostname.

### Cloudflare SSH Config

To SSH via your Cloudflare Tunnel, add a host to your SSH config that looks something like this:  

```shell
Host node1-cf
  Hostname node1-ssh.yourdomain.com
  User ubuntu
  IdentityFile ~/.ssh/oci_private_key
  StrictHostKeyChecking no
  ProxyCommand cloudflared access ssh --id 'XXXXXXXXXX' --secret 'YYYYYYYYYYY' --hostname %h
```

Next, ensure `cloudflared` is also installed on your local workstation and then attempt to SSH into the instance with 
`ssh node1-cf`. If this works, then you're ready to proceed to the next step.

### Dockerhub

Create a new [Dockerhub](https://hub.docker.com/) repository and ensure you've created an access token for deployment 
automation dedicated to pushing and pulling images.

### Github

#### Environment 
Create a Github environment named `prod` and create a Github Secret named `SSH_PRIVATE_KEY` with a private key to your 
OCI instance in this format:

    ```shell
    -----BEGIN RSA PRIVATE KEY-----
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    ...
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    -----END RSA PRIVATE KEY-----
    ```

Next, create Repository secrets named `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` and store your Dockerhub access token info.
Additionally, create two more Github repository secrets named `CF_ACCESS_CLIENT_ID` and `CF_ACCESS_CLIENT_SECRET` and store
your Cloudflare Service Auth token credentials. Also create a Github repository variables named `DOCKERHUB_ACCOUNT` and 
`MKDOCS_APP_NAME` and store the name of your Dockerhub account and repository respectively. The repository should be named 
after the app. 

Additionally, for Prometheus and Grafana support, create two additional variables `PROM_TAG` and `GRAFANA_TAG` with the
dockerhub tags you wish to use for those two images. To set the initial admin credentials for Grafana, create two more 
secrets named `GRAFANA_ADMIN_USER` and `GRAFANA_ADMIN_PASSWORD`. 

#### Actions

Lastly, initiate a deployment by going to the Actions tab and triggering the prod workflow using the Workflow dispatch menu.


At this point, if everything went well your Mkdocs based website should be viewable at the domain name you selected!

#### Tech Stack

The following technologies are utilized in this repository:

Github (Actions/Environments)  
Docker  
Oracle Cloud Infrastructure  
Cloudflare (Tunnels/Applications/DNS)  
Mkdocs  
Shell Scripting  
Ansible
Grafana
Prometheus
