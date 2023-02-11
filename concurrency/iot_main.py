"""
Module to declare the main function and run the application.
"""

import asyncio
from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IoTService


async def main() -> None:
    """
    Main function to call the service
    """
    service = IoTService()

    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()

    hue_light_id = service.register_device(hue_light)
    speaker_id = service.register_device(speaker)
    toilet_id = service.register_device(toilet)

    wakeup_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON,
                "Miles Davis - Kind of Blue")
    ]

    sleep_program = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(toilet_id, MessageType.FLUSH),
        Message(toilet_id, MessageType.CLEAN)
    ]

    service.run_program(wakeup_program)
    service.run_program(sleep_program)


if __name__ == "__main__":
    asyncio.run(main())
