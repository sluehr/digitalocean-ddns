# Dynamic DNS (DDNS) client for DigitalOcean

This is yet another DDNS client for [DigitalOcean](https://digitalocean.com) that is intended to be run as a
fire-and-forget Docker container. It is especially useful for running on a NAS appliance that doesn't natively support
DigitalOcean (looking at you, Synology) without requiring dependencies to be installed on the underlying OS... why
deploy a 1KiB script when you can deploy a 250MiB image?

This client will:

* monitor your external IP address for changes;
* update a single `A record` for a domain with a DigitalOcean managed nameserver.

The client does not:

* support `AAAA` records and IPv6 addresses;
* perform health checks or notify you of failures.

Contributions, however, are most welcome!

## Alternatives

People love creating DDNS clients for DO so there are [many alternatives](https://github.com/search?q=digitalocean+ddns) 
for you to consider that offer more features such as custom record types.

# Execution

This script can only update an existing `A record`. The record to update must first be configured in the DO console. The
API token required to access the DigitalOcean APIs can also be generated from the console.

## Environment variables

The script uses the following environment variables to pass secrets to the container:

* `DO_API_TOKEN`: your private API token;
* `DO_DOMAIN`: the domain containing the record to update. For example: `example.com` or `github.com`;
* `DO_RECORD`: the A record being updated. For example: `my` (for `my.example.com`) or `shop` (for `shop.github.com`).

### Docker CLI

```
docker run -d -t -i \
    -e DO_API_TOKEN='xxxxxxxxxxxxxxx' \
    -e DO_DOMAIN='example.com' \
    -e DO_RECORD='subdomain' \
    do-ddns:latest
```

### Docker compose

Use a [docker-compose.yml](https://github.com/sluehr/digitalocean-ddns/blob/main/docker/docker-compose.yml) file:

```
version: "3.0"
services:
  do-ddns:
    image: sluehr/digitalocean-ddns
    restart: unless-stopped
    environment:
      DO_API_TOKEN: 'xxxxxxxxxxxxxxx'
      DO_DOMAIN: 'example.com'
      DO_RECORD: 'subdomain'
```

... and start the container locally with `docker-compose up`. 
