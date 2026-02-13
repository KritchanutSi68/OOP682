from abc import ABC, abstractmethod
import csv

class ILogSource(ABC):
    @abstractmethod
    def read_logs(self):
        pass

class FileLogSource(ILogSource):
    def read_logs(self):
        print("Reading logs from .txt file...")
        return ["Log 1", "Log 2"]
    
class CsvLogSource(ILogSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_logs(self):
        print(f"Reading logs from CSV: {self.file_path}")
        logs = []
      
        return ["CSV Log A", "CSV Log B", "CSV Log C"]
    
class LogServiceFactory:
    @staticmethod
    def get_source(source_type: str) -> ILogSource:
        if source_type == "txt":
            return FileLogSource()
        elif source_type == "csv":
            return CsvLogSource("data.csv")
        raise ValueError("Unknown source type")

source_type_from_ui = "csv" 

log_source = LogServiceFactory.get_source(source_type_from_ui)

print(log_source.read_logs())
