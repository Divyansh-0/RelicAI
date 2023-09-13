import json

def generate_monument_summary(total_time, knowledge_level, interest):
    # Load the priorities list from the JSON file
    with open('priorities.json', 'r') as priorities_file:
        priorities = json.load(priorities_file)

    # Calculate the sum of weights in priorities
    total_weight = sum(item['weight'] for item in priorities)
    
    # Calculate the normalized weight per monument
    normalized_weights = [(item['monument_name'], item['weight'] / total_weight) for item in priorities]

    # Calculate the word limit per monument based on the given words per second
    words_per_second = 2
    word_limit = normalized_weights[0][1] * words_per_second * total_time

    # Generate the list of monument summaries
    monument_summaries = []
    for monument, normalized_weight in normalized_weights:
        prompt = f"For a tourist of {knowledge_level} background knowledge and particularly interested in {interest}, summarize the text to {int(normalized_weight * words_per_second * total_time)} words."
        monument_summaries.append((monument, prompt))

    return monument_summaries


results = generate_monument_summary(3600, "AI", "historical architecture")
for monument, prompt in results:
    print(f"Monument: {monument}\nPrompt: {prompt}\n")