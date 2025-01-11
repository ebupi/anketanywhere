from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# en yüksek puanı saklamak için global bir değişken
best_score = 0

@app.route('/', methods=['GET', 'POST'])
def quiz():
    global best_score

    if request.method == 'POST':
        # form verilerini al
        name = request.form.get('name')
        color = request.form.get('color')
        animal = request.form.get('animal')
        hobbies = request.form.get('hobbies')

        # puan hesapla
        # belirli seçenekeri seçelim 
        score = 0
        if color == 'Blue':
            score += 25
        if animal == 'Dog':
            score += 25
        if hobbies.strip() != '':
            score += 50

        # en yüksek puanı güncelle
        if score > best_score:
            best_score = score

        # Puanı kullanıcıya göster
        return render_template('index.html', score=score, best_score=best_score)

    # GET isteği için HTML sayfasını göster
    return render_template('index.html', best_score=best_score)

if __name__ == '__main__':
    app.run(debug=True)