## Docker Deployment

Install Docker

https://docs.docker.com/engine/install/ubuntu/

Add user to docker group

```bash
sudo usermod -aG docker russfeld
```

Log out and log in again

Check that you can access Docker

```bash
docker ps
```

Make sure `deploy/traefik/acme.json` has 600 permissions

```bash
sudo chmod 600 acme.json
```

Log in to the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry) if needed. This will create the required `~/.docker/config.json` file. 

Make sure the files in the `symlinks` folder are correctly linked to their respective configuration files. 

Make sure a DNS entry points to the server and update all container configurations to use that hostname. This example uses `dev.russfeld.me`.

Start the entire deployment using Docker Compose:

```bash
docker compose up -d
```