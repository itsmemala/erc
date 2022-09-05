"""
This is just a simple client example. Hack it as much as you want. 
"""
import argparse
import logging

import jsonpickle
import pandas as pd
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def run_text(file_path: str, text_field: str, url_emoberta: str) -> None:
    """Send data to the flask server.

    Args
    ----
    file_path: file path with text
    text_field: column header of text to label
    url_emoberta: e.g., http://127.0.0.1:10006/

    """
    input_data = pd.read_json(file_path, lines=True, orient='records')
    output_data = []

    logging.debug("sending text to server...")
    for i,row in input_data.iterrows():
        data = {"text": row[text_field]}
        data = jsonpickle.encode(data)
        response = requests.post(url_emoberta, json=data)
        # logging.info(f"got {response} from server!...")
        response = jsonpickle.decode(response.text)
        output_data.append(response)

    input_data['sentiment_labels']=output_data
    input_data.to_json(file_path)
    logging.info(f"results saved in same file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify room type")
    parser.add_argument("--url-emoberta", type=str, default="http://127.0.0.1:10006/")
    parser.add_argument("--file_path", type=str, required=True)
    parser.add_argument("--text_field", type=str, required=True)

    args = vars(parser.parse_args())

    run_text(**args)
