import csv

class CSVManager:
    def WriteData(directoryPath, fileName, collection):
        filePath = directoryPath + "/" + fileName
        with open(filePath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(collection)

    def WriteDictionaryData(directoryPath, fileName, dictionary):
        filePath = directoryPath + "/" + fileName
        with open(filePath, 'w') as csvfile:
            fieldnames = ['time', 'datatransferred']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for value in dictionary:
                writer.writerow(value)

    def ReadDictionaryData(filePath):
        with open(filePath) as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                data.append(row)
            return data

    def ReadData(filePath):
        with open(filePath, newline='') as f:
            reader = csv.reader(f)
            collection = []
            for row in reader:
                collection.append(row[0])
            return collection