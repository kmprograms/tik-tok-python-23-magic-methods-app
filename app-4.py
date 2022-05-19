class FileManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def send_text(self, text: str):
        self.file.write(f'{text}\n')

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


def main() -> None:
    with FileManager('data.txt') as fm:
        fm.send_text('Line 1')
        fm.send_text('Line 2')

if __name__ == '__main__':
    main()