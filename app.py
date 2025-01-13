from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Veritabanı konfigürasyonu
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Puan modeli
class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # İsim-soyisim
    hobbies = db.Column(db.String(500), nullable=False)  # Hobiler
    ai_lib = db.Column(db.String(50), nullable=False)
    ml_lib = db.Column(db.String(50), nullable=False)
    cv_algo = db.Column(db.String(50), nullable=False)
    cv_lib = db.Column(db.String(50), nullable=False)
    nlp_model = db.Column(db.String(50), nullable=False)
    nlp_lib = db.Column(db.String(50), nullable=False)
    framework = db.Column(db.String(50), nullable=False)
    flask_lib = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)

# İlk çalışma için veritabanı oluştur
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Form verilerini al
        name = request.form.get('name')
        hobbies = request.form.get('hobbies')
        ai_lib = request.form.get('ai_lib')
        ml_lib = request.form.get('ml_lib')
        cv_algo = request.form.get('cv_algo')
        cv_lib = request.form.get('cv_lib')
        nlp_model = request.form.get('nlp_model')
        nlp_lib = request.form.get('nlp_lib')
        framework = request.form.get('framework')
        flask_lib = request.form.get('flask_lib')
        
        # Puan hesapla
        score = 0
        if ai_lib == 'TensorFlow':
            score += 12.5
        if ml_lib == 'Scikit-Learn':
            score += 12.5
        if cv_algo == 'ResNet':
            score += 12.5
        if cv_lib == 'OpenCV':
            score += 12.5
        if nlp_model == 'BERT':
            score += 12.5
        if nlp_lib == 'NLTK':
            score += 12.5
        if framework == 'Hepsi':
            score += 12.5
        if flask_lib == 'Flask-RESTful':
            score += 12.5

        # Puanı veritabanına kaydet
        new_score = Score(
            name=name, hobbies=hobbies, ai_lib=ai_lib, ml_lib=ml_lib,
            cv_algo=cv_algo, cv_lib=cv_lib, nlp_model=nlp_model,
            nlp_lib=nlp_lib, framework=framework, flask_lib=flask_lib, score=score
        )
        db.session.add(new_score)
        db.session.commit()

        # En yüksek puanı al
        best_score = Score.query.order_by(Score.score.desc()).first().score

        # Puanı kullanıcıya göster
        return render_template('index.html', score=score, best_score=best_score)

    # Geçerli en yüksek puanı al
    best_score = Score.query.order_by(Score.score.desc()).first().score if Score.query.first() else 0
    
    return render_template('index.html', best_score=best_score)

if __name__ == '__main__':
    app.run(debug=True)