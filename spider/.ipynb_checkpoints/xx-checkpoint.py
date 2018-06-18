def response(flow):
    flow.response.headers["BOOM"] = "boom!boom!boom!"
    mitmdump http://localhost:8080/ -p 8321 --set block_global=false