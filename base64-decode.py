import base64

# Our Base64 encoded string
encodedStr = "aGVsbG8gd29ybGQxMjMhPyQ="

# Decoding the string
decodedBytes = base64.b64decode(encodedStr)
decodedStr = str(decodedBytes, "utf-8")

# Printing the decoded string
print(decodedStr)  # Outputs: hello world123!?$
