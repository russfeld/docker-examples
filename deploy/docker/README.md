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

