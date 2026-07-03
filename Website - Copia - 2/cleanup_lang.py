from pathlib import Path

root = Path('.')
for path in root.glob('*.html'):
    text = path.read_text(encoding='utf-8')
    original = text

    text = text.replace('<li class="nav-item lang-nav-item">', '<li class="nav-item d-none">')
    text = text.replace('</li>', '</li>', 1)

    marker_start = "    // ============================================================\n    // 10. LANGUAGE SWITCHER (PT/ES)\n    // ============================================================"
    marker_end = "    // ============================================================\n    // 11. CLOSE MOBILE NAV ON LINK CLICK\n    // ============================================================"

    if marker_start in text and marker_end in text:
        start = text.index(marker_start)
        end = text.index(marker_end)
        replacement = """    // ============================================================\n    // 10. LANGUAGE SWITCHER DISABLED\n    // ============================================================\n    (function initLanguageSwitcher() {\n        window.currentLang = 'pt';\n        document.documentElement.lang = 'pt-BR';\n        try {\n            localStorage.setItem('dibel_lang', 'pt');\n        } catch (e) {}\n    })();\n\n"""
        text = text[:start] + replacement + text[end:]

    text = text.replace("console.log('🌍 Clique no ícone de globo para alternar entre PT e ES.');", "console.log('🌍 Site disponível em português.');")
    text = text.replace("console.log('✅ Clínica Dibel — versão final com serviços redesenhados, equipe atualizada e suporte a PT/ES.');", "console.log('✅ Clínica Dibel — versão final com conteúdo e navegação em português.');")

    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f'updated {path.name}')
