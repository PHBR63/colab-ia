#!/usr/bin/env python3
"""
Script de teste para demonstrar o funcionamento do sistema WebGIS
"""

import requests
import json
import time
import sys

def test_webgis_system():
    """Testa o sistema WebGIS"""
    
    base_url = "http://localhost:5000"
    
    print("🗺️  TESTANDO SISTEMA WEBGIS")
    print("=" * 50)
    
    # Teste 1: Verificar se o servidor está rodando
    print("\n1. Testando conexão com o servidor...")
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("✅ Servidor está rodando!")
        else:
            print(f"❌ Servidor retornou status: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar com o servidor: {e}")
        print("💡 Certifique-se de que a aplicação Flask está rodando na porta 5000")
        return False
    
    # Teste 2: Verificar endpoint de camadas ativas
    print("\n2. Testando endpoint de camadas ativas...")
    try:
        response = requests.get(f"{base_url}/api/admin/layers/active", timeout=5)
        if response.status_code == 200:
            layers = response.json()
            print(f"✅ Endpoint funcionando! Encontradas {len(layers)} camadas ativas")
            if layers:
                for layer in layers:
                    print(f"   - {layer['name']}: {layer['description']}")
            else:
                print("   ℹ️  Nenhuma camada ativa encontrada (normal para instalação nova)")
        else:
            print(f"❌ Erro no endpoint: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao testar endpoint: {e}")
    
    # Teste 3: Verificar página de login
    print("\n3. Testando página de login...")
    try:
        response = requests.get(f"{base_url}/admin/login", timeout=5)
        if response.status_code == 200 and "WebGIS Admin" in response.text:
            print("✅ Página de login carregou corretamente!")
        else:
            print(f"❌ Erro na página de login: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao acessar página de login: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 TESTE CONCLUÍDO!")
    print("\n📋 PRÓXIMOS PASSOS:")
    print(f"1. Acesse: {base_url}")
    print("2. Para administração: {}/admin/login".format(base_url))
    print("3. Credenciais: admin / admin123")
    print("4. Use o arquivo 'exemplo_geojson.json' para testar upload de camadas")
    
    return True

def show_system_info():
    """Mostra informações sobre o sistema"""
    print("\n📖 INFORMAÇÕES DO SISTEMA WEBGIS")
    print("=" * 50)
    print("🔧 Funcionalidades:")
    print("   • Visualização interativa de mapas com Leaflet.js")
    print("   • Upload e gerenciamento de arquivos GeoJSON")
    print("   • Painel de administração web")
    print("   • Controle de visibilidade de camadas")
    print("   • Estilos personalizados para camadas")
    print("   • Popups informativos para elementos do mapa")
    
    print("\n🌐 URLs Principais:")
    print("   • Mapa Principal: http://localhost:5000")
    print("   • Login Admin: http://localhost:5000/admin/login")
    print("   • Painel Admin: http://localhost:5000/admin")
    
    print("\n📁 Arquivos Principais:")
    print("   • src/app.py - Backend Flask")
    print("   • src/templates/ - Templates HTML")
    print("   • exemplo_geojson.json - Arquivo de exemplo")
    print("   • README.md - Documentação completa")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--info":
        show_system_info()
    else:
        # Aguardar um pouco para o servidor iniciar
        print("⏳ Aguardando servidor iniciar...")
        time.sleep(3)
        test_webgis_system()