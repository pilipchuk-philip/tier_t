# URL SHORTENER

## Reqirements
* python => 3.9
* virtualenv or similar (For dev check was conda)
## Run & Testings

```
$ conda activate ENV (optional)

$ pip install -r requirements.txt

$ uvicorn main:app --reload 
```
or use docker
```
docker build --tag name:tag .
docker run -d name:tag 
```
URL with Swagger: http://localhost:8000/docs