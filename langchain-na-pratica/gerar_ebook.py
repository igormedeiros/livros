import os

SEQUENCE_FILE = os.path.join(os.path.dirname(__file__), 'sequence.txt')
EBOOK_FILE = os.path.join(os.path.dirname(__file__), 'ebook.md')
PROJECT_ROOT = os.path.dirname(__file__)


def main():
    with open(SEQUENCE_FILE, 'r', encoding='utf-8') as seq:
        files = [line.strip() for line in seq if line.strip()]

    # Zera o arquivo .md antes de iniciar
    with open(EBOOK_FILE, 'w', encoding='utf-8') as ebook:
        pass

    with open(EBOOK_FILE, 'a', encoding='utf-8') as ebook:
        for fname in files:
            chapter_path = os.path.join(PROJECT_ROOT, fname)
            chapter_path = os.path.abspath(chapter_path)
            if os.path.exists(chapter_path):
                with open(chapter_path, 'r', encoding='utf-8') as f:
                    ebook.write(f'<!-- {fname} -->\n')
                    ebook.write(f.read())
                    ebook.write('\n\n')
            else:
                ebook.write(f'<!-- {fname} NOT FOUND -->\n\n')
    print(f"Arquivo '{EBOOK_FILE}' gerado com sucesso.")

    # Converter ebook.md para ebook.docx usando pandoc
    DOCX_FILE = EBOOK_FILE.replace('.md', '.docx')
    # Checa se o pandoc está instalado
    import shutil
    if shutil.which('pandoc') is not None:
        try:
            exit_code = os.system(f"pandoc '{EBOOK_FILE}' -o '{DOCX_FILE}'")
            if exit_code == 0:
                print(f"Arquivo '{DOCX_FILE}' gerado com sucesso.")
            else:
                print(f"Falha ao converter '{EBOOK_FILE}' para DOCX. Verifique se o comando pandoc está funcionando corretamente.")
        except Exception as e:
            print(f"Erro ao converter para DOCX: {e}")
    else:
        print("Pandoc não está instalado. Instale o pandoc para converter o arquivo markdown em docx.")

if __name__ == '__main__':
    main()
