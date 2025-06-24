# Fine-Tuning Examples

This project demonstrates how to fine-tune an Azure OpenAI model using the OpenAI Python SDK.

## Project Structure

- `fine_tune.py` — Main script to upload training data, start a fine-tuning job, monitor progress, and test the fine-tuned model.
- `train_data.jsonl` — Training data in JSONL format.
- `.env` — Environment variables for Azure OpenAI credentials (not committed to git).
- `requirements.txt` — Python dependencies.

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   pip install python-dotenv
   ```

3. **Configure environment variables:**

   Create a `.env` file in the project root with the following content:
   ```
   AZURE_OPENAI_API_TYPE=azure
   AZURE_OPENAI_ENDPOINT=<your-endpoint>
   AZURE_OPENAI_API_VERSION=<api-version>
   AZURE_OPENAI_KEY=<your-api-key>
   ```

4. **Prepare your training data:**

   Edit `train_data.jsonl` with your training examples in the required format.

## Usage

Run the fine-tuning script:

```sh
python fine_tune.py
```

The script will:
- Upload the training data file to Azure OpenAI.
- Wait for the file to be processed.
- Start a fine-tuning job.
- Monitor the job status.
- Test the fine-tuned model with a sample prompt if successful.

## Notes

- Make sure your Azure OpenAI resource is properly configured and you have the correct permissions.
- The `.env` file is excluded from version control via `.gitignore`.

## License

MIT License
