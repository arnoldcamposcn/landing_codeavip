#!/usr/bin/env python3
"""
Script para construir la aplicación para producción
"""
import os
import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None):
    """Ejecuta un comando y maneja errores"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True, capture_output=True, text=True)
        print(f"✅ Comando ejecutado exitosamente: {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando comando: {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    # Obtener el directorio base del proyecto
    base_dir = Path(__file__).parent / "codeauni_vip"
    theme_dir = base_dir / "theme" / "static_src"
    
    print("🚀 Iniciando build para producción...")
    
    # Paso 1: Instalar dependencias de Node.js
    print("\n📦 Instalando dependencias de Node.js...")
    if not run_command("npm install", cwd=theme_dir):
        print("❌ Falló la instalación de dependencias de Node.js")
        sys.exit(1)
    
    # Paso 2: Compilar CSS de Tailwind para producción
    print("\n🎨 Compilando CSS de Tailwind...")
    if not run_command("npm run build-prod", cwd=theme_dir):
        print("❌ Falló la compilación de CSS")
        sys.exit(1)
    
    # Paso 3: Recolectar archivos estáticos de Django
    print("\n📁 Recolectando archivos estáticos...")
    if not run_command("python manage.py collectstatic --noinput", cwd=base_dir):
        print("❌ Falló la recolección de archivos estáticos")
        sys.exit(1)
    
    # Paso 4: Ejecutar migraciones
    print("\n🗄️ Ejecutando migraciones...")
    if not run_command("python manage.py migrate", cwd=base_dir):
        print("❌ Falló la ejecución de migraciones")
        sys.exit(1)
    
    print("\n✅ ¡Build completado exitosamente!")
    print("📋 Resumen:")
    print("   - Dependencias de Node.js instaladas")
    print("   - CSS de Tailwind compilado y minificado")
    print("   - Archivos estáticos recolectados")
    print("   - Migraciones aplicadas")
    print("\n🚀 Tu aplicación está lista para producción!")

if __name__ == "__main__":
    main() 