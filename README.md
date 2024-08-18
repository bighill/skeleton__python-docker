# Python Docker Skeleton

- Run python in disposable container
- Consistent environment seperate from python on the host system

## Usage

Write/put code here with `main.py` as the entrypoint.

Or edit the filename in `Dockerfile`.

```
CMD ["python", "main.py"]
```

Run

```bash
./run.sh
```

> The first run will need to download images. Subsequent runs will be quicker.
