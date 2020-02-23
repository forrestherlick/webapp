from flask import Flask, jsonify
import re
app =Flask(__name__)
@app.route('/')
def get_search(txt="yada",search="ya"):
    x = re.findall(search,txt)
    if (x):
        return("Yes, there is at least one match!")
    else:
        return("no match")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

