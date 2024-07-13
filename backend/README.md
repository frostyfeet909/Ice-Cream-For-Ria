# Backend

## Docker

### Build and Run

```bash
docker build -f docker/api.Dockerfile -t api .
docker run -it --rm --name api -p 8080:80 api
```