from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Define a dictionary to store track names based on track codes
tracks = {
    "backend": "Backend",  # You can add more tracks as needed
}

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters slack_name and track
    slack_name = request.args.get('slack_name')
    track_code = request.args.get('track')

    # Check if the track_code is valid
    if track_code not in tracks:
        return jsonify({"error": "Invalid track"}), 400

    # Get the current UTC time
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Create the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": datetime.datetime.now().strftime("%A"),
        "utc_time": utc_time,
        "track": tracks[track_code],
        "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
        "github_repo_url": "https://github.com/username/repo",
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
