class DatabaseService:
    def fetch_paid_order_totals(self):
        return [100, 200, 300]


class Logger:
    def log(self, message):
        print(message)


class DailySalesReport:
    def __init__(self, database:DatabaseService, logger:Logger)->None:
        self.database=database
        self.logger=logger
    

    def generate(self) -> None:
        totals = self.database.fetch_paid_order_totals()
        self.logger.log(f"Daily sales: {sum(totals)} EUR")


def main() -> None:
    DailySalesReport(DatabaseService(),Logger()).generate()


if __name__ == "__main__":
    main()