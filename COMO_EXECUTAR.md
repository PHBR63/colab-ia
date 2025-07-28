# 🚀 Como Executar o Sistema WebGIS

## Passos Rápidos para Execução

### 1. Instalar Dependências
```bash
pip install flask flask-sqlalchemy werkzeug
# ou
pip install -r requirements.txt
```

### 2. Executar a Aplicação
```bash
cd src
python3 app.py
```

### 3. Acessar o Sistema
- **Mapa Principal**: http://localhost:5000
- **Painel Admin**: http://localhost:5000/admin/login
- **Credenciais**: `admin` / `admin123`

### 4. Testar Upload de Camadas
1. Faça login no painel de administração
2. Use o arquivo `exemplo_geojson.json` para teste
3. Configure estilos opcionais:
   ```json
   {"color": "#ff0000", "weight": 3, "fillOpacity": 0.5}
   ```

## 🎯 Funcionalidades Principais

✅ **Mapa Interativo**: Visualização com Leaflet.js  
✅ **Upload GeoJSON**: Carregamento de arquivos geoespaciais  
✅ **Painel Admin**: Interface de administração completa  
✅ **Controle de Camadas**: Ativar/desativar camadas  
✅ **Estilos Personalizados**: Configuração visual  
✅ **Popups Informativos**: Detalhes dos elementos  

## 🔧 Resolução de Problemas

### Erro de Dependências
```bash
pip install --break-system-packages flask flask-sqlalchemy werkzeug
```

### Erro de Porta em Uso
```bash
lsof -ti:5000 | xargs kill -9
```

### Banco de Dados Corrompido
```bash
rm src/app.db
# A aplicação criará um novo banco automaticamente
```

## 📁 Estrutura do Projeto

```
/
├── src/
│   ├── app.py                 # Backend Flask
│   ├── templates/             # Templates HTML
│   │   ├── index.html         # Mapa principal
│   │   ├── admin_login.html   # Login admin
│   │   └── admin_panel.html   # Painel admin
│   └── app.db                 # Banco SQLite (criado automaticamente)
├── uploads/                   # Arquivos temporários
├── exemplo_geojson.json       # Arquivo de exemplo
├── test_webgis.py            # Script de teste
├── requirements.txt          # Dependências
└── README.md                 # Documentação completa
```

## 🌟 Próximos Passos

1. **Personalização**: Modifique estilos CSS nos templates
2. **Segurança**: Altere credenciais em produção
3. **Mapas Base**: Configure diferentes provedores de tiles
4. **Validação**: Implemente validação robusta de GeoJSON
5. **Performance**: Otimize para grandes datasets

---

**💡 Dica**: Use o comando `python3 test_webgis.py --info` para ver informações detalhadas do sistema!