import json


def generate_monument_summary(time, knowledge_level, interest):
    # Load the priorities list from the JSON file
    with open("backend/priorities.json", "r") as priorities_file:
        priorities = json.load(priorities_file)

    # Calculate the sum of weights in priorities
    total_weight = float(sum(item["weight"] for item in priorities))

    # Calculate the normalized weight per monument
    normalized_weights = [
        (item["monument_name"], item["weight"] / total_weight) for item in priorities
    ]

    # Calculate the word limit per monument based on the given words per second
    words_per_second = 2.0
    total_time = float(time) * (60.0 * 60.0)
    print(total_time)

    # Generate the list of monument summaries
    monument_summaries = []
    for monument, normalized_weight in normalized_weights:
        # print(type(normalized_weight))
        # print(type(words_per_second))
        # print(type(total_time))
        word_limit = int(normalized_weight * words_per_second * (total_time))
        # prompt = f"For a tourist of {knowledge_level} background knowledge and particularly interested in {interest}, Create a  guided tour about {monument} given the knowledge you have and tell user what they should visit in the {total_time} seconds. Given they have {total_time} seconds , make sure that user's time doesn't go to waste."
        prompt = f"For a tourist of {knowledge_level} background knowledge and particularly interested in {interest}, provide description about monument in less than  {int(normalized_weight * words_per_second * total_time)*0.5} words."
        monument_summaries.append((monument, prompt))

    return monument_summaries


# results = generate_monument_summary(3600.0, "AI", "historical architecture")
# for monument, prompt in results:
#     print(f"Monument: {monument}\nPrompt: {prompt}\n")


# // { "monument_name": "Main Mausoleum", "weight": 5 },
# // { "monument_name": "Taj Mahal Gardens", "weight": 4 },
# // { "monument_name": "Taj Mahal Mosque", "weight": 3 },
# // { "monument_name": "Jawab", "weight": 2 },
# // { "monument_name": "Mehtab Bagh", "weight": 1 },
# // { "monument_name": "Agra Fort", "weight": 1 },
# // { "monument_name": "Fatehpur Sikri", "weight": 1 }
