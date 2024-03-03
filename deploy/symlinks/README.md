## Symlinks

This folder should contain symlinks to various other configurations. Symlinks allow editing the configuration file outside the container without breaking the volume (for containers that support live reloading of configuration). 

### Docker Authentication for Watchtower

* `config.json` -> `~/.docker/config.json`

See https://docs.docker.com/engine/reference/commandline/login/

### Traefik

* `acme.json` -> `../traefik/acme.json`
* `dynamic.json` -> `../traefik/dynamic.json`
* `traefik.json` -> `../traefik/traefik.json`

See https://doc.traefik.io/traefik/getting-started/configuration-overview/ and https://doc.traefik.io/traefik/https/acme/