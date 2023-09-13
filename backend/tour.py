import json

from gradio_client import Client
from prompt import generate_monument_summary


def guide_tour(Time, Interest, Ip=""):
    conv_history = [["system", "You are a helpful assistant."], ["user", "Howdy!"]]

    with open("conversation.json", "w") as json_file:
        json.dump(conv_history, json_file)

    client = Client("https://327e23bd14dfe9b92d.gradio.live")
    qs_string = generate_monument_summary(Time, Ip, Interest)
    # qs_string = f"I am tourist who is visiting this tourist destination for first time . I have {Time} to visit this place and i have interest in {Interest} and also {Ip} . Please create a curated tour for me given the information i have provided. "
    result = client.predict(qs_string, "conversation.json", fn_index=0)
    print(result)
    _, fl = result

    with open(fl, "r") as json_file:
        result_data = json.load(json_file)
        json_data = {}
        json_data["statements"] = result_data

        return json_data


# a = tour(2, "History", "Medium Level")
# print(a)
