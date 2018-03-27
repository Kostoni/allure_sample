jsonschemas = {
    "http://httpbin.org/get": {
        "type": "object",
        "properties": {
            "args": {
                "type": "object"
            },
            "headers": {
                "type": "object",
                "properties": {
                    "Accept": {
                        "type": "string",
                        "examples": [
                            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                        ]
                    },
                    "Accept-Encoding": {
                        "type": "string",
                        "examples": [
                            "gzip, deflate"
                        ]
                    },
                    "Connection": {
                        "type": "string",
                        "examples": [
                            "close"
                        ]
                    },
                    "Host": {
                        "type": "string",
                        "examples": [
                            "httpbin.org"
                        ]
                    },
                    "User-Agent": {
                        "type": "string",
                        "examples": [
                            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
                        ]
                    }
                },
                "required": ["Accept", "Accept-Encoding", "Connection", "Host", "User-Agent"],
                "additionalProperties": False
            },
            "origin": {
                "type": "string",
                "examples": [
                    "109.194.155.9"
                ]
            },
            "url": {
                "type": "string",
                "examples": [
                    "http://httpbin.org/get?p-1=1"
                ]
            }
        },
        "required": ["args", "headers", "origin", "url"],
        "additionalProperties": False
    },
    "http://httpbin.org/ip": {
        "type": "object",
        "properties": {
            "origin": {
                "type": "string",
                "examples": [
                    "109.194.155.9"
                ]
            }
        },
        "required": ["origin"],
        "additionalProperties": False
    }
}
