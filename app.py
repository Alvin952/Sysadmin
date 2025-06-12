from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        username = request.form.get('username', 'Guest')
        message = "Selamat datang di halaman utama Flask!"
        return render_template('main.html', username=username, message=message)
    else:
        return render_template('main.html', username="Guest", message="Silakan kembali ke halaman awal dan isi nama.")

# ➕ Route baru: halaman dengan tombol redirect ke home
@app.route('/redirector')
def redirector():
    return render_template('redirector.html')

# ➕ Fungsi yang dijalankan saat tombol ditekan (opsional, bisa langsung redirect)
@app.route('/go_home', methods=['POST'])
def go_home():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)





