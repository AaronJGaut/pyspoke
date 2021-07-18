import spoke
import json

def pack_msg(channel, payload=None):
    full_msg = {
        "channel": channel,
        "payload": payload,
    }
    return full_msg

def unpack_msg(full_msg):
    channel = full_msg.get("channel", None)
    payload = full_msg.get("payload", None)
    return channel, payload
