from argparse import ArgumentParser
import xml.etree.ElementTree as ET
import random

if __name__ == '__main__':
    parser = ArgumentParser(description="Pick a random show from your PTW list")
    parser.add_argument("mal_list",
                        metavar="LIST",
                        type=str,
                        help="The exported XML from your MAL page.")

    args = parser.parse_args()
    list_tree = ET.parse(args.mal_list)
    tree_root = list_tree.getroot()

    ptw_list = list()
    for anime in tree_root.findall("anime"):
        if anime.find("my_status").text == "Plan to Watch":
            ptw_list.append(anime.find("series_title").text)

    opts = ["y", "n"]
    while True:
        user_in = input("Get random anime? [Y/n]: ").lower().rstrip()
        if user_in not in opts:
            print("Invalid input!\n")
            continue
        elif user_in == "n":
            break

        rand_index = random.randint(0, len(ptw_list))
        print("Your random anime is: {}\n".format(ptw_list[rand_index]))
