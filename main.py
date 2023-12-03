import os

if __name__ == "__main__":
    palace_to_send = os.environ.get("PLACE_TO_SEND", "postress")  # or kafka
    agr_time = os.environ.get("AGR_PARAM")  # time from env


