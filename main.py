## This is the entrypoint of my application and it contains the code of run the application 

from app.api import app
import uvicorn

if __name__ == "__main__" : 
    uvicorn.run(
            "app.api:app",
            host="0.0.0.0",
            port=8000,
            reload=True)


