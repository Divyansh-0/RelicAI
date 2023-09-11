from DeepImageSearch import Search_Setup
import os
import pandas as pd
import DeepImageSearch.config as config


class MySearchSetup(Search_Setup):
    def run_index(self, flag):
        """
        Indexes the images in the image_list and creates an index file for fast similarity search.
        """
        if len(os.listdir(f"metadata-files/{self.model_name}")) == 0:
            data = self._start_feature_extraction()
            self._start_indexing(data)
        else:
            if flag.lower() == "yes":
                data = self._start_feature_extraction()
                self._start_indexing(data)
            else:
                print("\033[93m Meta data already Present, Please Apply Search!")
                print(os.listdir(f"metadata-files/{self.model_name}"))
        self.image_data = pd.read_pickle(
            config.image_data_with_features_pkl(self.model_name)
        )
        self.f = len(self.image_data["features"][0])
