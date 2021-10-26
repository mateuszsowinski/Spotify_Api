from libraries import *
import download_data


def generate(artist, fileFormat):
    if fileFormat == "CSV" or fileFormat == "csv":
        df = pd.DataFrame({'album': download_data.albumsTab})
        if len(sys.argv) == 4:
            plik = df.to_csv(fileName + '.csv', index=False)
        else:
            plik = df.to_csv(artist + '.csv', index=False)
    elif fileFormat == "JSON" or fileFormat == "json":

        # with open(fileName+".json", "a", encoding="UTF-8") as file:
        #     json.dump(search_albums(search_artist(artist)), file, ensure_ascii=False)

        # I think this is a better way
        df = pd.DataFrame(download_data.albumsTab, columns=['album'])
        if len(sys.argv) == 4:
            plik = df.to_json(fileName + '.json')
        else:
            plik = df.to_json(artist + '.json')
    elif fileFormat == "EXCEL" or fileFormat == "excel":
        df = pd.DataFrame(download_data.albumsTab, columns=['album'])
        if len(sys.argv) == 4:
            plik = df.to_excel(fileName + ".xlsx", index=False, header=True)
        else:
            plik = df.to_excel(artist + ".xlsx", index=False, header=True)
    elif (fileFormat == "RAW" or fileFormat == "raw"):
        print(download_data.albumsTab)
    else:
        print("Wrong format")
    return plik
