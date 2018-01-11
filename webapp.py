from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response", methods=['GET', 'POST'])
def render_response():
    if request.method == 'POST':
        color = request.forms['color']   
    else:    
        color = request.args['color']
    #request object
    #args is = MultiDict (multiple values for one key)
    #The information in args is visible in the url for the page being requested
    if color == 'blue':
        reply = "Thats my favorite color too!"
    else:
        reply = "My favorite colors blue"
    return render_template('response.html', response = reply)
        
if __name__=="__main__":
    app.run(debug=False, port=54321)
