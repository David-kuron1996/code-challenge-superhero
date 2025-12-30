from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# GET all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([h.to_dict() for h in heroes]), 200

# GET all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([p.to_dict() for p in powers]), 200

# POST hero power
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    hero_id = data.get("hero_id")
    power_id = data.get("power_id")
    strength = data.get("strength")

    # Validate hero, power, and strength
    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    if not hero or not power:
        return jsonify({"errors": ["Invalid hero_id or power_id"]}), 400
    if strength not in ["Strong", "Average", "Weak"]:
        return jsonify({"errors": ["Invalid strength value"]}), 400

    # Create hero power
    hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        "id": hero_power.id,
        "hero_id": hero_id,
        "power_id": power_id,
        "strength": strength,
        "hero": hero.to_dict(),
        "power": power.to_dict()
    }), 201

if __name__ == "__main__":
    app.run(debug=True)