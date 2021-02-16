import urllib.request
import json
apiKey = "L1I1Y71YJ5CIIBHR"


def getStockData(stockName):
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + stockName + "&apikey=" + apiKey
    connection = urllib.request.urlopen(url)
    result = connection.read().decode()
    print(result)
    return json.loads(result)


def main():
    while True:
        inp = input("ENTER A STOCK NAME (or 'exit' to exit : ")
        if(inp == "exit"):
            break
        result = getStockData(inp)
        toPrint = "The current price of " + inp + " is " + str(result['Global Quote']['05. price'])
        print(toPrint)


if __name__ == '__main__':
    main()

