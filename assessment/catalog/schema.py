json_schema = {
    "name": "post_data",
    "type": "object",
    "properties": {
        "batch_id": {
            "type": "string"
        },
        "objects": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "object_id": {
                            "type": "string"
                        },
                        "data": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": [
                                                "string",
                                                "number",
                                                "boolean",
                                                "null"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "key",
                                        "value"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "object_id",
                        "data"
                    ]
                }
            ]
        }
    },
    "required": [
        "batch_id",
        "objects"
    ]
}
