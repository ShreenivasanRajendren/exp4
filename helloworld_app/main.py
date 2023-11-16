from flask import Flask

app= Flask(_name_)

@app.route('/')
def hello():
    return "Hello World"
    
if _name=='__main_':
    app.run(host='127.0.0.1', port=8080, debug=True)
