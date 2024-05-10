import store
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {
        'Hello': 'World'
        }

@app.get('/peanuts')
def string():
    return 'Hello World'
def run():
    store.get_categories()

if __name__ == '__main__':
    run()