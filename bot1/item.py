class item:
    def __init__(self,arr):
        self.name = arr[0].split('–')[0].strip()
        self.weights = arr[0].split('–')[-1].strip()
        self.nutrition_Score = arr[1].strip()
        self.Processing_type = arr[2].strip()
        self.green_score = arr[3].strip()


    def __str__(self):
        return f"Name: {self.name}, Weights: {self.weights}, Processing Type: {self.Processing_type}, Nutrition Score: {self.nutrition_Score}, Green Score: {self.green_score}"
    def to_dict(self):
        return {
            'name': self.name,
            'weights': self.weights,
            'nutrition_Score': self.nutrition_Score,
            'Processing_type': self.Processing_type,
            'green_score': self.green_score
        }