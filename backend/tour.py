import json
import time

from gradio_client import Client
from prompt import generate_monument_summary


def guide_tour(Time, Interest, Ip=""):
    conv_history = [["system", "You are a helpful assistant."], ["user", "Howdy!"]]
    monument_data = {}

    client = Client("https://1bbf1e9547bcd82c2d.gradio.live")
    qs_string = generate_monument_summary(Time, Ip, Interest)

    if qs_string is not None:
        ind = 3
        for i, query in enumerate(qs_string):
            if query is not None:
                name, a = query
                tour_message = f"For the Monument {name} Given {a}"
                print(f"Query {i+1}: {tour_message}")

                # Update the conv
                conv_history.append(["user", tour_message])
                with open("conversation.json", "w") as json_file:
                    json.dump(conv_history, json_file)

                #
                result = client.predict(tour_message, "conversation.json", fn_index=0)
                # print("API Response:", result)

                _, fl = result

                with open(fl, "r") as json_file:
                    result_data = json.load(json_file)
                    json_data = {}
                    json_data["statements"] = result_data

                    specific_part = json_data["statements"][ind][1]
                    print(ind)
                    print("Specific Part:", specific_part)
                    monument_data[name] = specific_part

                ind += 1
                #  wait for 30 s
                if i < len(qs_string) - 1:
                    print("Waiting for 30 seconds before the next API call.")
                    time.sleep(30)

    with open("monument_data.json", "w") as json_file:
        json.dump(monument_data, json_file, indent=4)


guide_tour(2, "Materials Used", "Medium Level")
