import uvicorn

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.app:app", host="localhost", port=8002, log_level="info")