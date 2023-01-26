from flask import Flask, request, jsonify
import json

from utils.email import extract_emails


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

'''
get the num of total emails in the raw input
'''
@app.route('/email_extract', methods=["PUT", "POST"])
def email_extract():
    if request.method == 'POST':
        dic = json.loads(request.get_data())
        raw = dic['raw_text']
    elif request.method == "PUT":
        raw = request.args.get('raw_text')
    num = extract_emails(raw)
    ans = {"total_email_ids": num}
    return jsonify(ans)

