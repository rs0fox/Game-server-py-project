from flask import request, jsonify
from app import app, db
from app.models import Score

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    scores = Score.query.order_by(Score.score.desc()).limit(10).all()
    leaderboard = [{'player_name': s.player_name, 'score': s.score} for s in scores]
    return jsonify(leaderboard)

@app.route('/leaderboard', methods=['POST'])
def post_score():
    data = request.get_json()
    new_score = Score(player_name=data['player_name'], score=data['score'])
    db.session.add(new_score)
    db.session.commit()
    return jsonify({'message': 'Score added!'}), 201
