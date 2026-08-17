from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(title="SQL File Reader API")


class SQLRequest(BaseModel):
    database: str
    sql_file: str


@app.get("/")
def root():
    return {"message": "SQL File Reader API is running"}


@app.post("/read-sql")
def read_sql(request: SQLRequest):

    file_path = Path(request.sql_file)

    if not file_path.exists():
        return {"error": "SQL file not found"}

    contents = file_path.read_text()

    return {
        "database": request.database,
        "sql_file": request.sql_file,
        "contents": contents
    }
