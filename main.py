from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import base64
import mimetypes
from fastapi.middleware.cors import CORSMiddleware

# Add this code before your existing routes


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins. You can restrict it to your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Sample User Information
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"


# Request Model for the POST request
class RequestModel(BaseModel):
    data: List[str]
    file_b64: Optional[str] = None  # Optional base64 file string


# Response Model for the GET request
@app.get("/bfhl", status_code=200)
def get_operation_code():
    return {"operation_code": 1}


# POST Endpoint for processing the data and file
@app.post("/bfhl")
async def process_data(request: RequestModel):
    try:
        # Extract data
        data = request.data
        file_b64 = request.file_b64

        # Initialize response fields
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = []

        # Separate numbers and alphabets
        for item in data:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)

        # Determine the highest lowercase alphabet
        lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
        if lowercase_alphabets:
            highest_lowercase_alphabet.append(max(lowercase_alphabets))

        # Handling the file if provided
        file_valid = False
        file_mime_type = None
        file_size_kb = None

        if file_b64:
            try:
                # Decode the base64 file string
                file_data = base64.b64decode(file_b64)
                file_valid = True

                # Get MIME type from binary data
                file_mime_type = mimetypes.guess_type("dummy")[0]

                # Calculate file size in KB
                file_size_kb = len(file_data) / 1024

            except Exception as e:
                file_valid = False

        # Response JSON
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet,
            "file_valid": file_valid,
            "file_mime_type": file_mime_type if file_valid else None,
            "file_size_kb": f"{file_size_kb:.2f}" if file_size_kb else None
        }

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the request")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
