# Cloudflare


###### Make GET request using Cloudflare Service Auth Token
```shell
curl -s -X GET \
  -H "CF-Access-Client-ID: ${CF_ACCESS_CLIENT_ID}" \
  -H "CF-Acess-Client-Secret: ${CF_ACCESS_CLIENT_SECRET}" \
  -H "Content-Type: applicationjson" \
  {http_endpoint}
```


###### Make POST request with JSON payload using Cloudflare Service Auth Token
```shell
curl --request POST \
  -H "CF-Access-Client-ID: ${CF_ACCESS_CLIENT_ID}" \
  -H "CF-Acess-Client-Secret: ${CF_ACCESS_CLIENT_SECRET}" \
  -H "Content-Type: applicationjson" \
  --url {http_endpoint} \
  --data '{"key":"value"}' 
```
