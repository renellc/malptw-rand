# malptw-rand
Randomly selects an anime listing from your MAL plan to watch section.

## Requirements
- Python 3.2+

## How to get your exported XML MAL file
Go to your MAL anime list page and locate the sidebar on the right. Then click the `Export` button.

![Export Button](https://i.ibb.co/TB9rnhX/mal1.png)

Select anime list from the dropdown.

![Dropdown Selection](https://i.ibb.co/VNGjrLR/image.png)

Then click the following link to download your list. Make sure to extract it into the same folder that has the `malptw_rand.py` script.

![Download list](https://i.ibb.co/rfB7GJf/image.png)


## Usage
First clone/download this repo and `cd` into with your terminal of choice. Make sure to follow the steps above and put your XML MAL file in the repo folder. Then type:

`python malptw_rand.py your_anime_list.xml`

or

`python3 malptw_rand.py your_anime_list.xml`

to get a random anime from your PTW list.
