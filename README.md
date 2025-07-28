# Sistema WebGIS

Sistema completo de WebGIS com backend Flask e frontend interativo para visualização de camadas GeoJSON.

## 🚀 Funcionalidades

- **Mapa Interativo**: Visualização de mapas com Leaflet.js
- **Gerenciamento de Camadas**: Upload e administração de arquivos GeoJSON
- **Painel de Administração**: Interface web para gerenciar camadas
- **Estilos Personalizados**: Configuração de estilos para cada camada
- **Controle de Visibilidade**: Ativar/desativar camadas dinamicamente
- **Popups Informativos**: Exibição de propriedades dos elementos

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.7+**
- **Flask**: Framework web
- **SQLAlchemy**: ORM para banco de dados
- **SQLite**: Banco de dados
- **Werkzeug**: Utilitários web

### Frontend
- **HTML5/CSS3/JavaScript**
- **Leaflet.js**: Biblioteca de mapas interativos
- **OpenStreetMap**: Camada base de mapas

## 📁 Estrutura do Projeto

```
/
├── src/
│   ├── app.py                 # Aplicação Flask principal
│   ├── templates/
│   │   ├── index.html         # Página principal do mapa
│   │   ├── admin_login.html   # Página de login
│   │   └── admin_panel.html   # Painel de administração
│   └── static/
│       ├── js/
│       └── css/
├── uploads/                   # Diretório para arquivos temporários
├── requirements.txt           # Dependências Python
└── README.md                 # Este arquivo
```

## 🚀 Instalação e Configuração

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar Banco de Dados

O banco de dados SQLite será criado automaticamente na primeira execução.

### 3. Executar a Aplicação

```bash
cd src
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

## 🔐 Credenciais de Acesso

### Painel de Administração
- **Usuário**: `admin`
- **Senha**: `admin123`

> ⚠️ **Importante**: Altere essas credenciais em produção!

## 📖 Como Usar

### 1. Acessar o Mapa Principal
- Acesse `http://localhost:5000`
- O mapa será carregado com as camadas ativas
- Use o painel lateral para controlar a visibilidade das camadas

### 2. Acessar o Painel de Administração
- Clique em "⚙️ Administração" no mapa principal
- Ou acesse diretamente: `http://localhost:5000/admin/login`
- Faça login com as credenciais fornecidas

### 3. Adicionar Camadas GeoJSON
- No painel de administração, use o formulário "Adicionar Nova Camada"
- Preencha o nome e descrição
- Faça upload do arquivo GeoJSON
- Opcionalmente, configure estilos personalizados
- Clique em "Adicionar Camada"

### 4. Gerenciar Camadas
- Visualize todas as camadas na tabela "Camadas Existentes"
- Ative/desative camadas conforme necessário
- Exclua camadas que não são mais necessárias

## 🎨 Configuração de Estilos

Para personalizar a aparência das camadas, use JSON no campo "Configuração de Estilo":

```json
{
  "color": "#ff0000",
  "weight": 3,
  "opacity": 0.8,
  "fillColor": "#ffff00",
  "fillOpacity": 0.5
}
```

### Propriedades Disponíveis:
- `color`: Cor da borda
- `weight`: Espessura da borda
- `opacity`: Opacidade da borda
- `fillColor`: Cor de preenchimento
- `fillOpacity`: Opacidade do preenchimento
- `dashArray`: Padrão de linha tracejada

## 📊 Formatos Suportados

- **GeoJSON** (`.geojson`, `.json`)
- Tipos de geometria: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon

## 🔧 API Endpoints

### Públicos
- `GET /` - Página principal do mapa
- `GET /api/admin/layers/active` - Listar camadas ativas

### Autenticados (requer login)
- `POST /api/admin/login` - Fazer login
- `POST /api/admin/logout` - Fazer logout
- `GET /admin` - Painel de administração
- `GET /api/admin/layers` - Listar todas as camadas
- `POST /api/admin/layers` - Adicionar nova camada
- `DELETE /api/admin/layers/{id}` - Excluir camada
- `POST /api/admin/layers/{id}/toggle` - Ativar/desativar camada

## 🛡️ Considerações de Segurança

### Para Produção:
1. **Alterar a chave secreta** em `app.py`
2. **Implementar autenticação robusta** (hash de senhas)
3. **Usar HTTPS**
4. **Configurar CORS** adequadamente
5. **Validar uploads** de arquivos
6. **Implementar rate limiting**

## 🐛 Solução de Problemas

### Erro ao carregar camadas
- Verifique se o arquivo GeoJSON é válido
- Confirme se o servidor está rodando
- Verifique os logs do console do navegador

### Erro de permissão de upload
- Verifique se o diretório `uploads/` existe
- Confirme as permissões de escrita

### Erro de banco de dados
- Delete o arquivo `app.db` e reinicie a aplicação
- Verifique se o SQLite está instalado

## 📝 Logs

Os logs da aplicação aparecem no terminal onde o Flask está rodando. Para logs mais detalhados, modifique o nível de debug em `app.py`.

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🆘 Suporte

Para suporte ou dúvidas:
- Abra uma issue no GitHub
- Consulte a documentação do Leaflet.js
- Verifique a documentação do Flask

---

Desenvolvido com ❤️ para facilitar a visualização de dados geoespaciais.