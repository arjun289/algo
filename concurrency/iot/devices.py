from iot.message import MessageType


class HueLightDevice:
    async def connect(self) -> None:
        print("Connecting Hue Light")
        print("Hue Light Connected")

    async def disconnect(self) -> None:
        print("Disconnecting the Hue Light")
        print("Hue Light Connected")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Hue Light Handling message of type {message_type.name} with data [{data}]")
        print('Hue light received message')


class SmartSpeakerDevice:
    async def connect(self) -> None:
        print("Connecting Smart Speaker")
        print("Smart Speaker Connected")

    async def disconnect(self) -> None:
        print("Disconnecting the Smart Speaker")
        print("Smart Speaker Connected")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Smart Speaker Handling message of type {message_type.name} with data [{data}]")
        print('Smart Speaker received message')


class SmartToiletDevice:
    async def connect(self) -> None:
        print("Connecting Smart Toilet Device")
        print("Smart Toilet Device Connected")

    async def disconnect(self) -> None:
        print("Disconnecting the Smart Toilet Device")
        print("Smart Toilet Device Connected")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Smart Toilet Device Handling message of type {message_type.name} with data [{data}]")
        print('Smart Toilet Device received message')
