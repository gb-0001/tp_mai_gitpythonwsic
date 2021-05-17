import uvicorn
from fastapi import FastAPI
import crud

app = FastAPI()

@app.get("/machines")
async def lister_machines():
    return crud.get_list_machines()


#@app.delete("/machine/{id}")
#async def delete_machine():
  #  return crud.get_list_machines()

#@app.put("/machines/{hostname}")
#async def update_machine():
 #   pass

uvicorn.run(app)