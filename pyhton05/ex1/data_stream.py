from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    
    def __init__(self, stream_id):
        self.stream_id = stream_id
    
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
        = None) -> List[Any]:
        ...

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ...


class SensorStream(DataStream):
    
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.data_type = "Environmental Data"
        self.analysis_total = 0
    
    def process_batch(self, data_batch: List[Any]) -> str:
        
        if not data_batch:
            return "No data is provided"
        else:
            temp = 0
            temp_total = 0
            for ele in data_batch:
                if isinstance(ele, dict):
                    self.analysis_total += len(ele)
                    temp += ele.get('temp', 0)
                    temp_total += 1
                else:
                    return "The data is not well structured (dict)"
            return f"Sensor analysis: {self.analysis_total} readings processed, avg temp: {temp / temp_total}°C"
        
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "processed_count": self.analysis_total,
        }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
        = None) -> List[Any]:

        if not data_batch:
            return "No data is provided"
        else:
            temp = 0
            temp_total = 0
            for ele in data_batch:
                if isinstance(ele, dict):
                    self.analysis_total += len(ele)
                    temp += ele.get('temp', 0)
                    temp_total += 1
                else:
                    return "The data is not well structured (dict)"
            return f"Sensor analysis: {self.analysis_total} readings processed, avg temp: {temp / temp_total}°C"

class TransactionStream(DataStream):
    
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.data_type = "Financial Data"
        self.analysis_total = 0
    
    def process_batch(self, data_batch: List[Any]) -> str:
        
        if not data_batch:
            return "No data is provided"
        else:
            net_flow = 0
            for ele in data_batch:
                if isinstance(ele, dict):
                    operation = ele['operation']
                    amount = ele['amount']
                    net_flow += amount if operation == "buy" else -amount
                else:
                    return "The data is not well structured (dict)"
            sign = "+" if net_flow > 0 else ""
            self.analysis_total = len(data_batch)
            return f"Transaction analysis: {self.analysis_total} operations, net flow: {sign}{net_flow} units"
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "processed_count": self.analysis_total,
        }


class EventStream(DataStream):
    
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.data_type = "System Events"
        self.analysis_total = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        
        if not data_batch:
            return "No data is provided"
        else:
            errors = 0
            temp_total = 0
            for ele in data_batch:
                self.analysis_total += len(ele)
                if isinstance(ele, list):
                    for event in ele:
                        errors += 1 if event.lower() == "error" else 0
                else:
                    return "The data is not well structured (list)"
            return f"Event analysis: {self.analysis_total} events, {errors} error detected"
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "processed_count": self.analysis_total,
        }


class StreamProcessor:

    stream_objects = []
    
    def process_all(self, batches: List[dict]):
        for ele in batches:
            a = ele['stream']
            StreamProcessor.stream_objects.append(a)
            b = ele['data']

            a.process_batch(b)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        for stream in StreamProcessor.stream_objects:
            yield stream.get_stats()

if __name__ == "__main__":

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_01 = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_01.stream_id}, Type: {sensor_01.data_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    sensor_batch = [{"temp": 22.5, "humidity": 65, "pressure": 1013}]
    print(sensor_01.process_batch(sensor_batch))

    print("\nInitializing Transaction Stream...")
    trans_01 = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans_01.stream_id}, Type: {trans_01.data_type}")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    trans_batch = [
        {"operation": "buy", "amount": 100},
        {"operation": "sell", "amount": 150},
        {"operation": "buy", "amount": 75}
        ]
    print(trans_01.process_batch(trans_batch))

    print("\nInitializing Event Stream...")
    event_01 = EventStream("EVENT_001")
    print(f"Stream ID: {event_01.stream_id}, Type: {event_01.data_type}")
    print("Processing event batch: [login, error, logout]")
    event_batch = [["login", "error", "logout"]]
    print(event_01.process_batch(event_batch))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    sensor_02 = SensorStream("SENSOR_002")
    trans_02 = TransactionStream("TRANS_002")
    event_02 = EventStream("EVENT_002")

    processor = StreamProcessor()

    batches: List[dict] = [
        {"stream": sensor_02, "data": [{"temp": 22.5}, {"temp": 29.5}]},
        {"stream": trans_02, "data": [
            {"operation": "buy", "amount": 50},
            {"operation": "sell", "amount": 200},
            {"operation": "buy", "amount": 80},
            {"operation": "buy", "amount": 120},
        ]},
        {"stream": event_02, "data": [["login", "error", "logout"]]}
    ]

    processor.process_all(batches)
    gen = processor.get_stats()


    print("Batch 1 Results:")
    curr = next(gen)
    print(f"- Sensor data: {curr['processed_count']} readings processed")
    curr = next(gen)
    print(f"- Transaction data: {curr['processed_count']} operations processed")
    curr = next(gen)
    print(f"- Event data: {curr['processed_count']} events processed")
