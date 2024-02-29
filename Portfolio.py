import requests
import matplotlib.pyplot as plt
class Portfolio:
    def __init__(self):
        self.stocks = []
        self.total_investment = 0
        self.sectors = {
            "Basic Materials": [],
            "Communication Services": [],
            "Consumer Cyclical": [],
            "Consumer Defensive": [],
            "Energy": [],
            "Financial Services": [],
            "Healthcare": [],
            "Industrials": [],
            "Miscellaneous": [],
            "Real Estate": [],
            "Technology": [],
            "Utilities": []
        }
        for stock in self.stocks:
            self.total_investment += stock.stock_value
        self.color_list = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']

    def add_stock(self, stock):
        self.stocks.append(stock)
        self.sectors[stock.sector].append(self.stocks)

    def get_stock(self, name):
        for stock in self.stocks:
            if stock.name == name:
                return stock

        return None


    def pie_chart(self, sector):
        plt.style.use("fivethirtyeight")
        if(sector == False):
            plt.title("Total Investment")
            plt.tight_layout()
            # will python trat doubles properly
            slices = []
            labels = []
            for stock in self.stocks:
                slices.append(stock.stock_value)
                labels.append(stock.name)
            plt.pie(slices, labels=labels, colors=self.color_list, wedgeprops={'edgecolor': 'black'})
            plt.show()
        else:
            plt.title("Total Investment By sector")
            plt.tight_layout()
            sector_totals = {key: 0 for key in self.sectors.keys()}
            for stock in self.stocks:
                sector_totals[stock.sector] += stock.stock_value
            slices = [amount for amount in sector_totals.values() if amount > 0]
            labels = [sector for sector, amount in sector_totals.items() if amount > 0]
            plt.pie(slices, labels=labels, colors=self.color_list, wedgeprops={'edgecolor': 'black'})
            plt.show()

        # Graphing method\

