from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters slack_name and track
    slack_name = request.args.get('slack_name')
    track_code = request.args.get('track')

    # Get the current UTC time
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Create the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": datetime.datetime.now().strftime("%A"),
        "utc_time": utc_time,
        "track": track_code,
        "github_file_url": "https://github.com/Resa200/HNGX-Internship-Tasks/blob/master/TASK1/api.py",
        "github_repo_url": "https://github.com/Resa200/HNGX-Internship-Tasks",
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
