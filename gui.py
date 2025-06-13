import sys
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QTextEdit, QFileDialog, QHBoxLayout
)
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QThread
from PyQt5.QtGui import QFont

from api import summarize_youtube_playlist_to_structured_excel

class Worker(QObject):
    log = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, playlist_url, output_file):
        super().__init__()
        self.playlist_url = playlist_url
        self.output_file = output_file

    def run(self):
        try:
            self.log.emit("⏳ Starting summarization...\n")
            summarize_youtube_playlist_to_structured_excel(
                self.playlist_url, output_file=self.output_file
            )
            self.log.emit(f"✅ Summary saved to: {self.output_file}\n")
        except Exception as e:
            self.log.emit(f"❌ Error: {str(e)}\n")
        self.finished.emit()

class SummarizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎬 Drama Summarizer - Netflix Style")
        self.setGeometry(200, 100, 700, 400)
        self.setStyleSheet(self.load_styles())
        self.thread = None
        self.worker = None

        self.init_ui()

    def load_styles(self):
        return """
        QWidget {
            background-color: #1e1e2f;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
            font-size: 14px;
        }
        QLineEdit, QTextEdit {
            background-color: #2e2e3e;
            border: 1px solid #444;
            border-radius: 6px;
            padding: 6px;
        }
        QPushButton {
            background-color: #ff4757;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 14px;
        }
        QPushButton:hover {
            background-color: #ff6b81;
        }
        QPushButton:pressed {
            background-color: #e84141;
        }
        QLabel {
            font-weight: bold;
        }
        """

    def init_ui(self):
        layout = QVBoxLayout()

        self.url_label = QLabel("YouTube Playlist URL:")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste your YouTube playlist URL here...")

        self.output_label = QLabel("Save Excel File As:")
        self.output_path_input = QLineEdit()
        self.output_path_input.setPlaceholderText("Click to choose save path...")
        self.output_path_input.setReadOnly(True)
        self.output_path_input.mousePressEvent = self.select_save_path

        self.summarize_button = QPushButton("🎯 Summarize Playlist")
        self.summarize_button.clicked.connect(self.start_summarization)

        self.status_output = QTextEdit()
        self.status_output.setReadOnly(True)
        self.status_output.setStyleSheet("font-size: 13px;")

        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)

        layout.addWidget(self.output_label)
        layout.addWidget(self.output_path_input)

        layout.addWidget(self.summarize_button)
        layout.addWidget(QLabel("Status:"))
        layout.addWidget(self.status_output)

        self.setLayout(layout)

    def select_save_path(self, event):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Select Excel Output", filter="Excel Files (*.xlsx)"
        )
        if filename:
            if not filename.endswith(".xlsx"):
                filename += ".xlsx"
            self.output_path_input.setText(filename)

    def start_summarization(self):
        playlist_url = self.url_input.text().strip()
        output_file = self.output_path_input.text().strip()

        if not playlist_url:
            self.status_output.append("⚠️ Please enter a YouTube playlist URL.")
            return

        if not output_file:
            output_file = "playlist_summary_structured.xlsx"
            self.output_path_input.setText(output_file)

        self.status_output.append("⏳ Initializing...\n")

        self.thread = QThread()
        self.worker = Worker(playlist_url, output_file)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.log.connect(self.status_output.append)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def run_summarization(self, playlist_url, output_file):
        try:
            summarize_youtube_playlist_to_structured_excel(
                playlist_url, output_file=output_file
            )
            self.status_output.append(f"✅ Summary saved to: {output_file}\n")
        except Exception as e:
            self.status_output.append(f"❌ Error: {str(e)}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SummarizerApp()
    window.show()
    sys.exit(app.exec_())
