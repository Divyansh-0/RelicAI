from DeepImageSearch import Load_Data
from my_search_setup import MySearchSetup
import os


def process_img(test_image_path, number_of_images=2):
    print(test_image_path)
    dl = Load_Data()
    image_list = dl.from_folder(folder_list=["D:\RelicAI\img_db"])
    print(image_list)
    st = MySearchSetup(
        image_list, model_name="vgg19", pretrained=True, image_count=None
    )
    # for files in os.walk("D:\RelicAI\img_db"):
    #     for file in files:
    #         print(file)

    # st = Search_Setup(image_list, model_name="vgg19", pretrained=True, image_count=None)
    st.run_index(flag="true")
    # Get similar images
    similar_images = st.get_similar_images(
        image_path=test_image_path,
        number_of_images=number_of_images,
    )
    print(similar_images)
    common_prefix = None
    for key, path in similar_images.items():
        filename = path.split("\\")[-1]

        monument_name = filename.split(".")[0]
        if common_prefix is None:
            common_prefix = monument_name
        else:
            common_prefix = os.path.commonprefix([common_prefix, monument_name])

    if common_prefix.endswith("_"):
        common_prefix = common_prefix[:-1]

    return common_prefix
