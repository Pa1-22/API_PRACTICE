from transformers import pipeline

# Load GPT-2 model
gen = pipeline("text-generation", model="gpt2")

# Generate the first text
prompt_output = gen(
    "Write a friendly tip about clean code:",
    max_new_tokens=40,
    do_sample=True,
    top_p=0.9,
    temperature=0.8
)[0]["generated_text"]

# Use the first generated text as a new prompt
res = gen(
    prompt_output + " Now write a new related tip:",
    max_new_tokens=50,
    do_sample=True,
    top_p=0.9,
    temperature=0.8
)[0]["generated_text"]

# Print both
print("First Output:\n", prompt_output)
print("\nSecond Output:\n", res)
