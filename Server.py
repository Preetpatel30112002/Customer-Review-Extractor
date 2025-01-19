from flask import Flask, request, jsonify
from Scraper import extract_review_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from the React frontend

@app.route("/api/reviews", methods=['GET'])
def get_reviews():
    url = request.args.get('page')
    if not url:
        return jsonify({"error": "URL parameter 'page' is required"}), 400

    try:
        reviews = extract_review_data(url)
        return jsonify({"reviews_count": len(reviews), "reviews": reviews})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)