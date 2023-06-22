from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


tokenizer = AutoTokenizer.from_pretrained('my_model_directory')
model = AutoModelForSeq2SeqLM.from_pretrained('my_model_directory')


# Define summarization function
def summarize(text):
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
    return summary[0]['summary_text']

# Example usage
text = "A nine-metre-long corridor has been discovered close to the main entrance of the 4,500-year-old Great Pyramid of Giza. The discovery within the pyramid was made under the ScanPyramids project. Since 2015, it has been using non-invasive technology including infrared thermography, 3D simulations and cosmic-ray imaging to peer inside the structure."

summary = summarize(text)
print(summary)