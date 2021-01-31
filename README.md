
TODO: fix logging going to stdout


# Dynamic DNS (DDNS) for DigitalOcean (DO)

TODO :)

... because why deploy a 1KiB script when you can deploy a 250MiB image?


# Execution

Secrets need to be passed through to the container:

```
docker run -d -t -i \
    -e DO_API_TOKEN='xxxxxxxxxxxxxxx' \
    -e DO_DOMAIN='example.com' \
    -e DO_RECORD='subdomain' \
    do-ddns:latest
```

