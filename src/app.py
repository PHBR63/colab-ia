from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import json
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['UPLOAD_FOLDER'] = '../uploads/'
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Mude para uma chave segura em produção
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo do banco de dados
class GeoJSONLayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    geojson_data = db.Column(db.Text, nullable=False)
    style_config = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<GeoJSONLayer {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'geojson_data': json.loads(self.geojson_data),
            'style_config': json.loads(self.style_config) if self.style_config else {},
            'active': self.active,
            'created_at': self.created_at.isoformat()
        }

# Rotas principais
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_panel():
    if 'logged_in' not in session:
        return redirect(url_for('admin_login'))
    return render_template('admin_panel.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin_login.html')

# API de autenticação
@app.route('/api/admin/login', methods=['POST'])
def api_admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Credenciais simples para MVP (em produção, usar hash de senha)
    if username == 'admin' and password == 'admin123':
        session['logged_in'] = True
        return redirect(url_for('admin_panel'))
    else:
        return render_template('admin_login.html', error='Credenciais inválidas')

@app.route('/api/admin/logout', methods=['POST'])
def api_admin_logout():
    session.pop('logged_in', None)
    return redirect(url_for('admin_login'))

# API para gerenciar camadas
@app.route('/api/admin/layers', methods=['POST'])
def add_layer():
    if 'logged_in' not in session:
        return jsonify({"error": "Não autenticado"}), 401
    
    try:
        file = request.files.get('geojson_file')
        if not file or not file.filename.endswith('.geojson'):
            return jsonify({"error": "Arquivo GeoJSON válido é obrigatório"}), 400

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)

        with open(file_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        # Validar se é um GeoJSON válido
        if 'type' not in geojson_data:
            return jsonify({"error": "Arquivo GeoJSON inválido"}), 400

        new_layer = GeoJSONLayer(
            name=request.form.get('name', ''),
            description=request.form.get('description', ''),
            geojson_data=json.dumps(geojson_data),
            style_config=request.form.get('style_config', '{}')
        )
        
        db.session.add(new_layer)
        db.session.commit()
        
        # Remover arquivo temporário
        os.remove(file_path)
        
        return jsonify({"message": "Camada adicionada com sucesso!", "layer_id": new_layer.id}), 201
    
    except Exception as e:
        return jsonify({"error": f"Erro ao processar camada: {str(e)}"}), 500

@app.route('/api/admin/layers', methods=['GET'])
def get_all_layers():
    if 'logged_in' not in session:
        return jsonify({"error": "Não autenticado"}), 401
    
    layers = GeoJSONLayer.query.all()
    return jsonify([{
        'id': layer.id,
        'name': layer.name,
        'description': layer.description,
        'active': layer.active,
        'created_at': layer.created_at.isoformat()
    } for layer in layers])

@app.route('/api/admin/layers/active', methods=['GET'])
def get_active_layers():
    layers = GeoJSONLayer.query.filter_by(active=True).all()
    return jsonify([layer.to_dict() for layer in layers])

@app.route('/api/admin/layers/<int:layer_id>', methods=['DELETE'])
def delete_layer(layer_id):
    if 'logged_in' not in session:
        return jsonify({"error": "Não autenticado"}), 401
    
    layer = GeoJSONLayer.query.get_or_404(layer_id)
    db.session.delete(layer)
    db.session.commit()
    return jsonify({"message": "Camada excluída com sucesso!"})

@app.route('/api/admin/layers/<int:layer_id>/toggle', methods=['POST'])
def toggle_layer(layer_id):
    if 'logged_in' not in session:
        return jsonify({"error": "Não autenticado"}), 401
    
    layer = GeoJSONLayer.query.get_or_404(layer_id)
    layer.active = not layer.active
    db.session.commit()
    return jsonify({"message": f"Camada {'ativada' if layer.active else 'desativada'} com sucesso!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)