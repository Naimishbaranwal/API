from fastapi import FastAPI, Depends,HTTPException,status


blogs={

    "1": "FastAPI prerequisites",
    "2": "Building API with fastAPI"
}

users={
    "a":"Naimish",
    "b":"Sunny"
}




app=FastAPI(title="Dependency_injkection")

development_db=["DB for development"]

def get_db_session():
     return development_db

# def get_blogs_or_404(model:dict,id:str):
#     blog=blogs.get(id)
#     if not blog:
#         raise HTTPException(detail=f"Blog with {id} is not present",
#                             status_code=status.HTTP_404_NOT_FOUND)
#     return blog

class GetObjectOr404:
    def __init__(self,model)->None:
        self.model=model

    def __call__(self,id:str):
        obj=self.model.get(id)
        if not obj:
                raise HTTPException(detail=f"Blog with {id} is not present",
                        status_code=status.HTTP_404_NOT_FOUND)
        return obj



blog_dependency=GetObjectOr404(blogs)
@app.get("/blog/{id}") #endpoint or rout with instance
def get_blogs(blog_name:str=Depends(blog_dependency)):
    return blog_name


user_dependency=GetObjectOr404(users)
@app.get("/user/{id}") #endpoint or rout with instance
def get_blogs(blog_name:str=Depends(user_dependency)):
    return blog_name


@app.post("/items")
def add_item(item:str,db=Depends(get_db_session)):
     db.append(item)
     print(db)
     return {"message":f"added item {item}"}