import os

class DataSet:
    def __init__(self, numeric_file, category_file, threshold=50):
        self.numeric_file = numeric_file
        self.category_file = category_file
        self.threshold = threshold
        self.data = []
        self.unique_categories = set()

        self.total = 0
        self.average = 0
        self.minimum = None
        self.maximum = None

        # ---------------------------------
        # 1 & 2. File Handling + Errors
        # ---------------------------------

    def load_data(self):
        # Load numerical data
        try:
            if not os.path.exists(self.numeric_file):
                raise FileNotFoundError("Numeric data file not found.")
            with open(self.numeric_file, "r") as file:
                lines = file.readlines()
                if not lines:
                    raise ValueError("Numeric data file is empty.")
                for line in lines:
                    value = line.strip()
                    if value == "":
                        continue
                    try:
                        self.data.append(float(value))
                    except ValueError:
                        print(f"Invalid value skipped: {value}")

            if len(self.data) == 0:
                raise ValueError("No valid numeric data found.")
        except Exception as e:
            print("Error loading numeric data:", e)
            return False
        
        # Load categorical data
        try:
            if not os.path.exists(self.category_file):
                raise FileNotFoundError("Category file not found.")
            with open(self.category_file, "r") as file:
                for line in file:
                    value = line.strip()
                    if value:
                        self.unique_categories.add(value)
        except Exception as e:
            print("Error loading category data:", e)
        return True
        
    #---------------------------------------
    # 3 & 4. Functions, Loops, Operators
    #---------------------------------------
    def calculate_total(self,data):
        total = 0
        for value in data:
            total += value
        return total
        
    def calculate_average(self, data):
        count = 0
        total = 0
        for value in data:
            total += value
        return total
        
    def calculate_minimum(self, data):
        minimum = data[0]
        for value in data:
            if value < minimum:
                minimum = value
        return minimum
        
    def calculate_maximum(self, data):
        maximum = data[0]
        for value in data:
            if value > maximum:
                maximum = value
        return maximum
        
    def calculate_statistics(self):
        self.total = self.calculate_total(self.data)
        self.average = self.calculate_average(self.data)
        self.minimum = self.calculate_minimum(self.data)
        self.maximum = self.calculate_maximum(self.data)


    #----------------------------------------------
    # 5. Conditional Statements
    #----------------------------------------------
    def performance_status(self):
        if self.average >= self.threshold:
            return "High Performance"
        else:
            return "Needs Improvement"
        
    #-----------------------------------------------
    # 7. Display Results
    #-----------------------------------------------
    def display_results(self):
        print("\n----- DATA ANALYSIS REPORT -----")
        print("Total:", self.total)
        print("Average:", self.average)
        print("Minimum:", self.minimum)
        print("Maximum:", self.maximum)
        print("Performance:", self.performance_status())
        print("Unique Categories:", len(self.unique_categories))
        print("-----------------------------------")

    
    #-----------------------------------------------
    # 8. Save Results to File
    #-----------------------------------------------
    def save_report(self, filename="report.txt"):
        with open(filename, "w") as file:
            file.write("DATA ANALYSIS REPORT\n")
            file.write("----------------------\n")
            file.write(f"Total: {self.total}\n")
            file.write(f"Average: {self.average}\n")
            file.write(f"Minimum: {self.minimum}\n")
            file.write(f"Maximum: {self.maximum}\n")
            file.write(f"Performance: {self.performance_status()}\n")
        print(f"\nReport saved to '{filename}'")


#------------------------------------------------
# Main Program
#------------------------------------------------
if __name__ == '__main__':
    dataset = DataSet(
        numeric_file="numbers.txt",
        category_file="categories.txt",
        threshold=50
    )

    if dataset.load_data():
        dataset.calculate_statistics()
        dataset.display_results()
        dataset.save_report()



