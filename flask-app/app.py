import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from agents import lookup

load_dotenv()
app = Flask(__name__)


@app.route("/linkedInLookup", methods=["GET"])
def linkedin_lookup():
    if(request.method == "GET"):
        name = request.args.get("name")
        # return jsonify(
        #     {
        #         "response":
        #     }
        # )
        return lookup(name)

if __name__ == '__main__':
    app.run(port=os.getenv('FLASK_API_PORT'))

