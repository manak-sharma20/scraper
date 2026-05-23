import requests


def download_bid_pdf(
    url,
    output_path="data/sample.pdf"
):

    response = requests.get(url)

    if response.status_code == 200:

        with open(output_path, "wb") as file:
            file.write(response.content)

        print(
            f"PDF downloaded successfully: "
            f"{output_path}"
        )

    else:

        print(
            f"Failed to download PDF. "
            f"Status code: {response.status_code}"
        )