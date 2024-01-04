import uvicorn
from api import app

if __name__ == "__main__":
    import os
    print(os.getcwd())
    uvicorn.run(
        "main:app",
        reload=True,
        ssl_keyfile="./keys_https/key.pem",
        ssl_certfile="./keys_https/cert.pem"
    )
