import random
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate a false statement
def generate_false_statement(prompt, max_length=50):
    # Encode the prompt
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate text with the model
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    
    # Decode the generated text
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Introduce false information
    false_statement = alter_truth(text)
    
    return false_statement

def alter_truth(statement):
    # A method to introduce falsehood by altering specific details
    # In a real scenario, this function should be more sophisticated
    words = statement.split()
    if len(words) < 5:
        return "This statement is too short to alter effectively."
    
    # Simple example of altering the statement
    change_idx = random.randint(0, len(words) - 1)
    words[change_idx] = random.choice(['never', 'not', 'no', 'none', 'nothing', 'nowhere', 'nobody', 'no one'])
    
    return ' '.join(words)

# Example usage
prompt = "is krakow is the capital of the Poland"
false_statement = generate_false_statement(prompt)
print("False Statement:", false_statement)
