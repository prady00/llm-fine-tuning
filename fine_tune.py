import os
import time
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch credentials from env
api_key = os.getenv("AZURE_OPENAI_KEY")
api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

if not all([api_key, api_base, api_version]):
    raise EnvironmentError("Missing one or more Azure OpenAI environment variables.")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=api_base,
    api_version=api_version
)

# Step 1: Upload the training file
print("Uploading training file...")
with open("train_data.jsonl", "rb") as f:
    file = client.files.create(file=f, purpose="fine-tune")

print(f"File uploaded: {file.id}")

# Step 2: Wait for file processing to complete
print("Waiting for file to be processed...")
while True:
    file_status = client.files.retrieve(file.id)
    print(f"File status: {file_status.status}")
    if file_status.status == "processed":
        break
    elif file_status.status == "error":
        raise RuntimeError("File processing failed.")
    time.sleep(5)

# Step 3: Create fine-tuning job
print("Starting fine-tuning job...")
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-35-turbo"
)
print(f"Fine-tuning Job ID: {job.id}")

# Step 4: Monitor fine-tuning job
print("Monitoring job status...")
while True:
    job_status = client.fine_tuning.jobs.retrieve(job.id)
    print(f"Job Status: {job_status.status}")
    if job_status.status in ["succeeded", "failed", "cancelled"]:
        break
    time.sleep(20)

# Step 5: Test the fine-tuned model
if job_status.status == "succeeded":
    fine_tuned_model = job_status.fine_tuned_model
    print("Fine-tuned Model ID:", fine_tuned_model)

    response = client.chat.completions.create(
        model=fine_tuned_model,
        messages=[
            {"role": "user", "content": "Who wrote Hamlet?"}
        ]
    )
    print("Model Output:", response.choices[0].message.content)
else:
    print("Fine-tuning failed.")
